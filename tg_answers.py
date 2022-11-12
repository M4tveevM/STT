# This code will provide answers to users actions and also, it will
import sqlite3

from tg_const import SQL_FILE


def check_userdata(user_id, task=''):
    con = sqlite3.connect(SQL_FILE)
    result = con.cursor().execute(
        f"SELECT * FROM users where message_chat_id = {user_id}").fetchall()
    con.close()

    if len(result) == 0:
        con = sqlite3.connect(SQL_FILE)
        con.cursor().execute(f"INSERT INTO users(message_chat_id) VALUES({user_id});")
        con.commit()

    if task == 'change_lang':
        con = sqlite3.connect(SQL_FILE)
        result = con.cursor().execute(
            f"SELECT preferred_language FROM users where message_chat_id = {user_id};"
            f"").fetchall()
        con.cursor().execute(f"UPDATE users SET preferred_language ="
                             f" '{'en' if result[0][0] == 'ru' else 'ru'}'"
                             f" WHERE message_chat_id = {user_id};")
        con.commit()
    con.close()

    if task == 'get_lang':
        con = sqlite3.connect(SQL_FILE)
        return con.cursor().execute(
            f"SELECT preferred_language FROM users where message_chat_id = {user_id};").fetchall()
    con.close()


def answ(question, lang):
    con = sqlite3.connect(SQL_FILE)
    cur = con.cursor()
    result = cur.execute(
        f"SELECT answer_en FROM quest_to_answ where question = '{question}'").fetchall() if \
        lang[0][0] == 'en' else cur.execute(
        f"SELECT answer_ru FROM quest_to_answ where question = '{question}'").fetchall()
    con.close()
    return result[0][0]
