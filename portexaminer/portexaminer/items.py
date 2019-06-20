# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PortExaminerItem(scrapy.Item):
    ###consignee details###
    c_name = scrapy.Field()
    c_address = scrapy.Field()

    ###shipper details###
    s_name = scrapy.Field()
    s_address = scrapy.Field()

    ###notify party details###
    n_name = scrapy.Field()
    n_address = scrapy.Field()

    ###product details###
    product_desc = scrapy.Field()
    weight = scrapy.Field()
    weight_unit = scrapy.Field()
    piece_count = scrapy.Field()
    piece_unit = scrapy.Field()


    ###Shipping Mode and Details###
    bol_number = scrapy.Field()
    shipping_date = scrapy.Field()
    business_type = scrapy.Field()
    unloading_port = scrapy.Field()
    loading_port = scrapy.Field()
    unloading_country = scrapy.Field()
    loading_country = scrapy.Field()
    teu = scrapy.Field()


