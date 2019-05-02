# -*- coding: utf-8 -*-
import scrapy
from douban_spider.items import DoubanMovieItem



class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        item = DoubanMovieItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            item['link'] = movie.xpath('.//div[@class="hd"]/a/@href').extract_first()
            item['quote'] = movie.xpath('.//span[@class="inq"]/text()').extract()[0]
            yield item

        next_sub_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_sub_url:
            next_url = response.urljoin(next_sub_url[0])
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
