# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import Selector
from qsbk_spider.qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domin = 'https://www.qiushibaike.com'

    def parse(self, response):
        assert isinstance(response, HtmlResponse)
        contents = response.xpath("//div[@class='col1 old-style-col1']/div")
        """:type:SelectorList"""
        for content in contents:
            assert isinstance(content, Selector)
            author = content.xpath(".//h2/text()").get()
            article = content.xpath(".//div[@class='content']//text()").getall()
            print(author)
            article = "".join(article).strip()
            print(article)
            qsbkitem = QsbkItem(author=author, article=article)
            yield qsbkitem
        next_page = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_page:
            return
        else:
            yield scrapy.Request(self.base_domin + next_page, callback=self.parse)
