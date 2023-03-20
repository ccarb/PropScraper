from scrapy import Request
from scrapy.http import TextResponse
import scrapy
import scrapy.utils.misc
import scrapy.core.scraper

def warn_on_generator_with_return_value_stub(spider, callable):
    pass

scrapy.utils.misc.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub
scrapy.core.scraper.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub

class losCerrosSpider(scrapy.Spider):
    name = "losCerros"

    def start_requests(self):
        url = 'https://xintel.com.ar/api/?json=resultados.fichas&inm=LCR&apiK=YXKRGYO3JUQS020AYLXF7MAJ2&page=0&destacados=&tipo_operacion=A&tipo_inmueble=All&sSearch=&valor_minimo=&valor_maximo=&moneda=&barrios1=All&Ambientes=&rppagina=10&permuta='

        headers = {
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
            "Accept": "*/*",
            "Referer": "https://loscerrospropiedades.com/",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "sec-ch-ua-platform": "\"Windows\""
        }

        request = Request(
            url=url,
            method='GET',
            dont_filter=True,
            headers=headers,
        )
        yield request

    def parse(self,response):
        textResp=TextResponse.copy(response)
        data=textResp.json()
        for ficha in data["resultado"]["fichas"]:
            yield {
                'title': ficha["titulo"],
                'link': "https://loscerrospropiedades.com/" + ficha["amigable"],
                'price': ficha["alquiler_precio"]
            }
