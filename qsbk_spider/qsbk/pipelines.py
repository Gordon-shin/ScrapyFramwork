# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from qsbk_spider.qsbk.util.commonUtil import IteratorAsList
from qsbk_spider.qsbk.items import *
from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter
# class QsbkPipeline:
#     def __init__(self):
#         self.fp = open("duanzi.json", 'w', encoding='utf-8')
#         self.json_list = []
#
#     def open_spider(self, spider):
#         pass
#
#     def process_item(self, item, spider):
#         assert isinstance(item,QsbkItem)
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         #item_json = item.toJSON()
#         self.json_list.append(item_json)
#         return item
#
#     def close_spider(self, spider):
#
#         parsed_data = self.json_list
#         #json.dump(parsed_data,self.fp,indent=4,ensure_ascii=False)
#         print(parsed_data,file=self.fp)
#         self.fp.close()
#         pass
# class QsbkPipeline:
#     def __init__(self):
#         self.fp = open("duanzi.json", 'wb')
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding = 'utf-8')
#         ''':type:'''
#         self.exporter.start_exporting()
#
#     def open_spider(self, spider):
#         pass
#
#     def process_item(self, item, spider):
#         assert isinstance(item,QsbkItem)
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         pass
class QsbkPipeline:
    def __init__(self):
        self.fp = open("duanzi.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding = 'utf-8')
        ''':type:'''

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        assert isinstance(item,QsbkItem)
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        pass
