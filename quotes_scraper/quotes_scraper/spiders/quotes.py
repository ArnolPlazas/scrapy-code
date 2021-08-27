import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class = "text" and @itemprop="text"]/text()
# Top ten tags = //div[contains(@class, "tags-box"]//span[@class="tag-item"]/a/text()
# Next page button = //ul[@class="pager"]//li[@class="next"]/a/@href

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls =[
        'http://quotes.toscrape.com/'
    ]

    custom_settings = {
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json',
    }

    # analizar la respuesta http que nos envia la peticion de esta pagina y con ella extraer la información       
    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        top_ten_tags = response.xpath('//div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()
        
        yield {
            'Title': title,
            'quotes': quotes,
            'top_ten_tags': top_ten_tags
        } 
        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()

        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)

        