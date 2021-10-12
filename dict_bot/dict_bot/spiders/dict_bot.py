import scrapy
import re
from dict_bot.items import DictBotItem, DictBotIntermediateItem
from scrapy.loader import ItemLoader
import languages


def findSublist(sub_list, in_list):
    sub_list_length = len(sub_list)
    for i in range(len(in_list)-sub_list_length+1):
        if sub_list == in_list[i:i+sub_list_length]:
            return (i, i+sub_list_length)
    return None


def removeSublistFromList(sub_list, in_list):
    indices = findSublist(sub_list, in_list)
    if not indices is None:
        return in_list[0:indices[0]] + in_list[indices[1]:]
    else:
        return in_list


word_classes = ["Noun", "Verb", "Adjective", "Pronoun", "Article",
                "Contraction", "Preposition", "Proverb", "Proper noun",
                "Adverb", "Conjunction", "Numeral", "Interjection", "Symbol"]

language = "Portuguese"
lang = "pt"
syn_ant_noise = [", ", " ", ""]
links_noise = ["*", "►"]

# Coletar dados online para dicionário


class dictSpider(scrapy.Spider):
    ordered_output = [{}]

    name = "dict_bot"
    start_urls = [
        # "https://en.wiktionary.org/wiki/Index:Portuguese/e",
        # "https://en.wiktionary.org/wiki/Index:Portuguese/f",
        # "https://en.wiktionary.org/wiki/Index:Portuguese/g",
        # "https://en.wiktionary.org/wiki/Index:Portuguese/h",
        "https://en.wiktionary.org/wiki/gente",
        "https://en.wiktionary.org/wiki/desarraigar",
        "https://en.wiktionary.org/wiki/a_cavalo_dado_n%C3%A3o_se_olha_os_dentes",
        "https://en.wiktionary.org/wiki/%C3%A2nus",
        "https://en.wiktionary.org/wiki/faca",
        "https://en.wiktionary.org/wiki/a",
        "https://en.wiktionary.org/wiki/gênio",
        "https://en.wiktionary.org/wiki/grilh%C3%B5es",
        "https://en.wiktionary.org/wiki/matar"
    ]

    def parse(self, response):
    #     word_block = response.css("div.index").css("li")
    #     urls = set()
    #     for word in word_block:
    #         links = word.css("a")
    #         for link in links:
    #             if link.css("::text").get() in links_noise or "/w/" in link.attrib["href"]:
    #                 pass
    #             else:
    #                 urls.add("https://en.wiktionary.org"+link.attrib["href"])
    #                 # yield {"link": link.attrib["href"]}
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parseWordPage)

    # def parseWordPage(self, response):
        spans = response.css("span.mw-headline")
        lang_found = False
        alt_forms = []
        for span in spans:
            # some pages have definition for multiple languages
            headline = span.css("::text").get()
            if headline in languages.languages.values():
                if headline == language:
                    lang_found = True
                else:
                    lang_found = False
            if lang_found:
                item_loader = ItemLoader(item=DictBotItem(), selector=span)
                id = span.attrib["id"]
                
                if "Alternative_forms" in id:  # Alternative form
                    alt_ul = response.xpath("//ul[preceding-sibling::*[./span[@id=\""
                                            + id+"\"]]]")[0]
                    alt_ul_item_loader = ItemLoader(item=item_loader.item, selector=alt_ul)
                    alt_ul_item_loader.add_css("alt", "li")
                    alt_forms = alt_ul_item_loader.get_output_value("alt")

                if headline in word_classes:  # Word class
                    item_loader.add_css("word_class", "::text")
                    item_loader.add_value("alt", alt_forms)
                    try:
                        word_p = response.xpath("//p[preceding-sibling::*[./span[@id=\""
                                                + id + "\"]]]")[0]
                    except:
                        continue
                    word_p_item_loader = ItemLoader(item=item_loader.item, selector=word_p)
                    word_p_item_loader.add_css("_word", "p>strong:first-child *::text, b:first-child *::text") # Word
                    word_p_item_loader.add_css("gender", "abbr") # Gender
                    
                    item_loader.add_value("_word", word_p_item_loader.get_output_value("_word"))    
                    item_loader.add_value("gender", word_p_item_loader.get_output_value("gender"))            
                    try:
                        def_ol = response.xpath("//ol[preceding-sibling::*[./span[@id=\""
                                                + id + "\"]]]")[0]
                    except:
                        continue
                    
                    def_ol_item_loader = ItemLoader(item=DictBotIntermediateItem(), selector=def_ol)
                    def_ol_item_loader.add_css("defs", "ol>li") # definitions = format: ["definition",["synonyms"],["antonym"],["extras(mostly examples)"]]
                    item_loader.add_value("defs", def_ol_item_loader.get_output_value("defs"))

                    yield item_loader.load_item()  