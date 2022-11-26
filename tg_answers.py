# This code will provide answers to users actions and also, it will
import sqlite3

from tg_const import SQL_FILE


def connect_db(request):
    # Функция, которая упрощает соединение с DB.
    # А, как следствие, уменьшает количество требуемых строчек кода, для реализации
    # запроссов к db.
    try:
        con = sqlite3.connect(SQL_FILE)
        cur = con.cursor()
        result = cur.execute(f'''{request}''').fetchall()
        con.commit()
        con.close()
        return result
    except Exception as ex:
        print(ex)


def create_user(user_id):
    connect_db(f"INSERT INTO tg_auth(message_chat_id, phase) VALUES({user_id}, FALSE)")


def clean_user(user_id):
    connect_db(f"UPDATE users SET tg_message_chat_id = NULL")
    connect_db(f"update tg_auth set phase = False where message_chat_id = {user_id}")


def get_flights(user_id):
    result = connect_db(f'''SELECT flight_id, destination, date, time_in_flight, airline
     FROM flights where flights.airline = (select users.airline from users where
                            tg_message_chat_id = "{user_id}") order by flights.date''')
    answer = []
    for x in result:
        answer.append(' | '.join(x))
    return "Вот рейсы вашей авиакомпании:\n"'\n'.join(answer)


def is_user_in_main_db(user_id):
    if len(connect_db(
            f"SELECT * FROM users where tg_message_chat_id = {user_id}")) > 0:
        return True


def is_user_in_auth_tg(user_id):
    if len(connect_db(
            f"SELECT * FROM tg_auth where message_chat_id = {user_id}")) > 0:
        return True


def user_phase(user_id):
    return connect_db(f"SELECT phase FROM tg_auth where message_chat_id = {user_id}")[0][
        0]


def check_db_rules(login, password):
    if len(login) < 6:
        return "Ошибка: Длинна поля Login не может состоять из < 6 символов!"
    elif len(password) < 8:
        return "Ошибка: Длинна поля Pass не может состоять из < 8 символов!"
    else:
        return True


def try_auth(user_id, message):
    if len(message.split()) > 1:
        login = message.split()[0]
        password = message.split()[1]
        if check_db_rules(login, password):
            if len(connect_db(
                    f"SELECT * FROM users where login = '{login}' and password ="
                    f" '{password}'")) > 0:
                connect_db(
                    f"UPDATE users SET tg_message_chat_id = {user_id} where login ="
                    f" '{login}' and password = '{password}'")
                connect_db(
                    f"update tg_auth set phase = True where message_chat_id = {user_id}")
                return answ('done')
            else:
                if len(connect_db(f"SELECT * FROM users where login = '{login}'")) > 0:
                    return answ('error_password')
                else:
                    return answ('error_login')
        else:
            return check_db_rules(login, password)


def answ(question):
    con = sqlite3.connect(SQL_FILE)
    cur = con.cursor()
    result = cur.execute(
        f"SELECT text FROM tg_answers where question = '{question}'").fetchall()
    con.close()
    return result[0][0]
