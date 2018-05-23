__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests

class FiftyThreeSpider(scrapy.Spider):
    name = 'fiftythree'

    def start_requests(self):
        urls = ['http://www.scs.gov.cn/zcfg/index.html','http://www.scs.gov.cn/zcfg/index_1.html']

        for url in urls:
            # print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     urls = ['http://www.sastind.gov.cn/n4235/n6654336/index.html']
    #
    #     for url in urls:
    #         # print('url:%s'%url)
    #         yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):
        base_url = response.meta['url']
        print('u:%s'%base_url)
        # base_url = base_url[:base_url.rindex('/')]
        # print('base:%s'%base_url)
        prefix_url = 'http://www.scs.gov.cn/zcfg'
        listTxts = response.xpath('//*[@class="gjgwy_main_er_main"]/ul//li')
        for li in listTxts:
            href = li.xpath('./a/@href').extract_first()
            href = prefix_url + href[1:]
            print('href:%s'%href)
            yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})



    def parse(self, response):
        # prefix_url = 'http://www.sastind.gov.cn/'
        title = response.xpath('//h1/text()').extract_first()

        publishDate = response.xpath('//h5/a/text()').extract_first()
        print('publishDate:%s'%publishDate)
        text = response.xpath('//p[@class="MsoNormal"]').extract()

        if not text:
            text = response.xpath('//p[@class="p0"]').extract()
        text = ' '.join(text)
        print('text:%s'%text)

        item_fiftythree = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,'')
        yield item_fiftythree
        # publishDate = response.xpath('//*[@id="con_time"]/text()').extract_first()
        # publishDate = publishDate.strip().split('：')[1]
        # publishDate = publishDate[:11]
        # text = response.xpath('//*[@id="con_con"]/p').extract()
        # text = ' '.join(text)
        # file = []
        # file_ = response.xpath('//*[@id="con_con"]//p')
        # attachment = file_.xpath('.//a')
        # for a_ in attachment:
        #     name = a_.xpath('./text()').extract_first()
        #     url = a_.xpath('./@href').extract_first()
        #     url = prefix_url + url[6:]
        #     print('name:%s;url:%s'%(name,url))
        #     if not url.endswith('html'):
        #         r = requests.get(url)
        #         with open('/Users/tian/zaqizaba/'+name,'wb') as f:
        #             f.write(r.content)
        #             file.append('/Users/tian/zaqizaba/'+name)
        # file = ';'.join(file)
        # print('file:%s'%file)
        # item_fiftyone = four.items.fillinData(title,'','','','','','','','','','','','',text,file,publishDate,'')
        # yield item_fiftyone








