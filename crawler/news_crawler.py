import scrapy
from bs4 import BeautifulSoup

class Crawler(scrapy.Spider):
    name = "Narutocrawler"
    start_urls = ['https://www.hawkai.online/']

    def parse(self, response):
        for href in response.css('.news-section')[0].css("a::attr(href)").extract():
            print(href)
            

