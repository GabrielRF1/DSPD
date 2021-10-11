# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join, Identity
import re
from w3lib.html import remove_tags

def non_empty_indentity(value):
    if value is not None and value != '':
        return value

def remove_line_break_and_forth(value):
    return value.split('\n')[0]

def search_synonyms(value):
    splited_list = value.split('\n')
    syn = re.compile('Synonym(s?): ')
    return_values = []
    for splited in splited_list:
        try:
            syn_text = re.search(syn, splited).group()
            return_values.extend(splited.split(syn_text)[1].split(', '))
        except:
            continue
    if len(return_values) != 0:
        return return_values

class DictBotItem(scrapy.Item):
    # define the fields for your item here like:
    _word = scrapy.Field(input_processor = Identity(), output_processor = Join(''))
    alt = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = Identity())
    defs = scrapy.Field(input_processor = MapCompose(remove_tags, remove_line_break_and_forth),
     output_processor = MapCompose(non_empty_indentity))
    gender = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    synonyms = scrapy.Field(input_processor = MapCompose(remove_tags, search_synonyms), output_processor = TakeFirst())
    # antonyms = scrapy.Field(input_processor = MapCompose(), output_processor = TakeFirst())
    word_class = scrapy.Field(input_processor = Identity(), output_processor = TakeFirst())
    # extras = scrapy.Field(input_processor = MapCompose(), output_processor = TakeFirst())

    pass
