__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings

class SixtytwoSpider(scrapy.Spider):
    name = 'sixtytwo'

    def start_requests(self):
        url_pre = 'http://www.chinanpo.gov.cn/pageindex.html?dictionid=2351&netid=2&issuedeptid=100&netTypeId=1&websitId=100&page_flag=true&pagesize_key=list&goto_page=next&current_page='
        url_post = '&total_count=1340'
        urls = [url_pre+str(num)+url_post for num in range(67)]
        # urls = [url_pre+str(num)+url_post for num in range(1)]

        #====================暂时做到这==========================
        for url in urls:
            print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     urls = ['http://www.sastind.gov.cn/n4235/n6654336/index.html']
    #
    #     for url in urls:
    #         # print('url:%s'%url)
    #         yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):
        prefix_url = 'http://www.chinanpo.gov.cn'
        lis = response.xpath('//*[@class="bscx-li-5"]')
        for li in lis:
            href = li.xpath('./a/@href').extract_first()
            href = prefix_url + href
            print('href:%s'%href)
            title = li.xpath('./a/text()').extract_first()
            yield scrapy.Request(url=href, callback=self.parse, meta={'title':title})



    def parse(self, response):
        publishDate = response.xpath('//*[@class="word-7 bscx-li-4"]/strong/text()').extract_first()
        publishDate = publishDate.split('：')[1]
        print(publishDate)
        title = response.meta['title']
        text = response.xpath('//*[@id="fontinfo"]/p').extract()
        text = ' '.join(text)
        item_sixtytwo = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,'')
        yield item_sixtytwo









