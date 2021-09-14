import scrapy
import time

word_classes = ["Noun", "Verb", "Adjective", "Pronoun", "Article",
                  "Contraction", "Preposition", "Proverb", "Proper noun",
                  "Adverb", "Conjunction", "Numeral", "Interjection", "Symbol"]

language = "Portuguese"
lang = "pt"

# Coletar dados online para dicionário
class proxySpider(scrapy.Spider):
    name = "pt_enDic"
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
        i = 0
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse_word_page)
            i = i+1
            if i == 3:
                break

    def parse_word_page(self, response):
        spans = response.css("span.mw-headline")
        lang_found = False
        for span in spans:
            if lang_found:
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
                        gender = ""
                    word = ''.join(word_p.css("strong *::text").getall())

                    defs = def_ol.css("li")
                    count = 1
                    definition = ""
                    for defi in defs:
                        text_list = defi.css('li *::text').getall()
                        if len(text_list) != 0:
                            definition = definition + str(count) + '.' + ''.join(text_list) + "; "
                            count = count + 1

                    yield {
                        "word": word,
                        "alt":"",
                        "gender":gender,
                        "defs":definition,
                        "word_class":word_class
                    }

            if span.css("::text").get() == language:
                lang_found = True
