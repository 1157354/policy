__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

#==========待完成===========

class ThirtythreeSpider(scrapy.Spider):
    name = 'thirtythree'

    def start_requests(self):
        urls = ['']


        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.sasac.gov.cn/n2588035/n2588320/n2588335/c8470777/content.html',callback=self.parse)



                    
    def parse_url(self, response):
            pass

    def parse(self, response):

        pass



