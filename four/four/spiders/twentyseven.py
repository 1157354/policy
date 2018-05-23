__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class TwentysixSpider(scrapy.Spider):
    name = 'twentyseven'

    def start_requests(self):
        urls = ['http://www.cnsa.gov.cn/n6758823/n6758839/index.html']
        urls_ = ['http://www.cnsa.gov.cn/n6758823/n6758839/index_6768779_%s.html'%num for num in range(1,5)]
        urls.extend(urls_)

        for url in urls:
            # print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):
        prefix_url = 'http://www.cnsa.gov.cn'
        listTxts = response.xpath('//*[@class="tongyongLb"]/ul//li')
        for li in listTxts:
            href = li.xpath('./a/@href').extract_first()
            href = prefix_url + href[5:]
            print('href:%s'%href)
            yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})



    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        publishDate = response.xpath('//*[@class="information"]/span[1]/text()').extract_first()
        publishDate = publishDate.split('：')[1]
        publishDate = re.sub('\D','-',publishDate)
        text = response.xpath('//*[@class="conText"]').extract()
        text = ' '.join(text)
        item_twentyseven = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,'')
        yield item_twentyseven