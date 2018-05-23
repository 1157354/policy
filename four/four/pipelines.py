# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from four.settings import MYSQL_HOST
from four.settings import MYSQL_DATABASE
from four.settings import MYSQL_USERNAME
from four.settings import MYSQL_PASSWORD
from four.settings import MYSQL_PORT




class FourPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host=MYSQL_HOST, db=MYSQL_DATABASE, user=MYSQL_USERNAME, passwd=MYSQL_PASSWORD,port=MYSQL_PORT,
                                       charset="utf8",autocommit=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        pass
        try:
            print('begin to process items')
            # item['text'] = 'aaa'
            sql = """insert into policy_new(title,metaKeywords,tagKeywords,officialClass,department,province,indexNumber,topicClass,IssuingOrgan,\
                writingDate,IssuedNumber,releaseDate,thematic,text,file,publishDate,source,website) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            self.cursor.execute(sql, (item['title'], item['metaKeywords'], item['tagKeywords'], item['officialClass'],
                                      item['department'], \
                                      item['province'], item['indexNumber'], item['topicClass'], item['IssuingOrgan'],\
                                      item['writingDate'] if item['writingDate'] else None, \
                                      item['IssuedNumber'], item['releaseDate'] if item['releaseDate'] else None, item['thematic'], item['text'],
                                      item['file'], item['publishDate'] if item['publishDate'] else None, \
                                      item['source'],item['website'])

                                )
        except Exception as error:
            print('sql error....................................................................')
            print(error)
        return item