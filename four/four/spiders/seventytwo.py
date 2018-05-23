import time

__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION
from four.textEdit import *
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeventytwoSpider(scrapy.Spider):
    name = 'seventytwo'

    def start_requests(self):
        urls = ['http://gkml.customs.gov.cn/tabid/1033/ctl/InfoDetail/InfoID/{}/mid/445/Default.aspx?ContainerSrc=%5bG%5dContainers%2f_default%2fNo+Container'.format(num) for num in range(1,32000)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,meta={'url':url})

    # def start_requests(self):
    #     urls = ['http://gkml.customs.gov.cn/tabid/1033/ctl/InfoDetail/InfoID/31318/mid/445/Default.aspx?ContainerSrc=%5bG%5dContainers%2f_default%2fNo+Container']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse,meta={'url':url})


    def parse(self, response):
        if response.xpath('//*[@name="docdate"]'):
            title = response.xpath('//title/text()').extract_first()
            title = title.strip()
            indexNumber = response.xpath('//*[@id="ess_ctr445_ModuleContent"]/table/tr[1]/td[2]/text()').extract_first()
            print('title',title)
            print('index',indexNumber)
            IssuedNumber = response.xpath('//*[@id="ess_ctr445_ModuleContent"]/table/tr[3]/td[2]/text()[2]').extract_first()
            print('Issued',IssuedNumber)
            publishDate = response.xpath('//*[@id="ess_ctr445_ModuleContent"]/table/tr[4]/td[2]/text()').extract_first()
            print('publish',publishDate)
            IssuedOrgan = response.xpath('//*[@id="ess_ctr445_ModuleContent"]/table/tr[5]/td[4]/text()').extract_first()
            print('Issued',IssuedOrgan)
            te = textEdit()
            text,files = te.dealWithAll(response,id='ess_ctr445_ModuleContent')
            print('text',text)
            print('files',files)
            item_seventytwo = four.items.fillinData(title,'','','','','',indexNumber,'',IssuedOrgan,'',IssuedNumber,'','',text,files,publishDate,'')
            yield item_seventytwo




















