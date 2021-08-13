import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls =[
        'http://quotes.toscrape.com/'
    ]
    # analizar la respuesta http que nos envia la peticion de esta pagina y xon ella extrar el la información       
    def parse(self, response):
        print('*' * 10)
        print(response.status, response.headers)
        print('*' * 10)

        