import scrapy

# Coletar dados online para dicionário
class proxySpider(scrapy.Spider):
    name = "test"
    start_urls = [
        # Palavras Classificadas por dificuldade para o Teste de proficiência em chinês
        'https://en.wiktionary.org/wiki/Appendix:HSK_list_of_Mandarin_words/Beginning_Mandarin',
        'https://en.wiktionary.org/wiki/Appendix:HSK_list_of_Mandarin_words/Elementary_Mandarin',
        'https://en.wiktionary.org/wiki/Appendix:HSK_list_of_Mandarin_words/Intermediate_Mandarin',
        'https://en.wiktionary.org/wiki/Appendix:HSK_list_of_Mandarin_words/Advanced_Mandarin',

        # Frequency list
        'https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/1-1000',
        'https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/1001-2000',
        'https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/2001-3000',
        'https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/3001-4000',
        'https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/4001-5000',
        'https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/5001-6000',
        'https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/6001-7000',
        'https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/7001-8000',
        'https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/8001-9000',
        'https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/9001-10000'
    ]


    def parse(self, response):
        pass
