# -*- coding: utf-8 -*-
import scrapy


class CoronastatsSpider(scrapy.Spider):
    name = 'coronastats'
    allowed_domains = ['mohfw.gov.in']
    start_urls = ['http://mohfw.gov.in/']

    def parse(self, response):
        yield{
            'Active COVID 2019 cases':  response.xpath('//*[@id="state-data"]//table/tbody/tr[32]/td[2]/strong/text()').extract()[0],
            'Cured / discharged cases': response.xpath('//*[@id="site-dashboard"]//ul/li[2]/strong/text()').extract()[0],
             "Death cases": response.xpath('//*[@id="site-dashboard"]//ul/li[3]/strong/text()').extract()[0]

        }
