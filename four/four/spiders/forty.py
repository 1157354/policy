__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class FortySpider(scrapy.Spider):
    name = 'forty'

    def start_requests(self):
        urls = ['http://www.gqb.gov.cn/zcfg/index.shtml']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.sasac.gov.cn/n2588035/n2588320/n2588335/c8470777/content.html',callback=self.parse)




    def parse_url(self, response):
            lis = response.xpath('//*[@class="left_list_hjpd_bt"]')
            for li in lis:
                if li.xpath('./a/@href'):
                    href = li.xpath('./a/@href').extract_first()
                    href = response.urljoin(href)
                    print('href:%s'%href)
                    # yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})


    def parse(self, response):
        title = response.xpath('//*[@name="title"]/@content').extract_first()
        print(title)
        publishDate = response.xpath('//*[@class="sp_time"]/font/text()').extract_first()
        publishDate = publishDate.split('：')[1]
        print(publishDate)
        te = textEdit()
        text,files = te.dealWithAll(response,id="zoom")
        print('text:%s'%text)
        print('file:%s'%files)










