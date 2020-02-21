import scrapy
from ..items import QuotesBotItem

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):

        items = QuotesBotItem()

        all_div_quotes = response.css("div.quote")

        for quotes in all_div_quotes:
            text = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()

            items["text"] = text
            items["author"] = author
            items["tag"] = tag

            yield items