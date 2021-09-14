import scrapy

# Coletar dados online para dicionário
class proxySpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'https://en.wiktionary.org/wiki/Index:Portuguese/a',
    ]


    def parse(self, response):
        pass
