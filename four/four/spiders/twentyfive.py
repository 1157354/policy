__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION

class TwentysixSpider(scrapy.Spider):
    name = 'twentysix'

    # def start_requests(self):
    #     urls = ['http://www.nhfpc.gov.cn/zwgk/wenji/list.shtml']
    #     urls_ = ['http://www.nhfpc.gov.cn/zwgk/wenji/list_%s.shtml'%num for num in range(2,126)]
    #     urls.extend(urls_)
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse_url)

    def start_requests(self):
        urls = ['http://www.nhfpc.gov.cn/fys/s3590/201804/b926a644b43d4ee68b6f26d1a8470b59.shtml']

        for url in urls:
            # print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse,meta={'url':url})


    def parse_url(self, response):
        prefix_url = 'http://www.nhfpc.gov.cn'
        listTxts = response.xpath('//*[@class="zwgklist"]//li')
        for li in listTxts:
            href = li.xpath('./h3/a/@href').extract_first()
            href = prefix_url + href[5:]
            print('href:%s'%href)
            yield scrapy.Request(url=href, callback=self.parse,meta={'url':href})



    def parse(self, response):

        # url_ = response.meta['url']
        # prefix_url = 'http://www.nhfpc.gov.cn'
        # text_found=False
        # while not text_found:
        #     text = self.getText(response,classname='con')
        #     if text:
        #         text_found = True
        # print('text:%s'%text)
        # text_ = response.xpath('//*[@class="con"]')
        # dict_file = self.dealWithText(text_,prefix_url)
        # print('dict_file:%s'%dict_file)
        # _text = self.textReedit(text,dict_file)
        # print('_text:%s'%_text)
        result = self.dealWithAll(response,classname='con',prefix_url='http://www.nhfpc.gov.cn')
        print('result:%s'%result)


    def dealWithAll(self,response,classname='',id='',prefix_url=''):

        text = self.getText(response,classname,id)
        if classname:
            classname_ = '\"'+classname+'\"'
            text_ = response.xpath('//*[@class=%s]'%classname_)
            dict_file = self.dealWithText(text_,prefix_url)
            print('dict_file:%s'%dict_file)
            _text = self.textReedit(text,dict_file)
            return _text
        elif id:
            id = '\"'+id+'\"'
            text_ = response.xpath('//*[@id=%s]'%id)
            dict_file = self.dealWithText(text_,prefix_url)
            print('dict_file:%s'%dict_file)
            _text = self.textReedit(text,dict_file)
            return _text

    def getText(self,response,classname='',id=''):
        connected = True
        while response.status != 200:
            print('...%s'%response.status)
            connected = False
        if connected:
            if classname:
                classname = '\"'+classname+'\"'
                text = response.xpath('//*[@class=%s]'%classname).extract()
                text = ' '.join(text)
                return text
            elif id:
                id = '\"'+id+'\"'
                text = response.xpath('//*[@id=%s]'%id).extract()
                text = ' '.join(text)
                return text
            else:
                return None

    def downloadFile(self,url,filename):
        r = requests.get(url)
        with open(LOCATION+filename,'wb') as f:
            f.write(r.content)

    def dealWithText(self,textXpath,prefix_url = ''):
        urls = textXpath.xpath('.//a')
        dict_file = {}
        if urls:
            for url in urls:
                url =  url.xpath('./@href').extract_first()
                if url.endswith('jpg') or url.endswith('JPG') or url.endswith('png') or url.endswith('PNG'):
                    imgName = url[(url.rindex('/')+1):]
                    if not imgName:
                        imgName = url
                    dict_file[url] = LOCATION+imgName
                    if not url.startswith('http'):
                        url = prefix_url+url
                    self.downloadFile(url,imgName)
                if url.endswith('doc') or url.endswith('zip') or url.endswith('docx') or url.endswith('pdf') or \
                    url.endswith('xls') or url.endswith('csv') or url.endswith('xlsx') or url.endswith('rar'):
                    fileName = url[(url.rindex('/')+1):]
                    if not fileName:
                        fileName = url
                    dict_file[url] = LOCATION+fileName
                    if not url.startswith('http'):
                        url = prefix_url+url
                    self.downloadFile(url,fileName)
        return  dict_file

    def textReedit(self,text,dict_file):
        text_ = text
        for k in dict_file.keys():
            text_ = re.sub(k,dict_file.get(k),text)
            text = text_
        return text_










