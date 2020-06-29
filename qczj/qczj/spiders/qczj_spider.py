# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class QczjSpiderSpider(scrapy.Spider):
    name = 'qczj_spider'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        assert isinstance(response,HtmlResponse)
        uibox = response.xpath("//div")
        pass
