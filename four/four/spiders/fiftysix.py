__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings

class FiftySixSpider(scrapy.Spider):
    name = 'fiftysix'

    def start_requests(self):
        urls = ['http://www.spb.gov.cn/zc/flfgjzc_1/index.html']
        url_ = ['http://www.spb.gov.cn/zc/flfgjzc_1/index_%s.html'%num for num in range(1,6)]
        urls.extend(url_)
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
        prefix_url = 'http://www.spb.gov.cn/zc/flfgjzc_1'
        listTxts = response.xpath('//*[@class="main"]/ul//li')
        for li in listTxts:
            href = li.xpath('./a/@href').extract_first()
            href = prefix_url + href[1:]
            print('href:%s'%href)
            yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})



    def parse(self, response):
        title = response.xpath('//*[@class="title1"]/a/text()').extract_first()
        print(title)
        IssuedNumber = response.xpath('//*[@class="title2"]/a/text()').extract_first()
        publishDate = response.xpath('//*[@class="time"]/a/text()').extract_first()
        publishDate = publishDate.strip()
        text = response.xpath('//*[@class="TRS_Editor"]/p').extract()
        text = ' '.join(text)
        item_fiftysix = four.items.fillinData(title,'','','','','','','','','',IssuedNumber,'','',text,'',publishDate,'')
        yield item_fiftysix



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








