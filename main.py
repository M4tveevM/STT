# Please, work!
import os
import sqlite3
import sys
import random
import asyncio
import time

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


# Класс окна ввода логина и пароля
class Login_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui', self)
        self.login = ''
        self.login_submit_btn.clicked.connect(self.login_pass_checking)
        self.registration_submit_btn.clicked.connect(self.registration_checking)

    def connect_db(self, request):
        # Функция, которая упрощает соединение с DB.
        # А, как следствие, уменьшает количество требуемых строчек кода, для реализации
        # запроссов к db.
        try:
            con = sqlite3.connect('airport.db')
            cur = con.cursor()
            result = cur.execute(f'''{request}''').fetchall()
            con.commit()
            con.close()
            return result
        except:
            print('Произошла ошибка при подключении к БД. '
                  'Проверьте имеется ли файл airport.db в папке с файлом. \n'
                  'А так же проверьте не допустили ли вы ошибку в структуре БД.')

    def check_login(self):
        # Функция, которая проверяет правильность ввода логина и пароля user'a в бд.
        # А так же она проверяет имется ли введенный в программе логин
        # или отсутствует в бд.

        password = self.password_input.text()
        login = self.login_input.text()
        result_login = self.connect_db(
            f'''SELECT name FROM users where login = "{login}"''')
        result = self.connect_db(
            f'''SELECT name FROM users where login = "{login}" 
            and password = "{password}"''')
        if len(result_login) == 0:
            return 'login error'
        elif result_login:
            self.login = login
            return result

    def check_db_rules(self):
        if len(self.login_input.text()) == 0:
            self.error_box.setText(
                "Ошибка: Поле Логина(Login)\n не как не может быть пустым!")
        elif len(self.password_input.text()) == 0:
            self.error_box.setText(
                "Ошибка: Поле Пароля(Pass)\n не как не может быть пустым!")
        elif len(self.login_input.text()) < 6:
            self.error_box.setText(
                "Ошибка: Длинна поля Login\n не может состоять из < 6 символов!")
        elif len(self.password_input.text()) < 8:
            self.error_box.setText(
                "Ошибка: Длинна поля Pass\n не может состоять из < 8 символов!")
        else:
            return True

    def login_pass_checking(self):
        # функция проверяющая логин и пароль по правилу.
        print(self.check_db_rules())
        if self.check_db_rules():
            self.error_box.setText('Сверяю данные с БД')
            if self.check_login() == 'login error':
                self.error_box.setText('Такого login нет в системе.'
                                       '\nПроверьте правильность написания.')
            elif len(self.check_login()) == 0:
                self.error_box.setText('Ошибка: не верный пароль.'
                                       '\nПроверьте введенный пароль.')
            else:
                self.error_box.setText(f'Добрый день,  {self.check_login()[0][0]}\n'
                                       f'Загружаю базу перелётов.')
                os.system(f'python main_screen.py {self.login}')
            self.password_input.setText('')

    def registration_checking(self):
        password = self.password_input.text()
        login = self.login_input.text()
        if self.check_db_rules():
            if len(self.connect_db(
                    f'''SELECT * FROM users where password = "{password}" 
                    and login = "{login}"''')) > 0:
                self.error_box.setText(
                    "Данный аккаунт уже зарегистрирован\nНажмите на кнопку sign in.")
            elif len(self.connect_db(
                    f'''SELECT * FROM users where login = "{login}"''')) > 0:
                self.error_box.setText(
                    f'Данный логин уже используется другим пользователем,'
                    f'\nпопробуйте ввести другой.')
            elif len(self.connect_db(
                    f'''SELECT login FROM users where password = "{password}"''')) > 0:
                self.error_box.setText("Данный пароль уже используется \nпользователем " +
                                       self.connect_db(f'''SELECT login FROM users where 
                                       password = "{password}"''')[0][0] + ".")
            else:
                try:
                    approved_aircompany = random.choice([x[0] for x in self.connect_db(
                        '''select airline from flights GROUP BY airline''')])
                    self.connect_db(f'''INSERT INTO users (name, login, password, airline)
                                        VALUES ('Agent', '{login}', '{password}', 
                                        '{approved_aircompany}')''')
                    self.error_box.setText(
                        f'Акакаунт создан, вас приняли в:\n{approved_aircompany}')
                except:
                    print('Error DB creating account')


def main():
    app = QApplication(sys.argv)
    ex = Login_UI()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
