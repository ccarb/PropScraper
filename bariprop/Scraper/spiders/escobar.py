import scrapy


class EscobarSpider(scrapy.Spider):
    name = 'escobar'
    allowed_domains = ['escobarnegociosinmobiliarios.com']
    start_urls = ['https://www.escobarnegociosinmobiliarios.com/buscar/?operation=2&type=&bedrooms=&currency=&currency=&priceFrom=15000&priceTo=&view=list&page=0&zone1=']

    def parse(self, response):
        for item in response.xpath('//div[@class="searchpage-item"]'):
                yield {
                    'title': item.xpath('div[@class="data"]/div[@class="title"]/a/text()').get(),
                    'link': 'www.' + self.allowed_domains[0] + item.xpath('div[@class="data"]/div[@class="title"]/a/@href').get(),
                    'price': item.xpath('div[@class="data"]/div[@class="price"]/text()').get()
                }
        
