import scrapy
import time

word_classes = ["Noun", "Verb", "Adjective", "Pronoun", "Article",
                  "Contraction", "Preposition", "Proverb", "Proper noun",
                  "Adverb", "Conjunction", "Numeral", "Interjection", "Symbol"]

language = "Portuguese"
lang = "pt"

# Coletar dados online para dicionário
class dictSpider(scrapy.Spider):
    name = "dict_bot"
    start_urls = [
        "https://en.wiktionary.org/wiki/Index:Portuguese/a",
    ]


    def parse(self, response):
        word_block = response.css("div.index").css("li")
        urls = set()
        for word in word_block:
            links = word.css("a")
            for link in links:
                if link.css("::text").get() == "*" or link.css("::text").get() == "►" or "/w/" in link.attrib["href"]:
                    pass
                else:
                    urls.add("https://en.wiktionary.org"+link.attrib["href"])
                    #yield {"link": link.attrib["href"]}
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse_word_page)

    def parse_word_page(self, response):
        spans = response.css("span.mw-headline")
        lang_found = False
        for span in spans:
            if lang_found:
                alt_forms = []
                if span.attrib["id"] == "Alternative_forms":
                    alt_ul = response.xpath("//ul[preceding-sibling::*[./span[@id=\"Alternative_forms\"]]]")[0]
                    alt_forms_li = alt_ul.css("li")
                    for alt_form in alt_forms_li:
                        if alt_form.attrib["lang"] != lang:
                            break
                        alt_forms.append(alt_form.css("* ::text").get())


                if span.css("::text").get() in word_classes:
                    word_class = span.css("::text").get()
                    id = span.attrib["id"]
                    try:
                        def_ol = response.xpath("//ol[preceding-sibling::h4[./span[@id=\""+ id +"\"]]]")[0]
                        word_p = response.xpath("//p[preceding-sibling::h4[./span[@id=\""+ id +"\"]]]")[0]
                    except:
                        try:
                            def_ol = response.xpath("//ol[preceding-sibling::h3[./span[@id=\""+ id +"\"]]]")[0]
                            word_p = response.xpath("//p[preceding-sibling::h3[./span[@id=\""+ id +"\"]]]")[0]
                        except:
                            continue
                    if word_p.css("strong").attrib["lang"] != lang:
                        break
                    try:
                        gender = word_p.css("abbr::text").get()
                    except:
                        gender = None
                    word = "".join(word_p.css("strong.Latn.headword *::text").getall())

                    defs = def_ol.css("li")
                    count = 1
                    definition = ""
                    for defi in defs:
                        text_list = defi.css("li *::text").getall()
                        try: # found example sentences or synonyms
                            target_index = text_list.index("\n")
                            try:
                                target_index_s = text_list.index("Synonyms:")
                                synonyms = text_list[target_index_s+2:] # synonyms
                                synonyms = list(filter(lambda v: v != ", ", synonyms))
                            except: # No Synonyms
                                pass
                            # Pegar os exemplos aqui tbm e depois:
                            text_list = text_list[:target_index]
                        except : # example sentences
                            raise

                        if len(text_list) != 0:
                            definition = definition + str(count) + "." + "".join(text_list) + "; "
                            count = count + 1

                    yield {
                        "word": word,
                        "alt": alt_forms,
                        "gender": gender,
                        "defs": definition,
                        "synonyms": synonyms,
                        "word_class": word_class,
                        "examples":
                    }

            if span.css("::text").get() == language:
                lang_found = True
