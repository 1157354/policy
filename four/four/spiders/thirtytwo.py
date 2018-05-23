__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class ThirtytwoSpider(scrapy.Spider):
    name = 'thirtytwo'

    def start_requests(self):
        urls = ['http://www.chinatax.gov.cn/n810341/n810755/index.html']
        urls_ = ['http://www.chinatax.gov.cn/n810341/n810755/index_2420064_%s.html'%num for num in range(1,42)]
        urls.extend(urls_)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.sasac.gov.cn/n2588035/n2588320/n2588335/c8470777/content.html',callback=self.parse)



                    
    def parse_url(self, response):
            href = response.meta['url']
            if href.endswith('index.html'):
                lis = response.xpath('//*[@id="comp_2420064"]/dl//dd')
                print('1')
                for li in lis:
                    print('2')
                    if li.xpath('./a/@href'):
                        href = li.xpath('./a/@href').extract_first()
                        href = response.urljoin(href)
                        print('href:%s'%href)
                        yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})
            else:
                lis = response.xpath('//dd')
                print('3')
                for li in lis:
                    print('4')
                    if li.xpath('./a/@href'):
                        href = li.xpath('./a/@href').extract_first()
                        href = response.urljoin(href)
                        print('href:%s'%href)
                        yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})

    def parse(self, response):


        title = response.xpath('//*[@name="title"]/@content').extract_first()
        print(title)
        publishDate = response.xpath('//*[@name="pubdate"]/@content').extract_first()
        print(publishDate)
        IssuingOrgan = response.xpath('//*[@name="mediaid"]/@content').extract_first()
        print(IssuingOrgan)


        te = textEdit()
        text,files = te.dealWithAll(response,classname='sv_textcon')
        print('text:%s'%text)
        print('file:%s'%files)
        item_thirtytwo=four.items.fillinData(title,'','','','','','','',IssuingOrgan,'','','','',text,files,publishDate,'')
        yield item_thirtytwo
        # item_twentynine = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        # yield item_twentynine



