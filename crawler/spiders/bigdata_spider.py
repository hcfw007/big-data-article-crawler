from scrapy import Request
from scrapy.spiders import Spider
from crawler.items import USDoDArticleItem
import re

class BigdataSpider(Spider):

    name = 'USDoDSpider'

    start_urls = ['https://www.defense.gov/Explore/News/Listing/']

    count = 0

    def parse(self, response):
        story_cards = response.xpath('//story-card[@article-title]')
        item = USDoDArticleItem()

        for card in story_cards:
            item['title'] = card.xpath('.//@article-title').extract()[0]

            if re.search(r'data', item['title'], re.I) == None: continue
            
            item['url'] = card.xpath('.//@article-url').extract()[0]
            
            item['date'] = card.xpath('.//@publish-date-jss').extract()[0]

            yield item

        next_page = response.xpath('//span[@class="fa fa-chevron-right"]/../@href').extract()
        if next_page:
            next_url = next_page[0]
            yield Request(next_url)
        