# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode

import scrapy
from scrapy import Request

from ..items import ImageItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        data = {
       'q': '摄影',
       'src': 'srp',
       'correct': '摄影',
       'pn': '0',
       'ch':'',
        'ran': '0',
        'ras': '6',
        'cn': '0',
        'gn': '0',
        'kn': '38',
        }
        base_url = 'https://image.so.com/j?'
        for page in range(1, self.settings.get('MAX_PAGE')+1):
            data['sn'] = page * 60 + 38
            params = urlencode(data)
            # 利用urlencode()方法将字典转化为url的GET参数，构造完整URL，构造并生成Request
            url = base_url + params
            yield Request(url, self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = ImageItem()
            item['id'] = image.get('id')
            item['url'] = image.get('img')
            item['title'] = image.get('title')
            item['thumb'] = image.get('_thumb')
            yield item
