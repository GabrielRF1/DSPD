import scrapy
import re
from dict_bot.items import DictBotFinalItem, DictBotIntermediateItem
from scrapy.loader import ItemLoader
import languages
import languages_settings

syn_ant_noise = [", ", " ", ""]
links_noise = ["*", "►"]

class dictSpider(scrapy.Spider):
    name = "dict_bot"


    def start_requests(self):
        start_urls = languages_settings.languages[self.lang]['start-urls_'+self.index]
        for url in start_urls:
            yield scrapy.Request(url=url, callback = self.parse)

    # start_urls = [
    #     # "https://en.wiktionary.org/wiki/gente",
    #     # "https://en.wiktionary.org/wiki/desarraigar",
    #     # "https://en.wiktionary.org/wiki/a_cavalo_dado_n%C3%A3o_se_olha_os_dentes",
    #     # "https://en.wiktionary.org/wiki/%C3%A2nus",
    #     # "https://en.wiktionary.org/wiki/faca",
    #     # "https://en.wiktionary.org/wiki/a",
    #     # "https://en.wiktionary.org/wiki/gênio",
    #     # "https://en.wiktionary.org/wiki/grilh%C3%B5es",
    #     # "https://en.wiktionary.org/wiki/matar",
    #     # "https://en.wiktionary.org/wiki/cobre",
    #     # "https://en.wiktionary.org/wiki/besta",
    #     # "https://en.wiktionary.org/wiki/cesta",
    #     # "https://en.wiktionary.org/wiki/dar",
    # ]

    def parse(self, response):
        word_block = response.css("div.index").css("li")
        urls = set()
        for word in word_block:
            links = word.css("a")
            for link in links:
                if link.css("::text").get() in links_noise or "/w/" in link.attrib["href"]:
                    pass
                else:
                    urls.add("https://en.wiktionary.org"+link.attrib["href"])
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_word_page)

    def parse_word_page(self, response):
        spans = response.css("span.mw-headline")
        lang_found = False
        alt_forms = []
        for span in spans:
            headline = span.css("::text").get()
            if headline in languages.languages:
                if headline == languages_settings.languages[self.lang]['language']:
                    lang_found = True
                else:
                    lang_found = False
            if lang_found:
                final_item_loader = ItemLoader(item=DictBotFinalItem(), selector=span)
                id = span.attrib["id"]
                
                if "Alternative_forms" in id:  # Alternative form
                    alt_ul = response.xpath("//ul[preceding-sibling::*[./span[@id=\""
                                            + id+"\"]]]")[0]
                    alt_ul_item_loader = ItemLoader(item=DictBotIntermediateItem(), selector=alt_ul)
                    alt_ul_item_loader.add_css("alt", "li")
                    alt_forms = alt_ul_item_loader.get_output_value("alt")

                if headline in languages_settings.languages[self.lang]['word_classes']:  # Word class
                    try:
                        word_p = response.xpath("//p[preceding-sibling::*[./span[@id=\""
                                                + id + "\"]]]")[0]
                    except:
                        continue
                    word_p_item_loader = ItemLoader(item=DictBotIntermediateItem(), selector=word_p)
                    word_p_item_loader.add_css("word", "p>strong:first-child *::text, b:first-child *::text") # Word
                    word_p_item_loader.add_css("gender", "abbr") # Gender
                             
                    try:
                        def_ol = response.xpath("//ol[preceding-sibling::*[./span[@id=\""
                                                + id + "\"]]]")[0]
                    except:
                        continue
                    
                    def_ol_item_loader = ItemLoader(item=DictBotIntermediateItem(), selector=def_ol)
                    def_ol_item_loader.add_css("defs", "ol>li") # definitions = format: ["definition",["synonyms"],["antonym"],["extras(mostly examples)"]]

                    final_item_loader.add_value("word", word_p_item_loader.get_output_value("word")) 
                    final_item_loader.add_value("gender", word_p_item_loader.get_output_value("gender"))
                    final_item_loader.add_value("alt", alt_forms) 
                    final_item_loader.add_value("defs", def_ol_item_loader.get_output_value("defs"))
                    final_item_loader.add_css("word_class", "::text")   
                    

                    yield final_item_loader.load_item()  