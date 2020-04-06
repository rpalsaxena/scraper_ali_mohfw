# -*- coding: utf-8 -*-
import scrapy


class MohfwSpider(scrapy.Spider):
    name = 'mohfw'
    allowed_domains = ['mohfw.gov.in']
    start_urls = ['https://www.mohfw.gov.in//']

    def parse(self, response):
        i =0 #//div[@id="cases"]//table/tbody/tr/td/text()
        for i, states in enumerate(response.xpath('//div[@id="cases"]//table/tbody/tr')):
            print(i)
            #print(states)
            #self.logger.info(states.extract())
            expath = states.xpath('td/text()')
            yield{
                'Id': expath.extract()[0],
                'State': expath.extract()[1],
                'Total Cases': (int(expath.extract()[2]) + int(expath.extract()[3]) + int(expath.extract()[4])),
                'Cured': int(expath.extract()[3]),
                'Death': int(expath.extract()[4],)
                #'': expath.extract()[5],

            }