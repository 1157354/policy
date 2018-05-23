__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *

class FortyfiveSpider(scrapy.Spider):
    name = 'fortyfive'

    def start_requests(self):
        urls = ['http://www.cma.gov.cn/root7/auto13139/']
        urls_ = ['http://www.cma.gov.cn/root7/auto13139/216/list_1856_%s.htm'%num for num in range(1,20)]
        urls.extend(urls_)
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})



    def parse_url(self, response):
            lis = response.xpath('//*[@class="mc"]')
            for li in lis:
                if li.xpath('./div/a/@href'):
                    href = li.xpath('./div/a/@href').extract_first()
                    href = response.urljoin(href)
                    print('href:%s'%href)
                    yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})


    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.cea.gov.cn/publish/dizhenj/465/527/760/20120216094235421961988/index.html',callback=self.parse)


    def parse(self, response):
        title = response.xpath('//title/text()').extract_first()
        print(title)
        indexNumber = response.xpath('//*[@id="headContainer"]/tbody/tr[1]/td/table/tr/td[1]/text()').extract_first()
        IssuingOrgan = response.xpath('//*[@id="headContainer"]/tbody/tr[3]/td/table/tr/td[1]/span/text()').extract_first()
        publishDate = response.xpath('//*[@id="headContainer"]/tbody/tr[3]/td/table/tr/td[2]/span/text()').extract_first()
        publishDate = re.sub('\D','-',publishDate)
        publishDate = publishDate[:-1]
        print('indexNumber:%s'%indexNumber)
        print('IssuingOrgan:%s'%IssuingOrgan)
        print('publishDate:%s'%publishDate)
        te = textEdit()
        text,files = te.dealWithAll(response,classname="content")
        print('text:%s'%text)
        print('files:%s'%files)
        item_fortyfive = four.items.fillinData(title,'','','','','',indexNumber,'',IssuingOrgan,'','','','',text,files,publishDate,'')
        yield item_fortyfive



        # merge = response.xpath('//*[@class="detail_main_right_conbg_tit"]/div[3]/text()').extract_first()
        # merge = merge.split(' ')
        # publishDate = merge[0].split('：')[1]
        # print('publishDate:%s'%publishDate)
        # te = textEdit()
        # text,files = te.dealWithAll(response,classname="detail_main_right_conbg_con")
        # print('text:%s'%text)
        # print('files:%s'%files)
        # item_fortyfour = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,'')
        # yield item_fortyfour





        # publishDate = response.xpath('//*[@name="PubData"]/@content').extract_first()
        # print(publishDate)
        # source = response.xpath('//*[@name="ContentSource"]/@content').extract_first()
        # print(source)
        #
        # te = textEdit()
        # text,files = te.dealWithAll(response,id="zoom")
        # print('text:%s'%text)
        # print('file:%s'%files)
        # item_fortythree = four.items.fillinData(title,'','','','','','','','','','','','',text,files,publishDate,source)
        # yield item_fortythree










