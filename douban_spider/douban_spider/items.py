# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()       # movie name
    ranking = scrapy.Field()    # movie ranking
    score = scrapy.Field()      # movie score
    score_num = scrapy.Field()  # movie score from how many people
    quote = scrapy.Field()      # movie quote
    link = scrapy.Field()       # movie link