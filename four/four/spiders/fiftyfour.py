__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests

class FiftyFourSpider(scrapy.Spider):
    name = 'fiftyfour'

    def start_requests(self):
        urls = ['http://www.sbsm.gov.cn/zwgk/zcfgjjd/gfxwj/index_%s.shtml'%num for num in range(1,15)]
        urls.append('http://www.sbsm.gov.cn/zwgk/zcfgjjd/gfxwj/index.shtml')

        for url in urls:
            # print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})

    # def start_requests(self):
    #     urls = ['http://www.sastind.gov.cn/n4235/n6654336/index.html']
    #
    #     for url in urls:
    #         # print('url:%s'%url)
    #         yield scrapy.Request(url=url, callback=self.parse_url,meta={'url':url})


    def parse_url(self, response):
        prefix_url = 'http://www.sbsm.gov.cn/zwgk/zcfgjjd/gfxwj'
        listTxts = response.xpath('//*[@class="rd-nr no_04"]//div')
        for li in listTxts:
            href = li.xpath('./span[2]/a/@href').extract_first()
            href = prefix_url + href[1:]
            print('href:%s'%href)
            if href.endswith('shtml'):
                yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})



    def parse(self, response):
        # prefix_url = 'http://www.sastind.gov.cn/'
        title = response.xpath('//*[@class="yjzj_nr_bt"]/text()').extract_first()
        title = title.strip()
        # print('title:%s'%title)
        source = response.xpath('//*[@class="yjzj_nr_top"]/p/text()').extract_first()
        source = source.strip()
        # print('source:%s'%source)
        text = response.xpath('//p[@class="MsoNormal"]').extract()

        if not text:
            text = response.xpath('//*[@class="allcontent"]/p').extract()
        if not text:
            text = response.xpath('//*[@class="TRS_Editor"]/p').extract()
        if not text:
            text = response.xpath('//*[@class="allcontent"]').extract()
        text = ' '.join(text)
        # print('text:%s'%text)
        item_fiftyfour = four.items.fillinData(title,'','','','','','','','','','','','',text,'','',source)
        yield item_fiftyfour

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








