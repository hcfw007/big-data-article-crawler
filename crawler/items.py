# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class USDoDArticleItem(scrapy.Item):

    title = scrapy.Field()

    url = scrapy.Field()

    date = scrapy.Field()

    mark = scrapy.Field()