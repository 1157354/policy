__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re

class TwentyfourSpider(scrapy.Spider):
    name = 'twentyfour'

    def start_requests(self):
        pass



