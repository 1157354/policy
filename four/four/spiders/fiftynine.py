__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings


class FiftyNineSpider(scrapy.Spider):
    name = 'fiftynine'

    def start_requests(self):
        urls = ['http://ghs.satcm.gov.cn/zhengcewenjian/']
        for url in urls:
            # print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url, meta={'url': url})

    def parse_url(self, response):
        url_prefix = 'http://www.satcm.gov.cn'
        result = response.xpath('//ul[@class="lbbt"]')
        for r in result:
            lis = r.xpath('.//li')
            for li in lis:
                href = li.xpath('./a/@href').extract_first()
                if not href.startswith('http'):
                    href = url_prefix + href
                publishDate = li.xpath('./span/text()').extract_first()
                yield scrapy.Request(url=href, callback=self.parse, meta={'publishDate': publishDate})

                # href = record.xpath('//a/@href').extract_first()
                # print('href:%s'%href)
    # def start_requests(self):
    #     urls = ['http://www.satcm.gov.cn/guohesi/zhengcewenjian/2018-03-24/3957.html']
    #     for url in urls:
    #         # print('url:%s'%url)
    #         yield scrapy.Request(url=url, callback=self.parse, meta={'url': url,'publishDate': '2013-05-28'})

    def parse(self, response):
        url_prefix = 'http://www.satcm.gov.cn'
        publishDate = response.meta['publishDate']
        # print('pd:%s' % publishDate)
        title = response.xpath('//title').extract_first()
        # print('title:%s' % title)
        text = response.xpath('//*[@class="zw"]/p').extract()
        file = []
        if not text:
            text = response.xpath('//*[@class="TRS_Editor"]/p').extract()
        if not text:
            text = response.xpath('//*[@class="TRS_PreAppend"]/p').extract()
        text = ' '.join(text)
        print(text)
        text_ = response.xpath('//*[@class="zw"]')
        attachment = text_.xpath('.//a')
        if attachment:
            for href in attachment:
                filename = href.xpath('./@title').extract_first()
                if not filename:
                    filename = href.xpath('./text()').extract_first()
                if not filename:
                    filename = href.xpath('./font/text()').extract_first()
                url = href.xpath('./@href').extract_first()
                if not url.startswith('http'):
                    url = url_prefix + url
                if '@' not in url and 'void' not in url:
                    r = requests.get(url)
                    with open(four.settings.LOCATION + filename,'wb') as f:
                        f.write(r.content)
                    temp = four.settings.LOCATION + filename
                    file.append(temp)
        if not file:
            file = ''
        else:
            file = ';'.join(file)
        print('file:%s'%file)
        item_fiftynine = four.items.fillinData(title,'','','','','','','','','','','','',text,file,publishDate,'')
        yield item_fiftynine
















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
