__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings

class FiftyEightSpider(scrapy.Spider):
    name = 'fiftyeight'

    def start_requests(self):
        urls = ['http://www.sach.gov.cn/module/jslib/jquery/jpage/dataproxy.jsp?startrecord=1&endrecord=45&perpage=15\
        &col=1&appid=1&webid=1&path=/&columnid=1036&sourceContentType=1&unitid=13601&webname=%E5%9B%BD%E5%AE%B6%E6%9\
        6%87%E7%89%A9%E5%B1%80&permissiontype=0',
                'http://www.sach.gov.cn/module/jslib/jquery/jpage/dataproxy.jsp?startrecord=46&endrecord=55&perpage=15\
                &col=1&appid=1&webid=1&path=/&columnid=1036&sourceContentType=1&unitid=13601&webname=%E5%9B%BD%E5%AE%B\
                6%E6%96%87%E7%89%A9%E5%B1%80&permissiontype=0']
        for url in urls:
            # print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    def parse_url(self, response):
        url_prefix = 'http://www.sach.gov.cn'
        records = response.xpath('//record')
        for record in records:
            result = record.xpath('.').extract_first()
            result = result.split()
            for r in result:
                if r.startswith('href'):
                    r = r.split('=')[1]
                    r = url_prefix+r[1:-1]
                    yield scrapy.Request(url=r,callback=self.parse)

            # href = record.xpath('//a/@href').extract_first()
            # print('href:%s'%href)
    def parse(self, response):
        title = response.xpath('//title').extract_first()
        text = response.xpath('//*[@id="zoom"]').extract()
        text = ' '.join(text)
        item_fiftyeight = four.items.fillinData(title,'','','','','','','','','','','','',text,'','','')
        yield item_fiftyeight














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








