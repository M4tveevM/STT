# This code will provide answers to users actions and also, it will
import sqlite3

FILE = 'sql/telegram.sqlite'
con = sqlite3.connect(FILE)


def answ(question, lang):
    cur = con.cursor()
    result = cur.execute(f"SELECT * FROM quest_to_answ where question = {question}").fetchall()
    con.close()
    return result[0][1] if lang == 'en' else result[0][1]
