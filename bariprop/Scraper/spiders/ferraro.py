from scrapy import Request
from scrapy.http import TextResponse
import scrapy
from urllib.parse import unquote
import scrapy.utils.misc
import scrapy.core.scraper

def warn_on_generator_with_return_value_stub(spider, callable):
    pass

scrapy.utils.misc.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub
scrapy.core.scraper.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub

class ferraroSpider(scrapy.Spider):
    name = "ferraro"

    def start_requests(self):
        url = 'https://www.ferrarapropiedades.com/wp-content/themes/wpresidence_3-9/ajax_handler.php'
        
        headers = {
            "authority": "www.ferrarapropiedades.com",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "sec-ch-ua-platform": "\"Windows\"",
            "origin": "https://www.ferrarapropiedades.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.ferrarapropiedades.com/",
            "accept-language": "es-419,es;q=0.9,en;q=0.8"
        }

        body = 'action=wpestate_ajax_filter_listings&action_values=rentals&category_values=Categories&county=States&city=Cities&area=Areas&order=0&newpage=1&page_id=26574&align=vertical&card_version=&rownumber=4&ishortcode=1&security=cab7679be8'

        request = Request(
            url=url,
            method='POST',
            dont_filter=True,
            headers=headers,
            body=body,
        )

        yield request

    def parse(self,response):
        textResp=TextResponse.copy(response)
        data=textResp.json()
        for marker in data["markers"]:
            yield {
                'title': unquote(marker[0]),
                'link':  unquote(marker[9]),
                'price': marker[11]
            }
