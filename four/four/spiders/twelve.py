__author__ = 'tian'
import scrapy
import four.items
import re

class Twelve(scrapy.Spider):
    name = 'twelve'

    def start_requests(self):
        url = 'http://www.mca.gov.cn/article/yw/shjzgl/fgwj/'