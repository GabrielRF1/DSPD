# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join, Identity
import re
from w3lib.html import remove_tags

def clean_up(value):
    if value['_def'] is not None and value['_def'] != '':
        return value

def build(value):
    splited_values = value.split('\n')
    definition = splited_values[0]
    synonyms = []
    antonyms = []
    extras = []
    syn = re.compile('Synonym(s?): ')
    ant = re.compile('Antonym(s?): ')
    synonyms.extend(search_for(syn, splited_values[1:]))
    antonyms.extend(search_for(ant, splited_values[1:]))
    extras.extend(search_for_ext(splited_values[1:]))
    
    return {'_def': definition, '_synonyms': synonyms, 'antonyms': antonyms, 'extras': extras}

def search_for_ext(values):
    result = []
    for value in values:
        to_search = re.compile('^((?!Synonym(s?): |Antonym(s)).)*$')
        try:
            ext = re.search(to_search, value).group()
            result.append(ext)
        except:
            continue
    
    return result

def search_for(regex, values):
    result = []
    for value in values:
        to_search = regex
        try:
            search_text = re.search(to_search, value).group()
            result.extend(value.split(search_text)[1].split(', '))
        except:
            continue
    
    return result

class DictBotItem(scrapy.Item):
    # define the fields for your item here like:
    _word = scrapy.Field(input_processor = Identity(), output_processor = Join(''))

    alt = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = Identity())
    
    defs = scrapy.Field()

    gender = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())

    word_class = scrapy.Field(input_processor = Identity(), output_processor = TakeFirst())

class DictBotIntermediateItem(scrapy.Item):
    defs = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = MapCompose(build, clean_up))