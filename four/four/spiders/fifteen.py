__author__ = 'tian'
#=============附件http://www.mohurd.gov.cn/wjfb/201804/t20180403_235608.html=============
import scrapy
import four.items

class FifteenSpider(scrapy.Spider):
    name = 'fifteen'

    def start_requests(self):
        urls = ['http://www.mohurd.gov.cn/wjfb/index.html']
        url_ = ['http://www.mohurd.gov.cn/wjfb/index_%s.html'%num for num in range(2,51)]
        urls.extend(url_)
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_url)

    def parse_url(self,response):
        listTxts = response.xpath('//*[@style=" padding-bottom:5px; background:#FAFBFD; padding-left:25px; line-height:25px;"]/tbody//tr')
        for li in listTxts:
            href = li.xpath('./td[2]/a/@href').extract_first()
            print('href:%s'%href)
            yield scrapy.Request(url=href,callback=self.parse)

    def parse(self, response):
        title = response.xpath('//*[]')

