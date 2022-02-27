import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from dict_bot.items import DictBotFinalItem, DictBotIntermediateItem
from scrapy.loader import ItemLoader
import languages
import languages_settings

class dictSpider(CrawlSpider):
    name = "dict_bot"
    allowed_domains = ["en.wiktionary.org"]

    def __init__(self, *a, **kw):
        super(dictSpider, self).__init__(*a, **kw)
        self.start_urls = languages_settings.languages[self.lang]['start-url-crawler']
        self.rules = (
        Rule(link_extractor=LinkExtractor(
            restrict_css=[
                'div.CategoryTreeItem',
                'div.mw-parser-output > ul a[title^=\'Category:\']'],
            deny='Category:Terms_derived_from_'+languages_settings.languages[self.lang]['language'])),
        Rule(link_extractor=LinkExtractor(
            restrict_css=[
                'div.mw-category-group',
                'td#oldest-pages',
                'td#recent-additions',
                '*:not(.p-form-of) > *:lang('+self.lang+'):not(.p-form-of)']), callback='parse_word_page', follow=True),
        )
        super(dictSpider, self)._compile_rules()

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
                    word_p_item_loader.add_css("gender", "span.gender") # Gender
                             
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