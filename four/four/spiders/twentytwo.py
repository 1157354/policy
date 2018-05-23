__author__ = 'tian'
#=====================http://www.mofcom.gov.cn/article/b/c/201804/20180402733178.shtml==========================

import scrapy
from four.items import FourItem
import four.items
import re

class TwentytwoSpider(scrapy.Spider):
    name = 'twentytwo'

    def start_requests(self):
        urls = ['http://www.mofcom.gov.cn/article/b/']

        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_url)



