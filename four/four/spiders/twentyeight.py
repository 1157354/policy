__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class TwentyeightSpider(scrapy.Spider):
    name = 'twentyeight'

    def start_requests(self):
        urls = ['http://www.china-language.gov.cn/fw/zwxxhpt/index.html']
        urls_ = ['http://www.china-language.gov.cn/fw/zwxxhpt/index_%s.html'%num for num in range(1,5)]
        urls.extend(urls_)

        for url in urls:
            # print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):
        # href_ = response.meta['url']
        # href_ = href_[0:(href_.rindex('/')+1)]
        listTxts = response.xpath('//*[@class="list-ty"]/ul//li')
        for li in listTxts:
            if li.xpath('./a/@href'):
                href = li.xpath('./a/@href').extract_first()
                href = response.urljoin(href)
                print('href:%s'%href)

                yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})



    def parse(self, response):


        title = response.xpath('//h1')
        title = title.xpath('string(.)').extract_first()
        merge = response.xpath('//*[@class="lyd"]/text()').extract_first()
        publishDate = re.findall('\d{4}-\d{2}-\d{2}',merge)[0]
        te = textEdit()
        text,files = te.dealWithAll(response,'con')
        print('text:%s'%text)
        print('file:%s'%files)
        item_twentyeight = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
