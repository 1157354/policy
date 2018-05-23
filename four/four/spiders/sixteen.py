__author__ = 'tian'
import scrapy
import four.items

class SixteenSpider(scrapy.Spider):
    name = 'sixteen'

    def start_requests(self):
        urls = ['http://www.mohrss.gov.cn/gkml/index3.htm']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_url)

    def parse_url(self,response):
        base_url = 'http://www.mohrss.gov.cn/gkml'
        roots = response.xpath('//*[@id="treeContainer"]/ul//ul')
        for root in roots:
            root_ = root.xpath('.//div')
            for r in root_:
                href = r.xpath('./a/@href').extract_first()
                href = base_url + href[1:]
                yield scrapy.Request(url=href,callback=self.parse_url2)

    def parse_url2(self,response):
        base_url = 'http://www.mohrss.gov.cn/gkml'
        urls = response.xpath('//*[@id="documentContainer"]//div[@class="row"]')
        for url in urls:
            href = url.xpath('./li[2]/div/a/@href').extract_first()
            href = base_url +href[11:]
            yield scrapy.Request(url=href,callback=self.parse,meta={'url': href})
    # def start_requests(self):
    #     urls = ['http://www.mohrss.gov.cn/gkml/zcfg/gfxwj/201312/t20131218_119791.html']
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        indexNumber = response.xpath('//*[@class="govInfoMainTab"]/div[1]/div[1]/div[2]/text()').extract_first()
        officialClass = response.xpath('//*[@class="govInfoMainTab"]/div[1]/div[2]/div[2]/text()').extract_first()
        IssuingOrgan = response.xpath('//*[@class="govInfoMainTab"]/div[2]/div[1]/div[2]/text()').extract()
        IssuingOrgan = IssuingOrgan[1].strip()
        releaseDate = response.xpath('//*[@class="govInfoMainTab"]/div[2]/div[2]/div[2]/text()').extract_first()
        releaseDate = self.timeReformat(releaseDate)
        title = response.xpath('//*[@class="govInfoMainTab"]/div[3]/div[1]/div[2]/text()').extract()
        title = title[1].strip()
        IssuedNumber = response.xpath('//*[@class="govInfoMainTab"]/div[3]/div[2]/div[2]/text()').extract_first()
        text = response.xpath('//*[@class="govInfoMainTabListTxtMain"]/p').extract()
        text = ' '.join(text)

        item_sixteen = four.items.fillinData(title,'','',None,'','',indexNumber,'',IssuingOrgan,'',IssuedNumber,releaseDate,'',text,'','','',response.meta['url'])
        yield item_sixteen


    def timeReformat(self, str):
        """

        :param str:
        :return:
        """
        str = str.replace('年', '-')
        str = str.replace('月', '-')
        str = str.replace('日', '')
        return str



