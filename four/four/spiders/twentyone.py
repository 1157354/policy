__author__ = 'tian'
__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
#====================attachment:http://zizhan.mot.gov.cn/zfxxgk/bnssj/dlyss/201804/t20180416_3010353.html==========================
class SevenSpider(scrapy.Spider):
    name = 'twentyone'

    def start_requests(self):
        post_url = '&indexPa=2&schn=252&curpos=%E4%B8%BB%E9%A2%98%E5%88%86%E7%B1%BB&sinfo=252&surl=zfxxgk'
        urls = ['http://was.mot.gov.cn:8080/govsearch/searPage.jsp?page=%s'%num + post_url for num in range(1,344)]
        # urls = ['http://was.mot.gov.cn:8080/govsearch/searPage.jsp?page=2&indexPa=2&schn=252&curpos=%E4%B8%BB%E9%A2%98%E5%88%86%E7%B1%BB&sinfo=252&surl=zfxxgk']

        for url in urls:
            print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        listTxts = response.xpath('//table//tr')
        for li in listTxts:
            # print('href:%s'%li.xpath('./td[2]/a/@href').extract_first())
            if li.xpath('./td[2]/a/@href').extract_first():
                print('href:%s'%li.xpath('./td[2]/a/@href').extract_first())
                yield scrapy.Request(url=li.xpath('./td[2]/a/@href').extract_first(),callback=self.parse)




    def parse(self, response):
        pass
        # title_ = response.xpath('//*[@id="content_body"]/h1/text()').extract()
        # if isinstance(title_,list) and len(title_)>1:
        #     title = ''.join(title_)
        # else:
        #     title = title_[0].strip()
        # print('title:%s'%title)
        # # IssuingOrgan = response.xpath('//*[@id="content_fwzh"]/text()').extract_first()
        # # print(IssuingOrgan)
        # result = re.search('var file_fwzh.*',response.text)
        # IssuingOrgan = result.group().split('\'')[1]
        # if not IssuingOrgan:
        #     IssuingOrgan = response.xpath('//*[@class="TRS_Editor"]/p[1]/span/text()').extract_first()
        # print('IssuingOrgan:%s'%IssuingOrgan)
        # text = response.xpath('//*[@class="TRS_Editor"]/p').extract()
        # text = ' '.join(text)
        # if not text:
        #     text = response.xpath('//*[@class="Custom_UnionStyle"]/p').extract()
        #     text = ' '.join(text)
        # if not text:
        #     text = response.xpath('//*[@id="content_body_txt"]/p').extract()
        #     text = ' '.join(text)
        # print('text:%s'%text)
        # item_seven = four.items.fillinData(title,'','','','','','','',IssuingOrgan,'','','','',text,'','','')
        # yield item_seven


