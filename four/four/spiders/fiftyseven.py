__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings

class FiftySevenSpider(scrapy.Spider):
    name = 'fiftyseven'

    def start_requests(self):
        urls = ['http://www.nra.gov.cn/jgzf/flfg/gfxwj/index.shtml']
        url_ = ['http://www.nra.gov.cn/jgzf/flfg/gfxwj/index_%s.shtml'%num for num in range(1,36)]
        urls.extend(url_)
        for url in urls:
            print('url:%s'%url)
            yield scrapy.Request(url=url, callback=self.parse,meta={'url':url})

    def parse(self, response):
        url_prefix = 'http://www.nra.gov.cn/jgzf/flfg/gfxwj'
        table_right = response.xpath('//*[@class="mulu_right"]/table//tr')
        for tr in table_right:
            title = tr.xpath('./td[1]/a/text()').extract_first()
            if title:
                IssuedNumber = tr.xpath('./td[2]/text()').extract_first()
                publishDate = tr.xpath('./td[4]/text()').extract_first()
                href = tr.xpath('./td[1]/a/@href').extract_first()
                href = url_prefix + href[1:]
                print('href:%s'%href)
                r = requests.get(href)
                with open(four.settings.LOCATION+title,'wb') as f:
                    f.write(r.content)
                file = four.settings.LOCATION + title
                item_fiftyseven = four.items.fillinData(title,'','','','','','','','','',IssuedNumber,'','','',file,publishDate,'')
                yield item_fiftyseven
















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








