__author__ = 'tian'
import scrapy
from four.items import FourItem
from four.textEdit import textEdit

class SixSpider(scrapy.Spider):
    name = 'six'
    def start_requests(self):
        urls = ['http://www.ndrc.gov.cn/zcfb/gfxwj/','http://www.ndrc.gov.cn/zcfb/gfxwj/index_1.html',\
                'http://www.ndrc.gov.cn/zcfb/gfxwj/index_2.html']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_url)

    def parse_url(self,response):
        base_url = 'http://www.ndrc.gov.cn/zcfb/gfxwj'
        listTxts = response.xpath('//*[@class="list_02 clearfix"]//li')
        for li in listTxts:
            if li.xpath('./a/@href'):
                href = li.xpath('./a/@href').extract_first()
                href = base_url + href[1:]
                print('href=%s'%href)
                yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})

    def parse(self, response):
        title = response.xpath('//title/text()').extract_first()
        te = textEdit()
        text,files = te.dealWithAll(response,classname="TRS_Editor")
        print('text:%s'%text)
        print('file:%s'%files)

