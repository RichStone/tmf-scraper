# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
import scrapy


# TODO: add logger


class ThreadsSpider(SitemapSpider):
    name = 'ThreadsSpider'
    sitemap_urls = ['https://www.thefastlaneforum.com/community/sitemap-2.xml']
    sitemap_rules = [
        ('/community/threads/', 'parse_thread'),
    ]
    count = 0

    def parse_thread(self, response):
        self.count += 1
        print(self.count)

        next_page = response.xpath('//a[./text()="Next >"]')
        if next_page:
            print("next_page")
            print(next_page)
            next_page = response.urljoin(next_page.attrib['href'])
            print("url joined")
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse_thread)
