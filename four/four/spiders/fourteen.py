__author__ = 'tian'
__author__ = 'tian'
import scrapy
import four.items

class FourteenSpider(scrapy.Spider):
    name = 'fourteen'

    def start_requests(self):
        urls = ['http://www.mof.gov.cn/zhengwuxinxi/zhengcefabu/index.htm']
        url_ = ['http://www.mof.gov.cn/zhengwuxinxi/zhengcefabu/index_%s.htm'%num for num in range(1,23)]
        urls.extend(url_)
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_url)

    def parse_url(self,response):
        listTxts = response.xpath('//*[@id="id_bl"]/tbody//tr')
        for li in listTxts:
            href = li.xpath('./td/a/@href').extract_first()
            print('href:%s'%href)
            yield scrapy.Request(url=href,callback=self.parse)

    def parse(self, response):
        pass



