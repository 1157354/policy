__author__ = 'tian'
__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests

class FiftySpider(scrapy.Spider):
    name = 'fifty'

    def start_requests(self):
        urls = ['http://zfxxgk.safea.gov.cn/list.shtml?scatcode%3D%CE%C4%BD%CC%C0%E0%26scatname%3D%D5%FE%B2%DF%B7%A8%B9%E6',\
                'http://zfxxgk.safea.gov.cn/list.shtml?scatcode%3D%CE%C4%BD%CC%C0%E0%26scatname%3D%D5%FE%B2%DF%B7%A8%B9%E6',\
                'http://zfxxgk.safea.gov.cn/list.shtml?scatcode%3D%D7%DB%BA%CF%C0%E0%26scatname%3D%D5%FE%B2%DF%B7%A8%B9%E6',\
                'http://zfxxgk.safea.gov.cn/list.shtml?scatcode%3D%C5%E0%D1%B5%C0%E0%26scatname%3D%D5%FE%B2%DF%B7%A8%B9%E6',
                'http://zfxxgk.safea.gov.cn/list.shtml?scatcode%3D%BE%AD%BC%BC%C0%E0%26scatname%3D%D5%FE%B2%DF%B7%A8%B9%E6',\
                'http://zfxxgk.safea.gov.cn/list.shtml?scatcode%3D%26scatname%3D%D5%FE%B2%DF%B7%A8%B9%E6']
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    def parse_url(self, response):
        listTxts = response.xpath('//*[@class="zfxxlist"]')
        for li in listTxts:
            href = li.xpath('./ul/li[2]/a/@href').extract_first()
            if href:
                print('href=%s' % href)
                yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})

    # def start_requests(self):
    #     urls = ['http://zfxxgk.safea.gov.cn/content.php?identifier%3D000014402%2F2008-00317']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse,meta={'url': url})

    def parse(self, response):
        indexNumber = response.xpath('//*[@class="zfxxgk_content"]/p[3]/text()').extract_first()
        # print('index:%s'%indexNumber)
        topicClass = response.xpath('//*[@class="zfxxgk_content"]/p[5]/text()').extract_first()
        # print('topic:%s'%topicClass)
        title = response.xpath('//*[@class="zfxxgk_content"]/p[7]/b/text()').extract_first()
        if not title:
            title = response.xpath('//*[@class="zfxxgk_content"]/p[7]/b/font/text()').extract_first()
        # print('title:%s'%title)
        IssuingOrgan = response.xpath('//*[@class="zfxxgk_content"]/p[9]/text()').extract_first()
        # print('IssuingOrgan:%s'%IssuingOrgan)
        releaseDate = response.xpath('//*[@class="zfxxgk_content"]/p[11]/text()').extract_first()
        # print('releaseDate:%s'%releaseDate)
        IssuedNumber = response.xpath('//*[@class="zfxxgk_content"]/p[13]/text()').extract_first()
        # print('IssuedNumber:%s'%IssuedNumber)
        metaKeywords = response.xpath('//*[@class="zfxxgk_content"]/p[15]/text()').extract_first()
        # print('metaKeywords:%s'%metaKeywords)
        text = response.xpath('//*[@class="zfxxgk_content"]/p[24]').extract()
        # print('text:%s'%text)
        item_fifty = four.items.fillinData(title,metaKeywords,'','','','',indexNumber,topicClass,\
                                           IssuingOrgan,'',IssuedNumber,releaseDate,'',text,'','','')
        yield item_fifty




