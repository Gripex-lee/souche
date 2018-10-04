# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from car_dataSpider.items import CarDataspiderItem
import re

class GauziSpider(scrapy.Spider):
    name = 'che'
    allowed_domains = ['taoche.com']
    start_urls = ['http://beijing.taoche.com/all/?page=1']


    def parse(self, response): 
        for content in response.xpath('//div[@id="container_base"]/ul/li[@class!="inter"]'):
            item = CarDataspiderItem()
            if content.xpath('./div[@class="gongge_main"]/a/span/text()').extract_first():
                item["title"] = content.xpath('./div[@class="gongge_main"]/a/span/text()').extract_first()
            else:
                item["title"] = "NA"
            if content.xpath('./div[@class="gongge_main"]/p/i[1]/text()').extract_first():
                item["time"] = content.xpath('./div[@class="gongge_main"]/p/i[1]/text()').extract_first()
            else:
                item["time"] = "NA"
            if content.xpath('./div[@class="gongge_main"]/p/i[2]/text()').extract_first():
                item["milestone"] = content.xpath('./div[@class="gongge_main"]/p/i[2]/text()').extract_first()
            else:
                item["milestone"] = "NA"
            if content.xpath('./div[@class="gongge_main"]/p/i[@class="city_i"]/a/text()').extract_first():
                item["gGB"] = content.xpath('./div[@class="gongge_main"]/p/i[@class="city_i"]/a/text()').extract_first()
            else:
                item["gGB"] = "NA"
            if content.xpath('./div[2]/div[1]/i[1]/text()').extract():
                item["price"] = content.xpath('./div[2]/div[1]/i[1]/text()').extract()
            else:
                item["price"] = "NA"
            if content.xpath('./div[2]/div[1]/i[2]/text()').extract():
                item["new_price"] = content.xpath('./div[2]/div[1]/i[2]/text()').extract()
            else:
                item["new_price"] = "NA"
            yield item

            for city in ['beijing','shanghai','guangzhou','shenzhen','chongqing']: 
                s_url = self.start_urls[0].replace('beijing',city)
                for i in range(1, 2): 
                    new_url = s_url.replace('=1','='+str(i))
                    yield Request(url = new_url,callback=self.parse)

