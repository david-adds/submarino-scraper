import scrapy


class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    allowed_domains = ['https://www.submarino.com.br/categoria/informatica/notebooks?ordenacao=relevance&origem=omega&source=blanca']
    start_urls = ['http://https://www.submarino.com.br/categoria/informatica/notebooks?ordenacao=relevance&origem=omega&source=blanca/']

    def parse(self, response):
        pass
