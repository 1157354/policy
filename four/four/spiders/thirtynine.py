__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class ThirtynineSpider(scrapy.Spider):
    name = 'thirtynine'

    def start_requests(self):
        urls = ['http://www.ggj.gov.cn/zcfg/fgxwj/index.htm']
        urls_ = ['http://www.ggj.gov.cn/zcfg/fgxwj/index_%s.htm'%num for num in range(1,30)]
        urls.extend(urls_)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.sasac.gov.cn/n2588035/n2588320/n2588335/c8470777/content.html',callback=self.parse)




    def parse_url(self, response):
            lis = response.xpath('//*[@class="listbox boxcenter"]//dt')
            for li in lis:
                if li.xpath('./a/@href'):
                    href = li.xpath('./a/@href').extract_first()
                    href = response.urljoin(href)
                    print('href:%s'%href)
                    yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})


    def parse(self, response):

        title = response.xpath('//h1')
        title = title.xpath('string(.)').extract_first()
        # title = response.xpath('//h1/text()').extract_first()
        print(title)
        source = response.xpath('//*[@class="fl"]/span[1]/text()').extract_first()
        print(source)
        publishDate = response.xpath('//*[@class="fl"]/span[3]/text()').extract_first()
        publishDate = publishDate.split(' ')[0]
        print(publishDate)
        te = textEdit()
        text,files = te.dealWithAll(response,classname="conbox2 boxcenter")
        print('text:%s'%text)
        print('file:%s'%files)
        item_thirtynine = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        yield item_thirtynine





