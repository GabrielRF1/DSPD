# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

lua_error = "Wiktionary:Lua memory errors"

class DictBotPipeline:
    def process_item(self, item, spider):
        if lua_error  in item['_word'] or lua_error in item['defs']:
            raise DropItem('invalid word or definition found')
        return item
