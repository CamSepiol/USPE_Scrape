from scrapy import Spider, Request
from ..items import PortExaminerItem
import re


class PortExaminerSpider(Spider):
    name = "portexaminerTZ"
    allowed_domains = ["www.usportexaminer.com"]
    start_urls = ["http://www.usportexaminer.com/"]


    def parse(self, response):

        #pulls urls for A-Z pagination at bottom of homepage#
        result_urls = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "left-ftr", " " ))]//@href').extract()

        #there is no "Y" category so we delete this from the list#
        del result_urls[-2]

        #Calls only categories T-Z to split result URL's between 5 concurrent spiders#
        result_urls = result_urls[19:25]

        for url in result_urls:
            yield Request(url=url, callback=self.parse_category_page)

    def parse_category_page(self, response):
        #alphaSort stores the current Letter (A-Z) category#
        alphaSort = response.xpath('//*[@id="wrapper"]/section/article/div/table/tr[1]/td[1]/span/a/@title').extract_first().strip()[0]
        #pulls the URL for the last page of the current A-Z category#
        lastPageURL = response.xpath('//li[(((count(preceding-sibling::*) + 1) = 21) and parent::*)]//a/@href').get().strip()
        #stores the integer value of the last page for use in list comprehension below#
        numPages = int(re.findall(r'\d+', lastPageURL)[0])

        #Creates a list of URLS for each page in the current category#
        letter_urls = ['http://www.usportexaminer.com/companies/{}.php&page={}'.format(alphaSort, x) for x in range(1, numPages+1)]

        for url in letter_urls:
            yield Request(url=url, callback=self.parse_companies_page)

    def parse_companies_page(self, response):
        #creates a list of URL's for each shipment on the current page#
        shipment_urls = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "text", " " ))]//a/@href').extract()

        for url in shipment_urls:
            yield Request(url=url, callback=self.parse_shipment_page)

    def parse_shipment_page(self, response):
        item = PortExaminerItem()

        #customer variables#
        c_name = response.xpath('//*[@id="wrapper"]/section/article[4]/div[2]/div[1]/table/tr[1]/td[2]//text()').extract_first().strip()
        c_address = response.xpath('//*[@id="wrapper"]/section/article[4]/div[2]/div[1]/table/tr[2]/td[2]//text()').extract_first().strip()

        #shipper variables#
        s_name = response.xpath('//*[@id="wrapper"]/section/article[5]/div[2]/div[1]/table/tr[1]/td[2]//text()').extract_first().strip()
        s_address = response.xpath('//*[@id="wrapper"]/section/article[5]/div[2]/div[1]/table/tr[2]/td[2]//text()').extract_first().strip()

        #notify party variables#

        # checks for string value before stripping to prevent scraping errors"
        n_name = response.xpath('//*[@id="wrapper"]/section/article[6]/div[2]/div[1]/table/tr[1]/td[2]//text()').extract_first()
        if n_name is not None:
            n_name = n_name.strip()
        # checks for string value before stripping to prevent scraping errors"
        n_address = response.xpath('//*[@id="wrapper"]/section/article[6]/div[2]/div[1]/table/tr[2]/td[2]//text()').extract_first()
        if n_address is not None:
            n_address = n_address.strip()

        #shipment info variables#
        product_desc = response.xpath('//*[@id="wrapper"]/section/article[2]/div[2]/div[2]/table/tr[2]/td//text()').extract_first().strip()
        bol_number = response.xpath('//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[1]/td[2]/span//text()').extract_first().strip()
        shipping_date = response.xpath('//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[2]/td[2]/span//text()').extract_first().strip()


        weight = int(response.xpath(
            '//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[3]/td[2]/span//text()').extract_first().strip())
        weight_unit = response.xpath(
            '//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[4]/td[2]/span//text()').extract_first().strip()
        piece_count = int(response.xpath(
            '//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[5]/td[2]/span//text()').extract_first().strip())
        piece_unit = response.xpath(
            '//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[6]/td[2]/span//text()').extract_first().strip()

        #checks for string value before stripping to prevent scraping errors"
        unloading_port = response.xpath(
            '//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[7]/td[2]/span//text()').extract_first()
        if unloading_port is not None:
            unloading_port = unloading_port.strip()

        # checks for string value before stripping to prevent scraping errors"
        loading_port = response.xpath(
            '//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[8]/td[2]/span//text()').extract_first()
        if loading_port is not None:
            loading_port = loading_port.strip()

        business_type = response.xpath(
            '//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[9]/td[2]/span//text()').extract_first().strip()
        unloading_country = response.xpath(
            '//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[10]/td[2]/span//text()').extract_first().strip()
        loading_country = response.xpath(
            '//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[11]/td[2]/span//text()').extract_first().strip()

        #Twenty foot container Equivalent Units#
        teu = int(response.xpath(
            '//*[@id="wrapper"]/section/article[7]/div[2]/div/table/tr/td[2]/table/tr[12]/td[2]/span//text()').extract_first().strip())


        #Items to yield#
        item["c_name"] = c_name
        item["c_address"] = c_address

        item["s_name"] = s_name
        item["s_address"] = s_address

        item["n_name"] = n_name
        item["n_address"] = n_address

        item["product_desc"] = product_desc
        item["bol_number"] = bol_number
        item["shipping_date"] = shipping_date
        item["weight"] = weight
        item["weight_unit"] = weight_unit
        item["piece_count"] = piece_count
        item["piece_unit"]= piece_unit
        item["unloading_port"] = unloading_port
        item["loading_port"] = loading_port
        item["business_type"] = business_type
        item["unloading_country"] = unloading_country
        item["loading_country"] = loading_country
        item["teu"] = teu

        yield item