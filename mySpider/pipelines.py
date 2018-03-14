# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json

class ItcastPipeline(object):

    #可选方法，初始化

    def __init__(self):

        #初始化一个文件
        self.filename = open('teacher.json',"w")


    #处理数据，必须写的

    def process_item(self, item, spider):

        #ensure_ascii=False 保证中文输出，使用unicode 编码
        jsontext = json.dumps(dict(item),ensure_ascii=False) + "\n"

        self.filename.write(jsontext)

        #return item

    #可选的，结束时执行
    def close_spider(self,spider):

        self.filename.close()
