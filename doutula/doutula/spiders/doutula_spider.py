# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DoutulaItem


class DoutulaSpiderSpider(CrawlSpider):
    name = 'doutula_spider'
    # allowed_domains = ['doutula.com']
    start_urls = ['https://www.doutula.com/article/list/?page=1']

    rules = (
        Rule(LinkExtractor(allow=r'/article/list/\?page=\d'), callback='parse_img', follow=True,
             process_links='makeAbsolutePath'),  # 问号要转义
    )

    def parse_item(self, response):
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def parse_img(self, response):
        assert isinstance(response, HtmlResponse)
        print("=" * 10)
        list_group = response.xpath("//a[contains(@class,'list-group-item')]")
        for item in list_group:
            assert isinstance(item, scrapy.selector.unified.Selector)  # item 是一组图片的Selector对象
            article = item.xpath(".//div[@class='random_title']/text()").get()  # 一组图片的标题
            date = item.xpath(".//div[@class='date']/text()").get()  # 一组图片的时间
            # time = item.css(".date").get()#一组图片的时间
            # pic_urls = item.xpath("//div[@class='random_article']/div[@class='col-xs-6 col-sm-3']/img/@data-original").getall()
            # pic_urls = item.xpath("//img/@data-original").getall()
            pic_urls = item.css(".random_article img::attr(data-original)").getall()
            print(pic_urls)
            item = DoutulaItem(article=article, date=date, pic_urls=pic_urls)
            yield item
        print(list_group)
        print("=" * 10)

    def makeAbsolutePath(self, links):
        print(links)

        return links
