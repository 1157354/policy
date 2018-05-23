__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class ThirtySpider(scrapy.Spider):
    name = 'thirty'

    def start_requests(self):
        urls = ['http://www.caea.gov.cn/n6759295/n6759297/index.html']
        urls_ = ['http://www.caea.gov.cn/n6759295/n6759297/index_6771227_%s.html'%num for num in range(1,9)]
        urls.extend(urls_)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):
        # href_ = response.meta['url']
        # href_ = href_[0:(href_.rindex('/')+1)]
        listTxts = response.xpath('//*[@class="clearfix"]')
        for li in listTxts:
            if li.xpath('./dd/a/@href'):
                href = li.xpath('./dd/a/@href').extract_first()
                href = response.urljoin(href)
                print('href:%s'%href)
                yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})



    def parse(self, response):


        title = response.xpath('//*[@class="X_title"]/text()').extract_first()
        print(title)
        publishDate = response.xpath('//*[@class="X_time"]/ul/li[1]/text()').extract_first()
        publishDate = publishDate.split('：')[1]
        print(publishDate)

        te = textEdit()
        text,files = te.dealWithAll(response,classname='X_nr')
        print(text)
        print(files)
        item_twentynine = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        yield item_twentynine



