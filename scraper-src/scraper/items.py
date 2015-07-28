# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Location(scrapy.Item):
    title = scrapy.Field()
    schools = scrapy.Field()


class School(scrapy.Item):
    title = scrapy.Field()
    results = scrapy.Field()


class Result(scrapy.Item):
    full_name = scrapy.Field()
    math = scrapy.Field()
    physics = scrapy.Field()
    chemistry = scrapy.Field()
    geometry = scrapy.Field()
    biology = scrapy.Field()
    geography = scrapy.Field()
    history = scrapy.Field()
    eng_lang = scrapy.Field()
    ger_lang = scrapy.Field()
    fr_lang = scrapy.Field()
    kyr_lang = scrapy.Field()
    rus_lang = scrapy.Field()
    uzb_lang = scrapy.Field()
    informatics = scrapy.Field()
    civics = scrapy.Field()
    notes = scrapy.Field()

