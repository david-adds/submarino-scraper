import scrapy
from ..items import SubmarinoItem


class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    allowed_domains = ['www.submarino.com.br']

    def start_requests(self):
        yield scrapy.Request(url='https://www.submarino.com.br/categoria/informatica/notebooks?ordenacao=relevance&origem=omega&source=blanca',
        callback=self.parse,headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
    })
    
    def parse(self, response):
        subm_item =SubmarinoItem()
        laptops = response.xpath("//div[@class='row product-grid no-gutters main-grid']//div[@class='RippleContainer-sc-1rpenp9-0 dMCfqq']")
        for laptop in laptops:
            subm_item['product_name'] = laptop.xpath(".//h2[contains(@class,'TitleUI-bwhjk3-15')]/text()").get()
            subm_item['product_url'] = laptop.xpath(".//a[contains(@class,'Link-bwhjk3-2 iDkmyz')]/@href").get()
            subm_item['price'] = laptop.xpath(".//span[contains(@class,'PriceUI-bwhjk3-11')]//text()[2]").get()
            subm_item['ratings'] = laptop.xpath(".//*[local-name()='svg'][@class='SvgUI-xoytwh-0 gyRqpB']//*[name()='desc']/text()").get()
            yield subm_item
            
