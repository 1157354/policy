__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class ThreeSpider(scrapy.Spider):
    name = 'three'

    def start_requests(self):
        urls = ['http://www.ccgp.gov.cn/gpsr/zcfg/']

        for url in urls:
            # print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):

        listTxts = response.xpath('//*[@class="c_list_tat"]//li')
        for li in listTxts:
            link = li.xpath('./a/@href').extract_first()
            href = response.urljoin(link)
            print(href)
            yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})



    def parse(self, response):


        title = response.xpath('//h2/text()').extract_first()
        print('title',title)
        publishDate = response.xpath('//*[@id="pubTime"]/text()').extract_first()
        publishDate = publishDate.split(' ')[0]
        publishDate = re.sub('\D','-',publishDate)
        publishDate = publishDate[:-1]
        print('publish',publishDate)
        source = response.xpath('//*[@id="sourceName"]/text()').extract_first()
        print('source',source)
        te = textEdit()
        text,files = te.dealWithAll(response,classname='TRS_Editor')
        print('text:%s'%text)
        print('file:%s'%files)
        item_two = four.items.fillinData(title,'','',None,'','','','','','','','','',text,files,publishDate,'',response.meta['url'])
        yield item_two
