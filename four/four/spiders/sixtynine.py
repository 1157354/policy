__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings
from four.settings import LOCATION

class SixtynineSpider(scrapy.Spider):
    name = 'sixtynine'

    def start_requests(self):
        urls = ['http://www.chinavolunteer.cn/cate/zyzg_zcwj/?p=1']
        for url in urls:
            print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url)

    # def start_requests(self):
    #     urls = ['http://www.sastind.gov.cn/n4235/n6654336/index.html']
    #
    #     for url in urls:
    #         # print('url:%s'%url)
    #         yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):
        # prefix_url = 'http://dmpc.mca.gov.cn'
        listTxts = response.xpath('//*[@class="tcon"]/ul//li')
        for li in listTxts:
            href = li.xpath('./a/@href').extract_first()
            # href = prefix_url + href
            print('href:%s'%href)
            yield scrapy.Request(url=href, callback=self.parse)



    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        merge = response.xpath('//*[@class="datef"]/text()').extract_first()
        merge = merge.split(' ')
        publishDate = merge[0].strip().split('：')[1]
        source = merge[1].strip().split('：')[1]
        text = response.xpath('//*[@class="content"]/p').extract()
        text = ' '.join(text)
        print(text)
        item_sixtynine = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,source)
        yield item_sixtynine

        # download_url = 'http://dmpc.mca.gov.cn'
        # title = response.xpath('//*[@class="c_title"]/text()').extract_first()
        # merge = response.xpath('//*[@class="c_head"]/p/text()').extract_first()
        # merge = merge.split(' ')[1].strip()
        # merge = merge.split('\u3000')
        # source = merge[0]
        # print('source:%s'%source)
        # publishDate = merge[1].split('：')[1]
        # print('publishDate:%s'%publishDate)
        # text = response.xpath('//*[@class="c_content"]/p').extract()
        # text = ' '.join(text)
        # print('text:%s'%text)
        # file = []
        # ps = response.xpath('//*[@class="c_content"]//p')
        # for p_ in ps:
        #     if p_.xpath('.//a'):
        #         if p_.xpath('.//a/@href'):
        #             link = p_.xpath('.//a/@href').extract_first()
        #             if not link.endswith('htm') and not link.endswith('cn'):
        #                 if not link.startswith('http'):
        #                     link = download_url+link
        #                 r = requests.get(link)
        #                 filename = p_.xpath('.//a/text()').extract_first()
        #                 if not filename:
        #                     filename = p_.xpath('.//a/span/text()').extract_first()
        #                 print('filename:%s'%filename)
        #                 with open(LOCATION+filename,'wb') as f:
        #                     f.write(r.content)
        #                 file.append(filename)
        # file = ';'.join(file)
        # item_sixtyeight = four.items.fillinData(title,'','','','','','','','','','','','',text,file,publishDate,source)
        # yield item_sixtyeight












