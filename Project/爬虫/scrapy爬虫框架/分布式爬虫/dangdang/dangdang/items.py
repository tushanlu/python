# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    big_name = scrapy.Field()
    big_link = scrapy.Field()
    small_name = scrapy.Field()
    small_link = scrapy.Field()
    name = scrapy.Field()
    book_link = scrapy.Field()
    author = scrapy.Field()
    Press = scrapy.Field()
    book_time = scrapy.Field()
    price = scrapy.Field()
    book_data = scrapy.Field()
