# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['www.wxapp-union.com']
    start_urls = ['c']


    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'),callback="parse_index",
             follow=True),#用正则表达式拦截url
        Rule(LinkExtractor(allow=r".+article-.+\.html")#.表示任意单字符，+表示匹配多次文章内部的关联链接不需要跟进
             ,callback="parse_detail"
             ,follow=False)
    )

    def parse_detail(self, response):
        assert isinstance(response,HtmlResponse)
        title = response.xpath("//h1[@class='ph']/text()").get()
        print(title)
        author_p = response.xpath("//p[@class='authors']")
        author = author_p.xpath(".//a/text()").get()
        print(author)
        post_time = author_p.xpath(".//span/text()").get()
        article_content = response.xpath("//td[@id='article_content']//text()").getall()
        print(post_time)
        article_content = "".join(article_content).strip()
        print(article_content)
    def parse_index(self,response):
        print(response)