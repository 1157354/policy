__author__ = 'tian'
import scrapy
import four.items

class ThirteenSpider(scrapy.Spider):
    name = 'thirteen'

    def start_requests(self):
        urls = ['http://www.moj.gov.cn/government_public/node_fggz.html']
        url_ = ['http://www.moj.gov.cn/government_public/node_fggz_%s.html'%num for num in range(2,21)]
        urls.extend(url_)
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_url)

    def parse_url(self,response):
        base_url = 'http://www.moj.gov.cn'
        listTxts = response.xpath('//*[@class="font_black_16"]//li')
        for li in listTxts:
            href = li.xpath('./dt/a/@href').extract_first()
            href = base_url + href
            yield scrapy.Request(url=href,callback=self.parse,meta={'url': href})

    def parse(self, response):
        title = response.xpath('//*[@class="con_bt"]/text()').extract_first()
        publishDate = response.xpath('//*[@class="con_time"]/span[1]/text()').extract_first().split(' ')[0]
        source = response.xpath('//*[@class="con_time"]/span[2]/text()').extract_first()
        text = response.xpath('//*[@id="content"]/span/p').extract()
        text = ' '.join(text)
        print('title:%s'%title)
        print('publishDate:%s'%publishDate)
        print('source:%s'%source)
        print('text:%s'%text)
        item_thirteen = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,source,response.meta['url'])
        yield item_thirteen



