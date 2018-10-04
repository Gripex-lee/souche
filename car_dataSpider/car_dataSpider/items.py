# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarDataspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()#品牌
    time = scrapy.Field()#上牌时间
    milestone = scrapy.Field()#里程数
    gGB = scrapy.Field()#外迁查询
    price = scrapy.Field()#现价 
    new_price = scrapy.Field()#新车价

    