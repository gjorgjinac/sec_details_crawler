# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst



class Litigation(scrapy.Item):
    release_no = scrapy.Field()
    date = scrapy.Field()
    respondents = scrapy.Field()
    title = scrapy.Field(input_processor=TakeFirst())
    subtitle = scrapy.Field(input_processor=TakeFirst())
    content = scrapy.Field(input_processor=Join())


    pass
