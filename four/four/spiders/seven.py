__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re

class SevenSpider(scrapy.Spider):
    name = 'seven'

    def start_requests(self):
        urls = ['http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/']
        url_ = ['http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/index_%s.html' % page for page in range(1,7)]
        urls.extend(url_)

        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        base_url = 'http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778'
        listTxts = response.xpath('//*[@class="scy_lbsj-right-nr"]/ul//li')
        for li in listTxts:
            href = li.xpath('./a/@href').extract_first()
            href = base_url + href[1:]
            print('href=%s' % href)
            yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})

    # def start_requests(self):
    #     urls = ['http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/201701/t20170118_295161.html']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title_ = response.xpath('//*[@id="content_body"]/h1/text()').extract()
        if isinstance(title_,list) and len(title_)>1:
            title = ''.join(title_)
        else:
            title = title_[0].strip()
        print('title:%s'%title)
        # IssuingOrgan = response.xpath('//*[@id="content_fwzh"]/text()').extract_first()
        # print(IssuingOrgan)
        result = re.search('var file_fwzh.*',response.text)
        IssuingOrgan = result.group().split('\'')[1]
        if not IssuingOrgan:
            IssuingOrgan = response.xpath('//*[@class="TRS_Editor"]/p[1]/span/text()').extract_first()
        print('IssuingOrgan:%s'%IssuingOrgan)
        text = response.xpath('//*[@class="TRS_Editor"]/p').extract()
        text = ' '.join(text)
        if not text:
            text = response.xpath('//*[@class="Custom_UnionStyle"]/p').extract()
            text = ' '.join(text)
        if not text:
            text = response.xpath('//*[@id="content_body_txt"]/p').extract()
            text = ' '.join(text)
        print('text:%s'%text)
        item_seven = four.items.fillinData(title,'','',None,'','','','',IssuingOrgan,'','','','',text,'','','',response.meta['url'])
        yield item_seven


