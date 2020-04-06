# -*- coding: utf-8 -*-
import scrapy
import time

class LiveChannelsSpider(scrapy.Spider):
    name = 'live_channels'
    allowed_domains = ['youtube.com']
    start_urls = ['https://www.youtube.com/user/ndtvindia/featured']

    def parse(self, response):
        time.sleep(1)
        print(response.xpath('//*[contains(@aria-label,"NDTV India LIVE TV")]/@href').extract())
