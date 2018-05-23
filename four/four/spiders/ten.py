__author__ = 'tian'
import scrapy
import four.items


class TenSpider(scrapy.Spider):
    name = 'ten'

    def start_requests(self):
        url_1 = 'http://www.seac.gov.cn/module/jslib/jquery/jpage/dataproxy.jsp?startrecord='
        url_2 = '&endrecord='
        url_3 = '&perpage=20&appid=1&webid=1&path=/&columnid=142&sourceContentType=1&unitid=2258&webname=%E5%9B%BD%E5%AE%B\
        6%E6%B0%91%E5%A7%94%E9%97%A8%E6%88%B7%E7%BD%91%E7%AB%99&permissiontype=0'

        urls = [url_1 + str(20 * n + 1) + url_2 + str(20 * n + 20) + url_3 for n in range(16)]

        for url in urls:
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        base_url = 'http://www.seac.gov.cn'
        hrefs = response.xpath('//a')
        for href in hrefs:
            result = href.xpath('./@href').extract_first()
            result = result.split('\'')[1]
            result = base_url+result[:-1]
            yield scrapy.Request(url=result,callback=self.parse,meta={'url': result})

    # def start_requests(self):
    #     url = 'http://www.seac.gov.cn/art/2016/2/2/art_142_247796.html'
    #     yield  scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        title = response.xpath('//*[@name="title"]/@content').extract_first()
        publishDate = response.xpath('//*[@name="pubDate"]/@content').extract_first()
        publishDate = publishDate.split(' ')[0]
        source = response.xpath('//*[@name="source"]/@content').extract_first()
        text = response.xpath('//*[@id="zoom"]/div/p').extract()
        text = ' '.join(text)
        if not text:
            text = response.xpath('//*[@id="zoom"]/p').extract()
            text = ' '.join(text)

        item_ten = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,source,response.meta['url'])
        yield item_ten
