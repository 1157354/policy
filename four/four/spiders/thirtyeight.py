__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class ThirtyeightSpider(scrapy.Spider):
    name = 'thirtyeight'

    def start_requests(self):
        urls = ['http://www.sara.gov.cn/zcfg/zc/zywj20170904204343165711/index.htm','http://www.sara.gov.cn/zcfg/zc/zywj20170904204343165711/index1.htm']


        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.sasac.gov.cn/n2588035/n2588320/n2588335/c8470777/content.html',callback=self.parse)




    def parse_url(self, response):
            lis = response.xpath('//*[@class="list01"]//li')
            for li in lis:
                if li.xpath('./a/@href'):
                    href = li.xpath('./a/@href').extract_first()
                    href = response.urljoin(href)
                    print('href:%s'%href)
                    yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})


    def parse(self, response):


        title = response.xpath('//title/text()').extract_first()
        print(title)
        publishDate = response.xpath('//*[@class="articleAuthor"]/span/strong/text()').extract_first()
        if publishDate:
            publishDate = publishDate.split(' ')[0]
        print(publishDate)
        te = textEdit()
        text,files = te.dealWithAll(response,classname="article art")
        print('text:%s'%text)
        print('file:%s'%files)
        item_thirtyeight = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        yield item_thirtyeight





        # te = textEdit()
        # text,files = te.dealWithAll(response,classname='sv_textcon')
        # print('text:%s'%text)
        # print('file:%s'%files)
        # item_thirtytwo=four.items.fillinData(title,'','','','','','','',IssuingOrgan,'','','','',text,files,publishDate,'')
        # yield item_thirtytwo




