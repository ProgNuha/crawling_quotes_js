import scrapy
from selenium import webdriver
from selenium.webdriver import Chrome
from ..items import QuotesItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/js/'
    ]
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1200x600')

    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=QuoteSpider.options)

    def parse(self, response):
        pages = 10

        for page in range(1,pages):
            items = QuotesItem()
            url = "http://quotes.toscrape.com/js/page/" + str(page) + "/"
            self.driver.get(url)

            quotes = self.driver.find_elements_by_class_name('quote')

            for quote in quotes:
                qoute_text = quote.find_element_by_class_name('text').text[1:-2]
                author = quote.find_element_by_class_name('author').text

                items['qoute_text'] = qoute_text
                items['author'] = author

                yield items

        self.driver.close()