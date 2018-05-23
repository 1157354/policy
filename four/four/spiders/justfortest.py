__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re

class FortestSpider(scrapy.Spider):
    name = 'fortest'

    def start_requests(self):
        urls = ['http://www.gov.cn/zhengce/zuixin.htm']

        for url in urls:
            print(url)
            # yield scrapy.Request(url=url, callback=self.parse_url)
            yield scrapy.Request(url=url,callback=self.parse_url)

    def parse_url(self, response):
        print('helloworld')
        pass
        # base_url = 'http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778'
        # listTxts = response.xpath('//*[@class="scy_lbsj-right-nr"]/ul//li')
        # for li in listTxts:
        #     href = li.xpath('./a/@href').extract_first()
        #     href = base_url + href[1:]
        #     print('href=%s' % href)
        #     yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})

    # def start_requests(self):
    #     urls = ['http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/201701/t20170118_295161.html']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)


