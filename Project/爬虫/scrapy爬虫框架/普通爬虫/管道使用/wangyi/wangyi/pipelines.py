# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import json
# from pymongo import MongoClient


class WangyiPipeline(object):

    def open_spider(self, spider):
        if spider.name == 'job':
            self.file = open('wangyi.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == 'job':
            # 将 itme 对象强转字典, 该操作只能在scrapy中使用
            item = dict(item)
            # 将字典数据序列化
            json_data = json.dumps(item, ensure_ascii=True) + ',\n'
            # 将数据写入文件
            self.file.write(json_data)
        return item

    def close_spider(self, spider):
        if spider.name == 'job':
            self.file.close()


class WangyiSimplePipeline(object):

    def open_spider(self, spider):
        if spider.name == 'job_simple':
            self.file = open('wangyisimple.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'job_simple':
            # 将 itme 对象强转对象, 该操作只能在scrapy中使用
            item = dict(item)
            # 将字典数据序列化
            json_data = json.dumps(item, ensure_ascii=True) + ',\n'
            # 将数据写入文件
            self.file.write(json_data)
        return item

    def close_spider(self, spider):
        if spider.name == 'job_simple':
            self.file.close()

#
# class MongoPipeline(object):
#
#     def open_spider(self, spider):
#         self.client = MongoClient('127.0.0.1', 27017)
#         self.db = self.client['itcast']
#         self.col = self.db['wangyi']
#
#     def process_item(self, item, spider):
#         data = dict(item)
#         self.col.insert(data)
#
#         return item
#
#     def close_spider(self, spider):
#         self.client.close()
