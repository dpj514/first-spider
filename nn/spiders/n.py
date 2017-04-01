# -*- coding: utf-8 -*-
import scrapy
import re
class NSpider(scrapy.Spider):
    name = "n"
    allowed_domains = ["moe.gov.cn"]
    start_urls = ['http://www.moe.gov.cn/jyb_xwfb/']

    def parse(self, response):
        for href in response.css('[target][title] ::attr(href)').extract():
            try:
                news = re.findall(r'/s\d{3,4}.*20170\d/t\d{8}_\d{6}\.html', href)[0]
                url = 'http://www.moe.gov.cn/jyb_xwfb' + news
            except:
                continue
            yield scrapy.Request(url,callback=self.parse_news)
    def parse_news(self,response):
        items = []
        item = {}
        item['标题']=str(response.css('title::text').extract()[0]),
        item['内容']=str(response.css('p::text').extract()).replace(r'\u3000',''),
        item['链接']=str(response.url),
        items.append(item)
        return items


