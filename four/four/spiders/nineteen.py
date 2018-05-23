__author__ = 'tian'

import scrapy
import four.items

class NineteenSpider(scrapy.Spider):
    name = 'nineteen'

    def start_requests(self):
        urls = ['http://www.moa.gov.cn/gk/zcfg/qnhnzc/index.htm','http://www.moa.gov.cn/gk/zcfg/qnhnzc/index_1.htm',\
                'http://www.moa.gov.cn/gk/zcfg/qnhnzc/index_2.htm']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_url)

    def parse_url(self,response):
        base_url = 'http://www.moa.gov.cn/gk/zcfg/qnhnzc'
        # http://www.moa.gov.cn/gk/zcfg/qnhnzc/201804/t20180412_6140127.htm
        roots = response.xpath('//*[@class="li_1 li_1_sty1 li_1_elp adc ahc zwdt_list mg_b_30"]//li')
        for root in roots:
            href = root.xpath('./a/@href').extract_first()
            href = base_url + href[1:]
            print('href:%s'%href)
            yield scrapy.Request(url=href,callback=self.parse)




    def parse(self, response):
        pass


    def timeReformat(self, str):
        """

        :param str:
        :return:
        """
        str = str.replace('年', '-')
        str = str.replace('月', '-')
        str = str.replace('日', '')
        return str



