# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        data = {
            "email":"970138074@qq.com",
            "password":"pythonspider"
        }
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request

    def parse_page(self, response):
        assert isinstance(response,HtmlResponse)
        with open('renren.html','w',encoding='utf-8')as fp:
            fp.write(response.text)
