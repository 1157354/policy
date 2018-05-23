__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings

class SixtysixSpider(scrapy.Spider):
    name = 'sixtysix'

    def start_requests(self):
        urls = ['http://www.jianzai.gov.cn//DRpublish/zcfg/000100010008-%s.html'%num for num in range(1,7)]
        for url in urls:
            print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     urls = ['http://www.sastind.gov.cn/n4235/n6654336/index.html']
    #
    #     for url in urls:
    #         # print('url:%s'%url)
    #         yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):
        # prefix_url = 'http://www.sbsm.gov.cn/zwgk/zcfgjjd/gfxwj'
        listTxts = response.xpath('//*[@id="con_tdwo_1"]/table/tbody//tr')
        for li in listTxts:
            href = li.xpath('./td[2]/a/@href').extract_first()
            print('href:%s'%href)
            yield scrapy.Request(url=href, callback=self.parse)



    def parse(self, response):
        title = response.xpath('//*[@class="tgaozhengwentxet"]/text()').extract_first()
        merge = response.xpath('//*[@class="tgaozhengwen1"]/tbody/tr[2]/td/text()').extract_first()
        merge = merge.split(' ')
        source = merge[1]
        publishDate = merge[2]
        publishDate = publishDate.split('：')[1]
        text = response.xpath('//*[@id="textflag"]/p').extract()
        text = ' '.join(text)
        item_sixtysix = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,source)
        yield item_sixtysix








