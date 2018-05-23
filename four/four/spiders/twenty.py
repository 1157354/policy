__author__ = 'tian'
__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re

class TwentySpider(scrapy.Spider):
    name = 'twenty'

    def start_requests(self):
        urls = ['http://www.mwr.gov.cn/zw/zcfg/xzfghfgxwj/201707/t20170713_9557%s.html'%num for num in range(10,30)]
        urls.extend('http://www.mwr.gov.cn/zw/zcfg/xzfghfgxwj/201707/t20170713_955708.html')
        urls.extend('http://www.mwr.gov.cn/zw/zcfg/xzfghfgxwj/201707/t20170713_955709.html')
        for url in urls:
            print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        title = title.strip()
        print('title:%s'%title)
        publishDate = response.xpath('//*[@class="slywxl4"]/span[5]/text()').extract_first()
        publishDate =publishDate.strip()
        print('publishDate:%s'%publishDate)
        text = response.xpath('//*[@class="TRS_Editor"]/p').extract()
        print('text:%s'%text)
        text = ' '.join(text)
        item_twenty = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,'')
        yield item_twenty


