# -*- coding: utf-8 -*-
import scrapy


class CoronastatsSpider(scrapy.Spider):
    name = 'coronastats'
    allowed_domains = ['mohfw.gov.in']
    start_urls = ['http://mohfw.gov.in/']

    def parse(self, response):
        active = int(response.xpath('//*[@id="site-dashboard"]//ul/li[1]/strong/text()').extract()[0])
        cured = int(response.xpath('//*[@id="site-dashboard"]//ul/li[2]/strong/text()').extract()[0])
        deaths = int(response.xpath('//*[@id="site-dashboard"]//ul/li[3]/strong/text()').extract()[0])
        mi = int(response.xpath('//*[@id="site-dashboard"]//ul/li[4]/strong/text()').extract()[0])
        yield{
            'Active COVID 2019 cases': active+cured+deaths+mi ,
            'Cured / discharged cases': cured,
             "Death cases": deaths,

        }
