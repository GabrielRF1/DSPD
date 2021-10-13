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
        value['_def'] = value['_def'].strip()
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

    a_def = {'_def': definition}
    if len(synonyms) != 0:
        a_def['_synonyms'] = list(set(synonyms))
    if len(antonyms) != 0:
        a_def['antonyms'] = list(set(antonyms))
    if len(extras) != 0:
        a_def['extras'] = list(set(extras))  
    return a_def

def search_for_ext(values):
    result = []
    for value in values:
        to_search = re.compile('^((?!Synonym(s?): |Antonym(s)).)*$')
        try:
            ext = re.search(to_search, value).group()
            result.append(ext.strip())
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

class DictBotFinalItem(scrapy.Item):
    word = scrapy.Field(output_processor = TakeFirst())

    alt = scrapy.Field()
    
    defs = scrapy.Field()

    gender = scrapy.Field(output_processor = TakeFirst())

    word_class = scrapy.Field(output_processor = TakeFirst())

class DictBotIntermediateItem(scrapy.Item):
    word = scrapy.Field(input_processor = Identity(), output_processor = Join(''))

    alt = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = Identity())

    defs = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = MapCompose(build, clean_up))

    gender = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())