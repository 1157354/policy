__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings


class SixtySpider(scrapy.Spider):
    name = 'sixty'

    def start_requests(self):
        url_prefix = 'http://www.safe.gov.cn/wps/portal/!ut/p/c5/hY7LDoIwEEU_aaZYCluspi9FG6NSNqQhBEl4uDAm_r0lbtygM8tz7syFEsKO_tm1_tFNo--hgJJVkm_43giCKVUcldJ2q7UkNqaBO1ZxkUma7DBwgajo-pBLbgmq1Z_0df73bZhLGoz4xPXZRJFJPvzX_ZnjwmQIuZyGBhyUyWKPnIHrm9bXL7gPBXbHm30DcilFmA!!/dl3/d3/L0lJSklna2shL0lCakFBTXlBQkVSQ0lBISEvWUZOQzFOS18yN3chLzdfSENEQ01LRzEwODRJQzBJSUpRRUpKSDFRTjY!/?WCM_PI=1&PC_7_HCDCMKG1084IC0IIJQEJJH1QN6000000_WCM_Page.8701320043345c578f76bf71e169ccd5='
        url_postfix = '#fenjuid='
        urls = [url_prefix+str(num)+url_postfix for num in range(1,5)]
        for url in urls:
            print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url, meta={'url': url})

    def parse_url(self, response):
        print('hello')
        url_prefix = 'http://www.safe.gov.cn'
        result = response.xpath('//*[@class="menulist"]//tr')
        for tr in result:
            href = tr.xpath('./td/a/@href').extract_first()

            if href:
                href = url_prefix + href
                print('href:%s'%href)
                yield scrapy.Request(url=href,callback=self.parse)


    def parse(self, response):
        indexNumber = response.xpath('//*[@id="syh"]/text()').extract_first()
        print('indexNumber:%s'%indexNumber)
        topicClass = response.xpath('//*[@id="lSubcat"]/text()').extract_first()
        print('topicClass:%s'%topicClass)
        title = response.xpath('//*[@class="mainContainer"]/tr[1]/td/div/strong/text()').extract_first()
        print('title:%s'%title)
        IssuedNumber = response.xpath('//*[@id="wenhaotd"]/span/text()').extract_first()
        print('IssuedNumber:%s'%IssuedNumber)
        publishDate = response.xpath(' //*[@id="headContainer"]/tbody/tr[2]/td/table/tr/td[2]/span/text()').extract_first()
        print('publishDate:%s'%publishDate)
        source = response.xpath(' //*[@id="headContainer"]/tbody/tr[2]/td/table/tr/td[1]/span/text()').extract_first()
        print('source:%s'%source)
        text = response.xpath(' //*[@id="newsContent"]/p').extract()
        if not text:
            text = response.xpath('//*[@id="newsContent"]/span/p').extract()
        if not text:
            text = response.xpath('//*[@class="MsoNormalTable/dbody/tr/td/p"]').extract()
        text = ' '.join(text)
        item_sixty = four.items.fillinData(title,'','','','','',indexNumber,topicClass,'','',IssuedNumber,'','',text,'',publishDate,source)
        yield item_sixty
        # url_prefix = 'http://www.satcm.gov.cn'
        # publishDate = response.meta['publishDate']
        # # print('pd:%s' % publishDate)
        # title = response.xpath('//title').extract_first()
        # # print('title:%s' % title)
        # text = response.xpath('//*[@class="zw"]/p').extract()
        # file = []
        # if not text:
        #     text = response.xpath('//*[@class="TRS_Editor"]/p').extract()
        # if not text:
        #     text = response.xpath('//*[@class="TRS_PreAppend"]/p').extract()
        # text = ' '.join(text)
        # print(text)
        # text_ = response.xpath('//*[@class="zw"]')
        # attachment = text_.xpath('.//a')
        # if attachment:
        #     for href in attachment:
        #         filename = href.xpath('./@title').extract_first()
        #         if not filename:
        #             filename = href.xpath('./text()').extract_first()
        #         if not filename:
        #             filename = href.xpath('./font/text()').extract_first()
        #         url = href.xpath('./@href').extract_first()
        #         if not url.startswith('http'):
        #             url = url_prefix + url
        #         if '@' not in url and 'void' not in url:
        #             r = requests.get(url)
        #             with open(four.settings.LOCATION + filename,'wb') as f:
        #                 f.write(r.content)
        #             temp = four.settings.LOCATION + filename
        #             file.append(temp)
        # if not file:
        #     file = ''
        # else:
        #     file = ';'.join(file)
        # print('file:%s'%file)
        # item_fiftynine = four.items.fillinData(title,'','','','','','','','','','','','',text,file,publishDate,'')
        # yield item_fiftynine
















        # prefix_url = 'http://www.sastind.gov.cn/'
        # title = response.xpath('//*[@class="yjzj_nr_bt"]/text()').extract_first()
        # title = title.strip()
        # # print('title:%s'%title)
        # source = response.xpath('//*[@class="yjzj_nr_top"]/p/text()').extract_first()
        # source = source.strip()
        # # print('source:%s'%source)
        # text = response.xpath('//p[@class="MsoNormal"]').extract()
        #
        # if not text:
        #     text = response.xpath('//*[@class="allcontent"]/p').extract()
        # if not text:
        #     text = response.xpath('//*[@class="TRS_Editor"]/p').extract()
        # if not text:
        #     text = response.xpath('//*[@class="allcontent"]').extract()
        # text = ' '.join(text)
        # # print('text:%s'%text)
        # item_fiftyfour = four.items.fillinData(title,'','','','','','','','','','','','',text,'','',source)
        # yield item_fiftyfour

        # item_fiftythree = four.items.fillinData(title,'','','','','','','','','','','','',text,'',publishDate,'')
        # yield item_fiftythree



        # publishDate = response.xpath('//*[@id="con_time"]/text()').extract_first()
        # publishDate = publishDate.strip().split('：')[1]
        # publishDate = publishDate[:11]
        # text = response.xpath('//*[@id="con_con"]/p').extract()
        # text = ' '.join(text)
        # file = []
        # file_ = response.xpath('//*[@id="con_con"]//p')
        # attachment = file_.xpath('.//a')
        # for a_ in attachment:
        #     name = a_.xpath('./text()').extract_first()
        #     url = a_.xpath('./@href').extract_first()
        #     url = prefix_url + url[6:]
        #     print('name:%s;url:%s'%(name,url))
        #     if not url.endswith('html'):
        #         r = requests.get(url)
        #         with open('/Users/tian/zaqizaba/'+name,'wb') as f:
        #             f.write(r.content)
        #             file.append('/Users/tian/zaqizaba/'+name)
        # file = ';'.join(file)
        # print('file:%s'%file)
        # item_fiftyone = four.items.fillinData(title,'','','','','','','','','','','','',text,file,publishDate,'')
        # yield item_fiftyone
