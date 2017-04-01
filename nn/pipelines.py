# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, Numeric, String
class newsPipeline(object):
    def process_item(self, item, spider):
        engine = (create_engine("mysql+pymysql://root:dupengju514@192.168.202.134:3306/news?charset=utf8", max_overflow=5, encoding="utf-8", echo=True))
        connection = engine.connect()
        metadata = MetaData()
        news = Table('news',metadata,
#        Column('序号',Integer(10),autoincrement=True,primary_key=True),
        Column('标题',String(200)),
        Column('内容',String(2000)),
        Column('链接',String(100))
                 )
        metadata.create_all(engine)
        ins = news.insert()

        result = connection.execute(ins,item)
        return item

