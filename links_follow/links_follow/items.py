# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LinksFollowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link_text = scrapy.Field()
    link_href = scrapy.Field()
    link_type = scrapy.Field()
    current_page = scrapy.Field()
    page_title = scrapy.Field()