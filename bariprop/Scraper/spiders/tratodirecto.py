import scrapy


class TratoDirectoSpider(scrapy.Spider):
    name = 'tratoDirecto'
    start_urls = ['https://www.tratodirecto.com.ar/propiedad/properties?properties_status=22&properties_type=0&properties_bedrooms=0&properties_bathrooms=0&properties_vendedor=0']

    def parse(self, response):
        for item in response.xpath('//div[@class="sc_properties_item_info"]'):
            title= item.xpath('div/div/span/span/div[@class="properties_page_data"]/text()')
            if title==[]:
                title=['']
            else:
                title=title.get().replace("\t",'').replace("\n",'').split('.')
            yield {
                'title': title[0],
                'link':  item.xpath('div/div[@class="sc_properties_item_button sc_item_button"]/a/@href').get(),
                'price': item.xpath('div/span/span/text()').get()
            }
        
