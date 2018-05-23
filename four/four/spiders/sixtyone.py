__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings

class SixtyOneSpider(scrapy.Spider):
    name = 'sixtyone'

    def start_requests(self):
        urls = ['http://www.saac.gov.cn/xxgk/2011-12/31/content_13382.htm']
        #====================暂时做到这==========================
        for url in urls:
            print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse,meta={'url':url})


    def parse(self, response):
        url_prefix = 'http://www.saac.gov.cn/xxgk/'
        trs = response.xpath('//*[@class="MsoNormalTable"]/tbody//tr')
        for tr in trs:
            if tr.xpath('.//a'):
                title = tr.xpath('.//a/text()').extract_first()
                if not title:
                    title = tr.xpath('.//a/span/span/text()').extract_first()
                link = tr.xpath('.//a/@href').extract_first()
                print(title)

                span = tr.xpath('./td[2]/p/span')
                IssuedNumber = span.xpath('string(.)').extract_first()
                print('date:%s'%IssuedNumber)
                if not link.startswith('http'):
                    link = url_prefix + link[6:]
                print(link)
                item_sixtyone = four.items.fillinData(title,'','','','','','','','','',IssuedNumber,'','','','','',link)
                yield item_sixtyone





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








