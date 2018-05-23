__author__ = 'tian'
import scrapy
from four.items import FourItem

class FiveSpider(scrapy.Spider):
    name = 'five'

    def start_requests(self):
        urls = ['http://www.mod.gov.cn/regulatory/node_47883.htm','http://www.mod.gov.cn/regulatory/node_47883_2.htm']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_url)

    def parse_url(self,response):
        base_url = 'http://www.mod.gov.cn/regulatory/'
        listTxts = response.xpath('//*[@class="list-unstyled article-list"]/li')
        for li in listTxts:
            href = li.xpath('./a/@href').extract_first()
            href = base_url + href
            print('href=%s' % href)
            yield scrapy.Request(url=href, callback=self.parse, meta={'url': href})

    def parse(self, response):
        title = response.xpath('//*[@class="article-header"]/h1/text()').extract_first()
        print('t:%s'%title)
        source = response.xpath('//*[@class="info"]/span[1]/text()').extract_first()
        print('s:%s'%source)
        publishDate = response.xpath('//*[@class="info"]/span[4]/text()').extract_first()
        publishDate = publishDate.split(' ')[0]
        print('p:%s'%publishDate)
        text = response.xpath('//*[@class="article-content p-t"]/p').extract()
        text = ' '.join(text)
        print('text:%s'%text)
        item_four = self.fillinData(title,'','',None,'','','','','','','','','',text,'',publishDate,source,response.meta['url'])
        yield item_four


    def fillinData(self, title, metaKeywords='', tagKeywords='', officialClass='', department='', province='',
                   indexNumber='', \
                   topicClass='', IssuingOrgan='', writingDate='', IssuedNumber='', releaseDate='', thematic='', \
                   text='', file='', publishDate='', source='',website=''):
        items = FourItem()
        items['indexNumber'] = indexNumber
        items['topicClass'] = topicClass
        items['IssuingOrgan'] = IssuingOrgan
        items['writingDate'] = writingDate
        items['title'] = title
        items['IssuedNumber'] = IssuedNumber
        items['releaseDate'] = releaseDate
        items['thematic'] = thematic
        items['text'] = text
        items['metaKeywords'] = metaKeywords
        items['tagKeywords'] = tagKeywords
        items['officialClass'] = officialClass
        items['department'] = department
        items['province'] = province
        items['file'] = file
        items['publishDate'] = publishDate
        items['source'] = source
        items['website'] = website
        return items
