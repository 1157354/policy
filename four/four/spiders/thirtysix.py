__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class ThirtysixSpider(scrapy.Spider):
    name = 'thirtysix'

    def start_requests(self):
        urls = ['http://www.forestry.gov.cn/CommonAction.do?dispatch=more&colid=5461&p=1&t=1526544257572']


        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.sasac.gov.cn/n2588035/n2588320/n2588335/c8470777/content.html',callback=self.parse)




    def parse_url(self, response):
            lis = response.xpath('//*[@class="con cl"]/ul//li')
            for li in lis:
                if li.xpath('./a/@href'):
                    href = li.xpath('./a/@href').extract_first()
                    href = response.urljoin(href)
                    print('href:%s'%href)
                    yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})


    def parse(self, response):


        title = response.xpath('//h1/text()').extract_first()
        print(title)
        publishDate = response.xpath('//*[@class="date"]/text()').extract_first()
        publishDate = re.sub('\D','-',publishDate)
        publishDate = publishDate[:-1]
        te = textEdit()
        text,files = te.dealWithAll(response,id='forestry_content')
        print('text:%s'%text)
        print('file:%s'%files)
        item_thirtysix = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        yield item_thirtysix





        # te = textEdit()
        # text,files = te.dealWithAll(response,classname='sv_textcon')
        # print('text:%s'%text)
        # print('file:%s'%files)
        # item_thirtytwo=four.items.fillinData(title,'','','','','','','',IssuingOrgan,'','','','',text,files,publishDate,'')
        # yield item_thirtytwo




