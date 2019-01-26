# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst, Compose
from w3lib.html import remove_tags

def TakeSecond (value):
    if len(value) >= 2:
        return value[1]


def RelativeToAbsoluteUrl (value):
    return "https://www.sec.gov/{0}".format(value);


class Litigation(scrapy.Item):
    release_no = scrapy.Field()
    date = scrapy.Field()
    respondents = scrapy.Field()
    title = scrapy.Field( input_processor=TakeFirst() )
    subtitle = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=Join('\n'))
    content = scrapy.Field(input_processor=Join())
    references_names = scrapy.Field()
    references_urls = scrapy.Field()
    references_sidebar_names = scrapy.Field()
    references_sidebar_urls = scrapy.Field(input_processor=MapCompose(RelativeToAbsoluteUrl))


    pass
