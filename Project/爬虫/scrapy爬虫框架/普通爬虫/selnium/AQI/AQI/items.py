# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AqiItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    time = scrapy.Field()
    aqi = scrapy.Field()
    level = scrapy.Field()
    Pm2_5 = scrapy.Field()
    Pm10 = scrapy.Field()
    So2 = scrapy.Field()
    Co = scrapy.Field()
    No2 = scrapy.Field()
    O3_8h = scrapy.Field()

