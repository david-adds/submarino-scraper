# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SubmarinoItem(scrapy.Item):
    product_name = scrapy.Field()
    product_url = scrapy.Field()
    price = scrapy.Field()
    
