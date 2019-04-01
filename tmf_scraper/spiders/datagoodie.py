# -*- coding: utf-8 -*-
import scrapy


class DatagoodieSpider(scrapy.Spider):
    name = 'datagoodie'
    allowed_domains = ['datagoodie.com']
    start_urls = ['http://datagoodie.com/']

    def parse(self, response):
        pass
