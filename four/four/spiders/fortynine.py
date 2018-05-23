__author__ = 'tian'
__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests

class FortyNineSpider(scrapy.Spider):
    name = 'fortynine'

    def start_requests(self):
        urls = ['http://www.nea.gov.cn/test_101.htm']
        # urls = []
        url_ = ['http://www.nea.gov.cn/test_101_%s.htm' % page for page in range(2,11)]
        urls.extend(url_)

        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    def parse_url(self, response):
        listTxts = response.xpath('//*[@class="list"]')
        for ul in listTxts:
            for li in ul.xpath('.//li'):
                href = li.xpath('./a/@href').extract_first()
                print('href=%s' % href)
                yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})

    # def start_requests(self):
    #     urls = ['http://www.nea.gov.cn/2017-01/24/c_136009629.htm']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse,meta={'url': url})

    def parse(self, response):
        base_url = response.meta['url']
        base_url = base_url[:base_url.rindex('/')]
        # print('..%s'%base_url)
        source = ''
        title = response.xpath('//*[@class="table1"]/tbody/tr[1]/td[2]/text()').extract_first()
        indexNumber = response.xpath('//*[@class="table1"]/tbody/tr[2]/td[2]/text()').extract_first()
        IssuingOrgan = response.xpath('//*[@class="table1"]/tbody/tr[2]/td[4]/text()').extract_first()

        publishDate = response.xpath('//*[@class="table1"]/tbody/tr[3]/td[2]/text()').extract_first()
        if not title:
            title = response.xpath('//*[@class="titles"]/text()').extract_first()
            publishDate = response.xpath('//*[@class="times"]/text()').extract_first()
            publishDate = publishDate.split('：')[1].strip()
            print('pd:%s'%publishDate)
            source = response.xpath('//*[@class="author"]/text()').extract_first()
            print('source:%s'%source)
        text = response.xpath('//*[@class="font_14 line25 STYLE8"]/p').extract()
        text = ' '.join(text)
        file = []
        file_ = response.xpath('//*[@id="id_appendix"]/ul//li')
        for f_ in file_:
            name = f_.xpath('./a/text()').extract_first()
            result = f_.xpath('./a/@href').extract_first()
            result = base_url +result[1:]
            # print('result:%s'%result)
            r = requests.get(result)
            with open('/Users/tian/zaqizaba/'+name,'wb') as f:
                f.write(r.content)
                file.append('/Users/tian/zaqizaba/'+name)
        #
        file = ';'.join(file)
        item_fortynine = four.items.fillinData(title,'','','','','',indexNumber,'',IssuingOrgan,'','','','',text,file,publishDate,source)
        yield item_fortynine




