# Please, work!
import os
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Login_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui', self)
        self.loginUI()
        self.login = ''

    def connect_db(self, request):
        con = sqlite3.connect('airport.db')
        cur = con.cursor()
        result = cur.execute(
            f'''{request}''').fetchall()
        con.close()
        return result

    def check_login(self):
        password = self.password_input.text()
        login = self.login_input.text()
        result_login = self.connect_db(
            f'''SELECT name FROM users where login = "{login}"''')
        result = self.connect_db(
            f'''SELECT name FROM users where login = "{login}" 
            and password = "{password}"''')
        if len(result_login) == 0:
            return 'login error'
        if len(result_login) > 0:
            self.login = login
            return result

    def login(self):
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

    def loginUI(self):
        self.login_submit_btn.clicked.connect(self.login)


def main():
    app = QApplication(sys.argv)
    ex = Login_UI()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
