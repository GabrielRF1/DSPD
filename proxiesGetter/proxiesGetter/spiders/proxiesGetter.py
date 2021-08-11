import scrapy
#from selenium import webdriver

class proxySpider(scrapy.Spider):
    name = "proxy"
    start_urls = [
        'https://www.proxynova.com/proxy-server-list/elite-proxies/'
    ]
    #
    # def __init__(self):
    #     # Para interagir com javascript
    #     self.driver = webdriver.Firefox()

    def parse(self, response):
        #self.driver.get(response.url)

        table = response.css('table#tbl_proxy_list').css('tbody')

        # Faz uma lista de address:port
        for row in table.css('tr'):
            yield {
                '' : row.css('td::text')[0].get() + ':' + row.css('td::text')[1].get()
            }

        # try:
        #     next = self.driver.find_element_by_xpath('//*[@id="proxylisttable_next"]')
        #     next.click()
        #     yield Request(response.url,callback=self.parse)
        # except:
        #     pass
