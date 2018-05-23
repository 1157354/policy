__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class ThirtyfiveSpider(scrapy.Spider):
    name = 'thirtyfive'

    def start_requests(self):
        urls = ['http://www.sapprft.gov.cn/sapprft/govpublic/10549.shtml']
        urls_ = ['http://www.sapprft.gov.cn/sapprft/govpublic/10549_%s.shtml'%num for num in range(2,8)]
        urls.extend(urls_)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.sasac.gov.cn/n2588035/n2588320/n2588335/c8470777/content.html',callback=self.parse)




    def parse_url(self, response):
            lis = response.xpath('//*[@class="h52"]/ul//li')
            for li in lis:
                if li.xpath('./span[2]/a/@href'):
                    href = li.xpath('./span[2]/a/@href').extract_first()
                    href = response.urljoin(href)
                    print('href:%s'%href)
                    yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})


    def parse(self, response):


        title = response.xpath('//title/text()').extract_first()
        print(title)
        publishDate = response.xpath('//*[@class="jar2_cfun"]/text()').extract_first()
        publishDate = publishDate.split(' ')[0]
        print(publishDate)
        te = textEdit()
        text,files = te.dealWithAll(response,id='artibody')
        print('text:%s'%text)
        print('file:%s'%files)
        item_thirtyfive = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        yield item_thirtyfive



        # te = textEdit()
        # text,files = te.dealWithAll(response,classname='sv_textcon')
        # print('text:%s'%text)
        # print('file:%s'%files)
        # item_thirtytwo=four.items.fillinData(title,'','','','','','','',IssuingOrgan,'','','','',text,files,publishDate,'')
        # yield item_thirtytwo




