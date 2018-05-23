__author__ = 'tian'
__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests

class FortyEightSpider(scrapy.Spider):
    name = 'fortyeight'

    def start_requests(self):
        urls = ['http://www.chinagrain.gov.cn/n316635/n746804/index.html']
        # urls = []
        url_ = ['http://www.chinagrain.gov.cn/n316635/n746804/index_318902_%s.html' % page for page in range(1,18)]
        urls.extend(url_)

        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    def parse_url(self, response):
        base_url = 'http://www.chinagrain.gov.cn/n316635/n746804/'
        listTxts = response.xpath('//*[@class="list_01"]')
        for ul in listTxts:
            for li in ul.xpath('.//li'):
                href = li.xpath('./a/@href').extract_first()
                href = base_url + href
                print('href=%s' % href)
                yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})

    # def start_requests(self):
    #     urls = ['http://www.chinagrain.gov.cn/n316635/n746804/../../n316635/n746804/c756741/content.html']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        base_url = 'http://www.chinagrain.gov.cn/'
        title = response.xpath('//title/text()').extract_first()
        publishDate = response.xpath('//*[@id="con_time"]/text()').extract_first()
        publishDate = publishDate[1:-1]
        text = response.xpath('//*[@id="con_con"]/p').extract()
        text = ' '.join(text)
        if not text:
            print('helloworld')
            text = response.xpath('//*[@id="con_con"]/text()').extract()
            text = ' '.join(text)
            print('helloworld:%s'%text)

        print('text:%s'%text)
        if not text:
            text=''
        text_ = response.xpath('//*[@id="con_con"]//p')
        file = []
        for t in text_:
            if t.xpath('.//a'):
                href = t.xpath('.//a')
                for h in href:
                    result = h.xpath('./@href').extract_first()
                    name = h.xpath('./text()').extract_first()
                    result = base_url +result[9:]

                    r = requests.get(result)
                    # print(r.text)
                    with open('/Users/tian/zaqizaba/'+name,'wb') as f:
                        f.write(r.content)
                        file.extend('/Users/tian/zaqizaba/'+name)

        file = ''.join(file)
        item_fortyeight = four.items.fillinData(title,'','','','','','','','','','','','',text,file,publishDate,'')
        yield item_fortyeight

        # item_seven = four.items.fillinData(title,'','','','','','','',IssuingOrgan,'','','','',text,'','','')
        # yield item_seven


