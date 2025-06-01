import Scrapy

class ChocolateTestSpiderCrawler(scrapy.Spider):
    name = "chocolate_test_pider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = [
    'https://www.chocolate.co.uk/collections/all'
    ]

    def parse(self,response):
        pass