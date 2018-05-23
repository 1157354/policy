__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class TwentynineSpider(scrapy.Spider):
    name = 'twentynine'

    def start_requests(self):
        urls = ['http://www.audit.gov.cn/n8/n28/index.html']
        urls_ = ['http://www.audit.gov.cn/n8/n28/index_192_%s.html'%num for num in range(1,16)]
        urls.extend(urls_)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):
        # href_ = response.meta['url']
        # href_ = href_[0:(href_.rindex('/')+1)]
        listTxts = response.xpath('//*[@class="grey14_24"]')
        for li in listTxts:
            if li.xpath('./a/@href'):
                href = li.xpath('./a/@href').extract_first()
                href = response.urljoin(href)
                if href.startswith('http://www'):
                    yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})



    def parse(self, response):


        title = response.xpath('//*[@id="con_title"]/text()').extract_first()
        publishDate = response.xpath('//*[@id="con_time"]/text()').extract_first()
        publishDate = re.sub('\D','-',publishDate)
        publishDate = publishDate[:(len(publishDate)-1)]
        te = textEdit()
        text,files = te.dealWithAll(response,id='con_con')
        item_twentynine = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        yield item_twentynine



