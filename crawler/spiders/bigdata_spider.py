from scrapy.spiders import Spider

class BigdataSpider(Spider):

    name = 'USDoDSpider'

    start_urls = ['https://www.defense.gov/Explore/News/Listing/']

    def parse(self, response):
        titles = response.xpath('//story-card[@article-title]/attribute::article-title').extract()

        print(response)

        for title in titles:
            print(title.strip())