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
    name = 'thirtyone'

    def start_requests(self):
        urls = ['http://www.sasac.gov.cn/n2588035/n2588320/n2588335/index.html']
        urls_ = ['http://www.sasac.gov.cn/n2588035/n2588320/n2588335/index_2603340_%s.html'%num for num in range(1,13)]
        urls.extend(urls_)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.sasac.gov.cn/n2588035/n2588320/n2588335/c8470777/content.html',callback=self.parse)


    def parse_url(self, response):
        href = response.meta['url']
        if href.endswith('index.html'):
            lis = response.xpath('//*[@id="comp_2603340"]//li')
            for li in lis:
                if li.xpath('./a/@href'):
                    href = li.xpath('./a/@href').extract_first()
                    href = response.urljoin(href)
                    print('href:%s'%href)
                    yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})
        else:
            lis = response.xpath('//li')
            for li in lis:
                if li.xpath('./a/@href'):
                    href = li.xpath('./a/@href').extract_first()
                    href = response.urljoin(href)
                    print('href:%s'%href)
                    yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})






        # te = textEdit()
        # text,files = te.dealWithAll(response,classname='X_nr')
        # print(text)
        # print(files)
        # item_twentynine = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        # yield item_twentynine

    def parse(self, response):


        title = response.xpath('//*[@class="zsy_cotitle"]/text()').extract_first()
        # print(title)
        publishDate = response.xpath('//*[@class="zsy_cotitle"]/p/text()').extract_first()
        publishDate = re.findall('\d{4}-\d{2}-\d{2}',publishDate)[0]
        # print(publishDate)
        te = textEdit()
        text,files = te.dealWithAll(response,classname='zsy_comain')
        item_thirtyone = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        yield item_thirtyone

