__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class FortytwoSpider(scrapy.Spider):
    name = 'fortytwo'

    def start_requests(self):
        urls = ['http://www.hmo.gov.cn/zcfg_new/xf/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.sasac.gov.cn/n2588035/n2588320/n2588335/c8470777/content.html',callback=self.parse)




    def parse_url(self, response):
            lis = response.xpath('//*[@class="itemList"]/ul//li')
            for li in lis:
                if li.xpath('./a/@href'):
                    href = li.xpath('./a/@href').extract_first()
                    href = response.urljoin(href)
                    print('href:%s'%href)
                    yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})


    def parse(self, response):
        title = response.xpath('//*[@class="pageHead"]/h2/text()').extract_first()
        print(title)
        publishDate = response.xpath('//*[@class="pageHead"]/h3/span[1]/text()').extract_first()
        print(publishDate)

        te = textEdit()
        text,files = te.dealWithAll(response,classname="view TRS_UEDITOR trs_paper_default trs_word trs_key4format")
        if not text:
            text,files = te.dealWithAll(response,classname="TRS_Editor")
        print('text:%s'%text)
        print('file:%s'%files)
        item_fortyone = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        yield item_fortyone










