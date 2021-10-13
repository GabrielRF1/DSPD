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
        # ------ removing possible non-extras from extras --------
        for defs in item["defs"]:
            to_remove_from_extras = []
            try:
                for extra in defs["extras"]:
                    for definitions in item["defs"]:
                        if extra == definitions["_def"]:
                            to_remove_from_extras.append(extra)
                for to_remove in to_remove_from_extras:
                    defs["extras"].remove(to_remove)
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
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Word(
        word_id TEXT PRIMARY KEY,
        word TEXT NOT NULL,
        word_class TEXT NOT NULL,
        gender VARCHAR(1)
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS AlternativeForm(
        alt TEXT NOT NULL PRIMARY KEY
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Word_Alt(
        word_id TEXT NOT NULL,
        alt TEXT NOT NULL,
        FOREIGN KEY(word_id) REFERENCES Word(word_id),
        FOREIGN KEY(alt) REFERENCES AlternativeForm(alt),
        PRIMARY KEY(word_id, alt)
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Definition(
        def_id TEXT PRIMARY KEY,
        def TEXT NOT NULL,
        word_id TEXT NOT NULL,
        FOREIGN KEY(word_id) REFERENCES Word(word_id)
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Synonym(
        syn TEXT NOT NULL PRIMARY KEY
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Antonym(
        ant TEXT NOT NULL PRIMARY KEY
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Extra(
        ext TEXT NOT NULL PRIMARY KEY
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Def_Syn(
        def_id TEXT NOT NULL,
        syn TEXT NOT NULL,
        FOREIGN KEY(def_id) REFERENCES Definition(def_id),
        FOREIGN KEY(syn) REFERENCES Synonym(syn),
        PRIMARY KEY(def_id, syn)
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Def_Ant(
        def_id TEXT NOT NULL,
        ant TEXT NOT NULL,
        FOREIGN KEY(def_id) REFERENCES Definition(def_id),
        FOREIGN KEY(ant) REFERENCES Antonym(ant),
        PRIMARY KEY(def_id, ant)
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Def_Ext(
        def_id TEXT NOT NULL,
        ext TEXT NOT NULL,
        FOREIGN KEY(def_id) REFERENCES Definition(def_id),
        FOREIGN KEY(ext) REFERENCES Extra(ext),
        PRIMARY KEY(def_id, ext)
        )""")
        

    def process_item(self, item, spider):
        word_id = item["word"]+"_"+item["word_class"]
        try:
            gender = item["gender"]
        except:
            gender = ""
        self.cur.execute("""INSERT OR IGNORE INTO Word VALUES (?, ?, ?, ?)""",
            (word_id, item["word"], item["word_class"], gender))

        try:
            for alt in item["alt"]:
                self.cur.execute("""INSERT OR IGNORE INTO AlternativeForm VALUES (?)""",
                    (alt,))
                self.cur.execute("""INSERT OR IGNORE INTO Word_Alt VALUES (?, ?)""",
                    (word_id, alt))
        except:
            pass
        count = 0
        for defs in item["defs"]:
            count = count+1
            def_id = str(count) + word_id
            self.cur.execute("""INSERT OR IGNORE INTO Definition VALUES (?, ?, ?)""",
            (def_id, defs["_def"], word_id))
            try:
                for syn in defs["_synonyms"]:
                    self.cur.execute("""INSERT OR IGNORE INTO Synonym VALUES (?)""",
                        (syn,))
                    self.cur.execute("""INSERT OR IGNORE INTO Def_Syn VALUES (?, ?)""",
                        (def_id, syn))
            except:
                pass
            try:
                for ant in defs["antonyms"]:
                    self.cur.execute("""INSERT OR IGNORE INTO Antonym VALUES (?)""",
                        (ant,))
                    self.cur.execute("""INSERT OR IGNORE INTO Def_Ant VALUES (?, ?)""",
                        (def_id, ant))
            except:
                pass
            try:
                for ext in defs["extras"]:
                    self.cur.execute("""INSERT OR IGNORE INTO Extra VALUES (?)""",
                        (ext,))
                    self.cur.execute("""INSERT OR IGNORE INTO Def_Ext VALUES (?, ?)""",
                        (def_id, ext))
            except:
                pass
        self.con.commit()
        return item

