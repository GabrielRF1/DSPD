import scrapy
import re
from dict_bot.items import DictBotItem
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
        # "https://en.wiktionary.org/wiki/desarraigar",
        # "https://en.wiktionary.org/wiki/a_cavalo_dado_n%C3%A3o_se_olha_os_dentes",
        "https://en.wiktionary.org/wiki/%C3%A2nus",
        # "https://en.wiktionary.org/wiki/faca",
        # "https://en.wiktionary.org/wiki/a",
        "https://en.wiktionary.org/wiki/gênio",
        # "https://en.wiktionary.org/wiki/grilh%C3%B5es",
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
                    
                    def_ol_item_loader = ItemLoader(item=item_loader.item, selector=def_ol)
                    def_ol_item_loader.add_css("defs", "ol>li") # definitions
                    def_ol_item_loader.add_css("synonyms", "ol>li") # synonyms
                    item_loader.add_value("defs", def_ol_item_loader.get_output_value("defs"))
                    item_loader.add_value("synonyms", def_ol_item_loader.get_output_value("synonyms"))
                    yield item_loader.load_item()  

    # Parses the definition, the examples and the synonyms.
    # They are kinda tied together in the HTML, that's why it's done like this
    def parseDefSynExp(self, response, id, item_loader):
        try:
            def_ol = response.xpath("//ol[preceding-sibling::*[./span[@id=\""
                                    + id + "\"]]]")[0]
        except:
            return (None, [], [], [])
        # get li tags preceded by ol tags, this is done because this way because
        # of the fact that some times inside a definition there will be a li
        # preceded by a ul, those are quotation and not definitions. We don't
        # want those
        defs = def_ol.css("ol>li")
        count = 1
        definition = ""
        synonyms = []
        antonyms = []
        examples = []
        for defi in defs:
            text_list = self.removeSubDefinitions(defi)
            try:  # example sentences, synonyms or antonyms
                target_index = [i for i, item in enumerate(
                    text_list) if re.search('\\n', item)][0]
                before_brk = text_list[target_index].split("\n")[0]
                after_brk = text_list[target_index].split("\n")[1]
                text_list[target_index -
                          1] = text_list[target_index-1] + before_brk
                text_list[target_index+1] = after_brk + \
                    text_list[target_index+1]
                not_a_definition_list = self.getExamplesAndSynonyms(text_list,
                                                                    target_index)
                for non_def in not_a_definition_list:
                    try:  # try for synonyms
                        syn = re.compile('Synonym(s?):')
                        # 'synonym' or 'synonyms'
                        syn_text = re.search(syn, ''.join(non_def)).group()
                        target_index_s = non_def.index(syn_text)
                        syn_list = non_def[target_index_s+2:]
                        synonym = "".join(syn_list)
                        synonym = synonym.split(',')
                        synonym = [str(count) + ". " + s for s in synonym]
                        synonyms.extend(synonym)
                        synonyms = list(filter
                                        (lambda v: (v not in syn_ant_noise), synonyms))
                    except:
                        try:  # try for antonyms
                            syn = re.compile('Antonym(s?):')
                            # 'Antonym' or 'Antonyms'
                            syn_text = re.search(syn, ''.join(non_def)).group()
                            target_index_s = non_def.index(syn_text)
                            syn_list = non_def[target_index_s+2:]
                            antonym = "".join(syn_list)
                            antonym = antonym.split(',')
                            antonym = [str(count) + ". " + s for s in antonym]
                            antonyms.extend(antonym)
                            antonyms = list(filter
                                            (lambda v: (v not in syn_ant_noise), antonyms))
                        except:  # neigher a synonym nor a antonym: this means it is a example
                            example = str(count) + ". " + "".join(non_def)
                            examples.append(example)

                # lastly, we get the definition portion of the tag <li>
                text_list = text_list[:target_index]
            except:  # only definitions
                pass

            if len(text_list) != 0:
                main_def = "".join(text_list)
                if main_def != " ":
                    definition = definition + \
                        str(count) + "." + main_def + "; "
                    count = count + 1

        return (definition, synonyms, antonyms, examples)

    # Sometime definitions will have subdefinitions in their HTML li tag,
    # So we remove them from the main definition.
    # this 'sub-defs' (most of the time, just translations) are themselves a li
    # tag preceded by a ol tag, so they will appear later as their own definition
    def removeSubDefinitions(self, defi):
        sub_defs = defi.css("ol")
        sub_defis = sub_defs.css("*::text").getall()
        text_list = defi.css("*::text").getall()
        text_list = removeSublistFromList(sub_defis, text_list)
        return text_list

    # examples and synonyms will be after a definition, here we get a list of
    # those
    def getExamplesAndSynonyms(self, text_list, target_index):
        not_a_definition_list = text_list[target_index+1:]
        ndef_str = r'{}'.format('<>'.join(not_a_definition_list))
        return [line.split('<>') for line in ndef_str.split('\n')]

    # get a single synonym
    def parseSynonym(self, non_def, count):
        syn = re.compile('Synonym(s?):')
        # 'synonym' or 'synonyms'
        syn_text = re.search(syn, ''.join(non_def)).group()
        target_index_s = non_def.index(syn_text)
        syn_list = non_def[target_index_s+2:]
        synonym = "".join(syn_list)
        synonym = synonym.split(',')
        synonym = [str(count) + ". " + s for s in synonym]
        return synonym
