# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LittlescrapyPipeline(object):

    def __init__(self):
        pass

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


    def process_item(self, item, spider):
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
        )