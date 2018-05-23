__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items

class FourSpider(scrapy.Spider):
    name = 'four'

    def start_requests(self):
        urls = ['http://www.mfa.gov.cn/web/ziliao_674904/tytj_674911/zcwj_674915/default.shtml']
        url_ = ['http://www.mfa.gov.cn/web/ziliao_674904/tytj_674911/zcwj_674915/default_%s.shtml' % page for page in range(1,13)]
        urls.extend(url_)

        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self,response):
        base_url = 'http://www.mfa.gov.cn/web/ziliao_674904/tytj_674911/zcwj_674915'
        listTxts = response.xpath('//*[@class="rebox_news"]/ul//li')
        for li in listTxts:
            href = li.xpath('./a/@href').extract_first()
            href = base_url + href[1:]
            print('href=%s' % href)
            if href.endswith('shtml'):
                yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})


    def parse(self, response):
        title = response.xpath('//*[@class="title"]/text()').extract_first()
        print('title:%s'%title)
        publishDate = response.xpath('//*[@id="News_Body_Time"]/text()').extract_first()
        print('publishDate:%s'%publishDate)
        text = response.xpath('//*[@id="News_Body_Txt_A"]/p').extract()
        if not text:
            text = response.xpath('//*[@class="content"]').extract()
        print('text:%s'%text)
        text = ' '.join(text)


        item_four = four.items.fillinData(title,'','',None,'','','','','','','','','',text,'',publishDate,'',response.meta['url'])
        yield item_four

