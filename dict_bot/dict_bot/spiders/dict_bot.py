import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from dict_bot.items import DictBotFinalItem, DictBotIntermediateItem
from scrapy.loader import ItemLoader
import languages
import languages_settings

class dictSpider(CrawlSpider):
    name = "dict_bot"

    def __init__(self, *a, **kw):
        super(dictSpider, self).__init__(*a, **kw)
        self.allowed_domains = [self.base_lang+".wiktionary.org"]
        language = languages_settings.lang_base_to_language[self.base_lang]

        self.start_urls = language[self.lang]['start-url-crawler']
        
        cur_lang = language[self.lang]['language']
        other_langs = languages.select_languages_list[self.base_lang].copy()
        other_langs.remove(cur_lang)
        other_langs = [(lang+'_').replace(' ','_') for lang in other_langs]
        deny_rules = ['Category:Terms_derived_from_'+language[self.lang]['language'],'Grammar']
        deny_rules.extend(other_langs)

        self.rules = (
        Rule(link_extractor=LinkExtractor(
            restrict_css=[
                'div.CategoryTreeItem',
                'div.mw-parser-output > ul a[title^=\'Category:\']'
            ],
            deny=deny_rules
            )
        ),
        Rule(link_extractor=LinkExtractor(
            # restrict_xpaths=[
            # '//*[@lang = \''+self.lang+'\' and (not(ancestor::*[@class=\'p-form-of\']) and not(ancestor::*[@class=\'form-of\']) and not(ancestor::*[@class=\'NavFrame\']))]'
            # ],
            restrict_css=[
                'div.mw-category-group',
                'td#oldest-pages',
                'td#recent-additions']), callback='parse_word_page', follow=True),
        )
        super(dictSpider, self)._compile_rules()

    def parse_word_page(self, response):
        spans = response.css("span.mw-headline")
        language = languages_settings.lang_base_to_language[self.base_lang]
        lang_found = False
        alt_forms = []
        for span in spans:
            headline = span.attrib['id']                
            if str(headline).lower() in [langu.lower() for langu in languages.select_languages_list[self.base_lang]]:
                if headline == language[self.lang]['language']:
                    lang_found = True
                else:
                    lang_found = False
            else: 
                headline = span.css("::text").get()
            if lang_found:
                final_item_loader = ItemLoader(item=DictBotFinalItem(), selector=span)
                id = span.attrib["id"]
                
                if "Alternative_forms" in id:  # Alternative form
                    alt_ul = response.xpath("//ul[preceding-sibling::*[./span[@id=\""
                                            + id+"\"]]]")[0]
                    alt_ul_item_loader = ItemLoader(item=DictBotIntermediateItem(), selector=alt_ul)
                    alt_ul_item_loader.add_css("alt", "li")
                    alt_forms = alt_ul_item_loader.get_output_value("alt")

                if headline in language[self.lang]['word_classes']:  # Word class
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
                    def_ol_item_loader.add_css("defs", "ol>li") 

                    final_item_loader.add_value("word", word_p_item_loader.get_output_value("word")) 
                    final_item_loader.add_value("gender", word_p_item_loader.get_output_value("gender"))
                    final_item_loader.add_value("alt", alt_forms) 
                    final_item_loader.add_value("defs", def_ol_item_loader.get_output_value("defs"))
                    final_item_loader.add_css("word_class", "::text")   
                    

                    yield final_item_loader.load_item()  