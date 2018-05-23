__author__ = 'tian'
__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings

class SixtyFiveSpider(scrapy.Spider):
    name = 'sixtyfive'

    def start_requests(self):
        urls = ['http://sy.mca.gov.cn/article/fgzc/?','http://sy.mca.gov.cn/article/fgzc/?2']
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
        prefix_url = 'http://sy.mca.gov.cn'
        listTxts = response.xpath('//*[@class="article"]//tr')
        for li in listTxts:
            if li.xpath('./td[2]/a/@href'):
                href = li.xpath('./td[2]/a/@href').extract_first()
                href = prefix_url + href
                print('href:%s'%href)
                yield scrapy.Request(url=href, callback=self.parse)



    def parse(self, response):
        title = response.xpath('//h3/text()').extract_first()
        result = re.findall("var tm = .*",response.text)[0]
        result = result.split('\'')[1].split(' ')[0]
        source = re.findall("var source = .*",response.text)[0]
        source = source.split('\'')[1]
        text = response.xpath('//*[@class="content"]').extract()
        text = ' '.join(text)
        item_sixtyfive = four.items.fillinData(title,'','','','','','','','','','','','',text,'',result,source)
        yield item_sixtyfive








