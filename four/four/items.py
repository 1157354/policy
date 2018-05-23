# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FourItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    metaKeywords = scrapy.Field()
    tagKeywords = scrapy.Field()
    officialClass = scrapy.Field()
    department = scrapy.Field()
    province = scrapy.Field()
    indexNumber = scrapy.Field()
    topicClass = scrapy.Field()
    IssuingOrgan = scrapy.Field()
    writingDate = scrapy.Field()
    IssuedNumber = scrapy.Field()
    releaseDate = scrapy.Field()
    thematic = scrapy.Field()
    text = scrapy.Field()
    file = scrapy.Field()
    publishDate = scrapy.Field()
    source = scrapy.Field()
    website = scrapy.Field()

def fillinData(title, metaKeywords='', tagKeywords='', officialClass='', department='', province='',
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
