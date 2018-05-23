__author__ = 'tian'
import scrapy
import re
import four.items
#==========省略了http://www.most.gov.cn/mostinfo/xinxifenlei/fgzc/gfxwj/gfxwj2017/201706/t20170627_133757.htm=================#
class EightSpider(scrapy.Spider):
    name = 'eight'
    def start_requests(self):
        urls = ['http://www.most.gov.cn/kjzc/gjkjzc/gjkjzczh/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        base_url = 'http://www.most.gov.cn/kjzc/gjkjzc/gjkjzczh/'
        listTxts = response.xpath('//*[@class="list"]/ul//li')
        for li in listTxts:
            href = li.xpath('./a/@href').extract_first()
            if not href.startswith('..'):
                href = base_url + href[1:]
            else:
                href = base_url + href

            if href.endswith('htm'):
                print('href=%s' % href)
                yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})

    def parse(self, response):
        diff = response.xpath('//*[@class="style14"]')
        if diff:
            title = response.xpath('//*[@class="style14"]/text()').extract_first()
            print('title:%s'%title)
            publishDate = response.xpath('//*[@class="gray12 lh22"]/text()').extract_first()
            publishDate = re.findall('\d+',publishDate)
            publishDate = '-'.join(publishDate)
            print(publishDate)
            source = '科技部'
            text = response.xpath('//*[@class="Custom_UnionStyle"]/p').extract()
            text = ' '.join(text)
            if not text:
                text = response.xpath('//*[@class="trshui13 lh22"]/p').extract()
                text = ' '.join(text)
            print('text:%s'%text)
            item_eight = four.items.fillinData(title,'','',None,'','','','','','','','','',text,'',publishDate,source,response.meta['url'])
            yield item_eight

