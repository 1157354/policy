__author__ = 'tian'
import scrapy
from four.items import FourItem
import four.items
import re
import requests
import four.settings

class FiftyFiveSpider(scrapy.Spider):
    name = 'fiftyfive'

    def start_requests(self):
        post_url = '&channelid=211383&orderby=-fabuDate%2C-DOC_ID&was_custom_expr=+PARENTID%3D%2710%27+or+CLASSINFOID%\
        3D%2710%27+&perpage=20&outlinepage=7&orderby=-fabuDate%2C-DOC_ID&selST=All&fl=10'
        urls = ['http://www.caac.gov.cn/was5/web/search?page=%s'%num + post_url for num in range(1,8)]
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
        # prefix_url = 'http://www.sbsm.gov.cn/zwgk/zcfgjjd/gfxwj'
        listTxts = response.xpath('//*[@class="t_table"]/tbody//tr')
        for li in listTxts:
            href = li.xpath('./td[2]/a/@href').extract_first()
            print('href:%s'%href)
            yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})



    def parse(self, response):
        i = response.meta['url'].rindex('/')
        url_prefix = response.meta['url'][:i]
        print('url_prefix:%s'%url_prefix)
        merge_ = response.xpath('//*[@class="content_nav"]')
        topicClass = merge_.xpath('//*[@class="content_nav_left special"]/text()').extract_first()
        print('topicClass:%s'%topicClass)
        IssuingOrgan = merge_.xpath('//*[@id="libwdw"]/text()').extract_first()
        print('IssuingOrgan:%s'%IssuingOrgan)
        publishDate = response.xpath('//*[@id="lifwrq"]/text()').extract_first()
        print('publishDate:%s'%publishDate)
        title = response.xpath('//*[@class="content_t"]/text()').extract_first()
        print('title:%s'%title)
        text = response.xpath('//*[@class="content"]/p').extract()

        if not text:
            text = response.xpath('//*[@class="Custom_UnionStyle"]').extract()
        text = ' '.join(text)
        file = ''
        if not text:
            file = response.xpath('//*[@id="id_tblAppendix"]/p/a/@href').extract_first()
            filename = response.xpath('//*[@id="id_tblAppendix"]/p/a/text()').extract_first()
            if file:

                file = url_prefix + file[1:]
                # print('file:%s'%file)
                r = requests.get(file)
                with open(four.settings.LOCATION+filename,'wb') as f:
                    f.write(r.content)
                file = four.settings.LOCATION + filename
        item_fiftyfive = four.items.fillinData(title,'','','','','','',topicClass,IssuingOrgan,'','','','',text,file,publishDate,'')
        yield item_fiftyfive


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








