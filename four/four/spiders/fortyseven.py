__author__ = 'tian'
#===============finished==============
import scrapy
from four.items import FourItem
import four.items
import re

class FortySevenSpider(scrapy.Spider):
    name = 'fortyseven'

    def start_requests(self):
        urls = ['http://www.nsfc.gov.cn/publish/portal0/xxgk/04202/info7353%s.htm'%num for num in range(8)]

        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        publishDate = response.xpath('//*[@class="line_xilan"]/text()').extract_first()
        publishDate = publishDate.split(' ')[1]
        publishDate = publishDate.strip()
        text = response.xpath('//*[@class="normal105"]/p').extract()
        text = ' '.join(text)
        item_fortyseven = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,'')
        yield item_fortyseven
        # IssuingOrgan = response.xpath('//*[@id="content_fwzh"]/text()').extract_first()
        # print(IssuingOrgan)
        # result = re.search('var file_fwzh.*',response.text)
        # IssuingOrgan = result.group().split('\'')[1]
        # if not IssuingOrgan:
        #     IssuingOrgan = response.xpath('//*[@class="TRS_Editor"]/p[1]/span/text()').extract_first()
        # print('IssuingOrgan:%s'%IssuingOrgan)
        # text = response.xpath('//*[@class="TRS_Editor"]/p').extract()
        # text = ' '.join(text)
        # if not text:
        #     text = response.xpath('//*[@class="Custom_UnionStyle"]/p').extract()
        #     text = ' '.join(text)
        # if not text:
        #     text = response.xpath('//*[@id="content_body_txt"]/p').extract()
        #     text = ' '.join(text)
        # print('text:%s'%text)
        # item_seven = four.items.fillinData(title,'','','','','','','',IssuingOrgan,'','','','',text,'','','')
        # yield item_seven


