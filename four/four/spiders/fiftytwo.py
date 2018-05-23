__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests

class FiftyTwoSpider(scrapy.Spider):
    name = 'fiftytwo'

    def start_requests(self):
        urls = ['http://www.soa.gov.cn/zwgk/fwjgwywj/gwyfgwj/index.html','http://www.soa.gov.cn/zwgk/fwjgwywj/gwyfgwj/index_1.html']

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
        prefix_url = 'http://www.soa.gov.cn/zwgk/fwjgwywj/gwyfgwj'
        listTxts = response.xpath('//*[@class="ul_liebiao1"]//li')
        for li in listTxts:
            href = li.xpath('./a/@href').extract_first()
            href = prefix_url + href[1:]
            print('href:%s'%href)
            yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})



    def parse(self, response):
        prefix_url = 'http://www.sastind.gov.cn/'
        title = response.xpath('//title/text()').extract_first()
        IssuedNumber = response.xpath('//*[@class="z-h2"]/text()').extract_first()
        merge = response.xpath('//*[@class="subhead"]/text()').extract_first()
        merge = merge.strip().split(' ')
        source = merge[0]
        publishDate = merge[-1]
        publishDate = publishDate.split('：')[1]
        print('source:%s'%source)
        print('publishDate:%s'%publishDate)
        text = response.xpath('//*[@class="TRS_Editor"]/p').extract()
        text = ' '.join(text)
        print(text)
        item_fiftytwo = four.items.fillinData(title,'','','','','','','','','',IssuedNumber,'','',text,'',publishDate,source)
        yield item_fiftytwo

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








