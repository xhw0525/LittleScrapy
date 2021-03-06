# -*- coding: utf-8 -*-
import os
import scrapy

# scrapy下载图片专用管道
from scrapy.pipelines.images import ImagesPipeline
# 在setting中指定图片存储路径
import LittleScrapy.settings as Settings

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
        return cls()

class ImageSourcePipeline(object):

    # 添加数据源
    def process_item(self, item, spider):
        item['source'] = spider.name
        return item


class DouyuImagePipeline(ImagesPipeline):

    # 发送图片链接请求
    def get_media_requests(self, item, info):
        # 获取item数据的图片链接
        image_link = item['image_link']

        # 发送图片请求，响应会保存在settings中指定的路径下(IMAGES_STORE)
        try:
            yield scrapy.Request(url=image_link)
        except:
            print(image_link)

    def item_completed(self, results, item, info):
        """
        :param results: 下载图片结果,包含一个二元组（下载状态，图片路径）
        :param item:
        :param info:
        :return:
        """
        # 取出每个图片的原本路径
        # path为设定的图片存储路径
        [x['path'] for ok, x in results if ok]
        for ok, x in results:
            if ok and len(item['nick_name']) and os.path.exists(os.path.join(Settings.IMAGES_STORE, x['path'])):
                # 默认保存当前图片的路径
                old_name = os.path.join(Settings.IMAGES_STORE, x['path'])
                # 新建当前图片路径,因为默认路径有一些不需要的东西
                new_name = os.path.join(Settings.IMAGES_STORE, item['nick_name'] + '.jpg')
                try:
                    # 将原本路径的图片名，修改为新建的图片名
                    os.rename(old_name, new_name)
                    item['image_path'] = new_name
                except:
                    print item
                    print("INFO:图片更名错误！")
            else:
                if os.path.exists(os.path.join(Settings.IMAGES_STORE, item['nick_name'] + '.jpg')):
                    item['image_path'] = os.path.join(Settings.IMAGES_STORE, item['nick_name'] + '.jpg')
                    print '已存在:', item['image_path']
                else:
                    print '下载失败:', item['nick_name'], item['image_link']
        return item