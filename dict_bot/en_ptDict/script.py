import sqlite3

con = sqlite3.connect("dict_bot\\en_ptDict\\en_ptDict.db")
cur = con.cursor()
cur.execute("""
            SELECT word_id, word FROM Word WHERE word LIKE '%.%' or word LIKE '%·%';
            """)
records = cur.fetchall()

for row in records:
    word = str(row[1])
    new_word = word.replace('.', '').replace('·', '')
    cur.execute("""UPDATE Word set word=? WHERE word_id=?""",(new_word, row[0]))
    print (new_word)
    print('\n')
con.commit()

cur.close()