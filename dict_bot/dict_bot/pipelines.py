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
        # ------------------ Lua error checking ------------------
        if lua_error  in item["_word"]:
            raise DropItem('invalid word found')
        
        for defs in item["defs"]:
            if lua_error in defs["_def"]:
                raise DropItem('invalid definition found')
        # ------------------ ------------------ ------------------

        # ------ removing possible non-extras from extras --------
        for defs in item["defs"]:
            to_remove_from_extras = []
            for extra in defs["extras"]:
                for definitions in item["defs"]:
                    if extra == definitions["_def"]:
                        to_remove_from_extras.append(extra)
            for to_remove in to_remove_from_extras:
                defs["extras"].remove(to_remove)
        # ------------------ ------------------ ------------------

        #------------------- Insert into SQlite -------------------
        
        #------------------- ------------------ -------------------

        return item
