# -*- coding: utf-8 -*-
import scrapy
import logging
from bs4 import BeautifulSoup

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']


    def parse(self, response):
        soup = BeautifulSoup(response.body,'lxml')
        zzr=soup.find_all('a')
        for item in zzr:
            print item.get("href")
        # print (response.body)
        pass
