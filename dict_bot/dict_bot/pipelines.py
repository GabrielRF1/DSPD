# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import sqlite3

lua_error = "Wiktionary:Lua memory errors"
add_translation_error = "rfdef"

class DictBotPipeline:
    def process_item(self, item, spider):
        # ------------------ error checking ------------------
        if lua_error  in item["word"]:
            raise DropItem('invalid word found')
        
        for defs in item["defs"]:
            if lua_error in defs["_def"] or add_translation_error in defs["_def"]:
                raise DropItem('invalid definition found')
        # ------------------ ------------------ ------------------
        # ------ removing possible non-extras or duplicates from extras --------
        for defs in item["defs"]:
            to_remove_from_extras = []
            try:
                for extra in defs["extras"]:
                    for definitions in item["defs"]:
                        if extra == definitions["_def"]:
                            to_remove_from_extras.append(extra)
                        try:
                            if extra in definitions["extras"] and defs != definitions:
                                to_remove_from_extras.append(extra)
                        except:
                            pass
                for to_remove in to_remove_from_extras:
                    defs["extras"].remove(to_remove)
                if len(defs["extras"]) == 0:
                    defs.pop("extras")
            except: # no extras in this definition
                continue
        # ------------------ ------------------ ------------------
        return item

class DictBotSQLitePipeline:
    @classmethod
    def from_crawler(cls, crawler):
        db_name = getattr(crawler.spider, 'db_name')
        return cls(db_name)

    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name + ".db")
        self.cur = self.con.cursor()
        self.create_db()
    
    def create_db(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Extension(
        extension TEXT NOT NULL PRIMARY KEY
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Word(
        word_id INTEGER PRIMARY KEY,
        word TEXT NOT NULL,
        word_class TEXT NOT NULL,
        gender text
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Definition(
        def_id INTEGER PRIMARY KEY,
        def TEXT NOT NULL,
        word_id INTEGER NOT NULL,
        FOREIGN KEY(word_id) REFERENCES Word(word_id)
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Alternative(
        word_id INTEGER NOT NULL,
        extension TEXT NOT NULL,
        FOREIGN KEY(word_id) REFERENCES Word(word_id),
        FOREIGN KEY(extension) REFERENCES Extension(extension),
        PRIMARY KEY(word_id, extension)
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Synonym(
        def_id INTEGER NOT NULL,
        extension TEXT NOT NULL,
        FOREIGN KEY(def_id) REFERENCES Definition(def_id),
        FOREIGN KEY(extension) REFERENCES Extension(extension),
        PRIMARY KEY(def_id, extension)
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Antonym(
        def_id INTEGER NOT NULL,
        extension TEXT NOT NULL,
        FOREIGN KEY(def_id) REFERENCES Definition(def_id),
        FOREIGN KEY(extension) REFERENCES Extension(extension),
        PRIMARY KEY(def_id, extension)
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Extra(
        def_id INTEGER NOT NULL,
        extension TEXT NOT NULL,
        FOREIGN KEY(def_id) REFERENCES Definition(def_id),
        FOREIGN KEY(extension) REFERENCES Extension(extension),
        PRIMARY KEY(def_id, extension)
        )""")
        

    def process_item(self, item, spider):
        try:
            gender = item["gender"]
        except:
            gender = ""
        self.cur.execute("""INSERT OR IGNORE INTO Word(word, word_class, gender) VALUES (?, ?, ?)""",
            (item["word"], item["word_class"], gender))
        word_id = self.cur.lastrowid
        try:
            for alt in item["alt"]:
                self.cur.execute("""INSERT OR IGNORE INTO Extension VALUES (?)""",
                    (alt,))
                self.cur.execute("""INSERT OR IGNORE INTO Alternative VALUES (?, ?)""",
                    (word_id, alt))
        except:
            pass
        for defs in item["defs"]:
            self.cur.execute("""INSERT OR IGNORE INTO Definition(def, word_id) VALUES (?, ?)""",
            (defs["_def"], word_id))
            def_id = self.cur.lastrowid
            try:
                for syn in defs["_synonyms"]:
                    self.cur.execute("""INSERT OR IGNORE INTO Extension VALUES (?)""",
                        (syn,))
                    self.cur.execute("""INSERT OR IGNORE INTO Synonym VALUES (?, ?)""",
                        (def_id, syn))
            except:
                pass
            try:
                for ant in defs["antonyms"]:
                    self.cur.execute("""INSERT OR IGNORE INTO Extension VALUES (?)""",
                        (ant,))
                    self.cur.execute("""INSERT OR IGNORE INTO Antonym VALUES (?, ?)""",
                        (def_id, ant))
            except:
                pass
            try:
                for ext in defs["extras"]:
                    self.cur.execute("""INSERT OR IGNORE INTO Extension VALUES (?)""",
                        (ext,))
                    self.cur.execute("""INSERT OR IGNORE INTO Extra VALUES (?, ?)""",
                        (def_id, ext))
            except:
                pass
        self.con.commit()
        return item

