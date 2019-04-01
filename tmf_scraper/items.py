# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmfScraperItem(scrapy.Item):
    id = scrapy.Field()
    creation_date = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
