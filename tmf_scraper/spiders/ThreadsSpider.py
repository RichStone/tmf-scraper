# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
from scrapy.exceptions import CloseSpider
import scrapy
from tmf_scraper.items import Post


# TODO: add logger


class ThreadsSpider(SitemapSpider):
    name = 'ThreadsSpider'
    sitemap_urls = ['https://www.thefastlaneforum.com/community/sitemap-2.xml']
    sitemap_rules = [
        ('/community/threads/', 'parse_thread'),
    ]
    count = 0

    def parse_thread(self, response):
        posts = response.xpath('//li[starts-with(@class, "message ")]')
        for post in posts:
            post = Post(
                author=post.xpath('.//a[@class="username"]/text()').get(),
                # TODO: adapt to different time formats either span@title or abbr@data-time or fallback: post.xpath('.//span[@class="leftSide"]//a[@title="Permalink"]//text()').get()
                creation_date=post.xpath('.//span[@class="leftSide"]//a[@title="Permalink"]//text()').get()
            )
            yield post

        self.count += 1
        if self.count is 2:
            raise CloseSpider('enough')

        next_page = response.xpath('//a[./text()="Next >"]')
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse_thread)
