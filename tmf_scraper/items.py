# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Post(scrapy.Item):
    id = scrapy.Field(serializer=int)
    author = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()
    creation_date = scrapy.Field()
