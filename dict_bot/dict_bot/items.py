# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

class DictBotItem(scrapy.Item):
    # define the fields for your item here like:
    word = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    alt = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    defs = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    gender = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    synonyms = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    antonyms = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    word_class = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    extras = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())

    pass
