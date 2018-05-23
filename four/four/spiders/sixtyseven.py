__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings

class SixtysevenSpider(scrapy.Spider):
    name = 'sixtyseven'

    def start_requests(self):
        urls = ['http://www.xzqh.org.cn/index.php/article-lists-category-204-p-%s.html'%num for num in range(1,10)]
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
        prefix_url = 'http://www.xzqh.org.cn'
        listTxts = response.xpath('//*[@class="ul_list"]//li')
        for li in listTxts:
            href = li.xpath('./a/@href').extract_first()
            href = prefix_url + href
            print('href:%s'%href)
            yield scrapy.Request(url=href, callback=self.parse)



    def parse(self, response):
        title = response.xpath('//h2/text()').extract_first()
        merge = response.xpath('//*[@class="pull-left"]/span/text()').extract_first()
        merge = merge.split(' ')
        print(merge)
        publishDate = merge[0].split('：')[1]
        source = merge[3].split('：')[1]
        print('publish:%s'%publishDate)
        print('source:%s'%source)
        text = response.xpath('//*[@id="content"]/p').extract()
        text = ' '.join(text)
        print(text)
        item_sixtyseven = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,'')
        yield item_sixtyseven





