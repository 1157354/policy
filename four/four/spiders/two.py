__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class TwoSpider(scrapy.Spider):
    name = 'two'

    def start_requests(self):
        urls = ['http://www.chinapolicy.net/list.php?fid-41-page-%s.htm'%num for num in range(1,100)]

        for url in urls:
            # print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):

        listTxts = response.xpath('//*[@id="list_article"]/tr[2]/td/table//tr/td/span/a/@href').extract()
        for li in listTxts:
            href = response.urljoin(li)
            yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})

        # for li in listTxts:
        #     if li.xpath('./a/@href'):
        #         href = li.xpath('./a/@href').extract_first()
        #         href = response.urljoin(href)
        #         print('href:%s'%href)
        #
        #         yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})



    def parse(self, response):


        title = response.xpath('//*[@class="main_title"]/text()').extract_first()
        print('title',title)
        publishDate = response.xpath('//*[@class="top_about"]/a/text()').extract_first()
        publishDate = publishDate.split(' ')[0]
        print('publish',publishDate)
        te = textEdit()
        text,files = te.dealWithAll(response,classname='content_word')
        print('text:%s'%text)
        print('file:%s'%files)
        item_two = four.items.fillinData(title,'','',None,'','','','','','','','','',text,files,publishDate,'',response.meta['url'])
        yield item_two
