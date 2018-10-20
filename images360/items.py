# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class ImageItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义四个字段，图片的ID，链接，标题，缩略图，两个属性collection 和 table 都定义成images字符串，
    # 分别代表MongoDB存储的Collection名称和MySQL存储的表名称
    collection = table = 'image'
    id = Field()
    url = Field()
    title = Field()
    thumb = Field()
