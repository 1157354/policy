__author__ = 'tian'
import scrapy
import four.items
import re

class Eleven(scrapy.Spider):
    name = 'eleven'

    def start_requests(self):
        urls = ['http://www.mps.gov.cn/n2254314/n2254409/n4904353/index.html']
        url1 = ['http://www.mps.gov.cn/n2254314/n2254409/n4904353/index_4939820_%s.html'%num for num in range(1,11)]
        urls.extend(url1)

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_url,meta={'url':url})

    def parse_url(self,response):
        prex_url = 'http://www.mps.gov.cn/'
        if response.meta['url'].endswith('index.html'):
            urls_ = response.xpath('//*[@id="comp_4939820"]/dl//dd')
            for url_ in urls_:
                result = url_.xpath('./a/@href').extract_first()
                result = prex_url + result[9:]
                yield scrapy.Request(url=result,callback=self.parse,meta={'url':result})
        else:
            urls_ = response.xpath('/html/body/dl//dd')
            for url_ in urls_:
                result = url_.xpath('./a/@href').extract_first()
                result = prex_url +result[9:]
                yield scrapy.Request(url=result,callback=self.parse,meta={'url':result})

    # def start_requests(self):
    #     url = 'http://www.mps.gov.cn/n2254314/n2254409/n4904353/c5519508/content.html'
    #     yield scrapy.Request(url=url,callback=self.parse,meta={'url':url})

    def parse(self, response):
        # print(response.text)
        if re.findall('window.location',response.text):
            print('it is relocated:%s'%response.meta['url'])
        else:
            title = response.xpath('//h1/text()').extract_first()
            mix = response.xpath('//*[@class="arcTool relative"]/text()').extract_first()
            mix = mix.strip().split('    ')
            print('mix:%s'%mix)
            if len(mix) == 1:
                publishDate = re.findall('/d+',mix[0])
                print('1:%s'%publishDate)
            else:
                source = mix[0]
                publishDate = re.findall('/d+',mix[1])
                print('2:%s,%s'%(source,publishDate))







