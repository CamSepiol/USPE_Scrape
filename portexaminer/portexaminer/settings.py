# -*- coding: utf-8 -*-

# Scrapy settings for portexaminer project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'portexaminer'

SPIDER_MODULES = ['portexaminer.spiders']
NEWSPIDER_MODULE = 'portexaminer.spiders'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 128

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'portexaminer.middlewares.PortexaminerSpiderMiddleware': 543,
#}


#Rotating Proxies list#
ROTATING_PROXY_LIST = [
    '82.114.92.122:41837',
    '81.16.10.141:54544',
    '149.28.169.27:3128',
    '195.149.221.1:3128',
    '103.231.163.58:48325',
    '181.115.168.35	:45905',
    '177.67.139.209:80',
    '186.225.45.146:58111',
    '200.153.145.174:58809',
    '103.239.54.177:53516',
    '119.82.253.103:51004',
    '175.100.30.156:25',
    '201.184.169.194:47241',
    '181.129.42.179:36771',
    '77.48.137.65:33748',
    '136.243.48.32:808',
    '94.21.118.140:33706',
    '117.200.53.210:38910',
    '119.235.248.165:8080',
    '115.124.86.250:48203',
    '41.139.159.34:56926',
    '114.108.181.130:34003',
    '187.188.213.4:33815',
    '86.123.166.109:8080',
    '213.222.244.150:61436',
    '95.66.140.121:45592',
    '83.234.206.165:55044',
    '195.208.36.45:52949',
    '31.173.94.93:37463',
    '84.53.247.204:53281',
    '62.33.210.34:55187',
    '87.103.234.116:3128',
    '122.117.65.107:0292',
    '31.202.30.118:54547',
    '178.151.205.154:55101',
    '77.121.160.9:55148',
    '195.211.174.34:51634'


]
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'portexaminer.middlewares.PortexaminerDownloaderMiddleware': 543,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'portexaminer.pipelines.PortexaminerPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = False
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
#each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
