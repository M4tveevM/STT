# Please, work!
# imports
import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QApplication, \
    QMainWindow
from PyQt5 import uic

last_user = ''


class Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login_ui.ui', self)
        self.initUI()

    def check_login(self):
        # global last_user
        password = self.password_input.text()
        login = self.login_input.text()
        con = sqlite3.connect('login.db')
        cur = con.cursor()
        result_login = cur.execute(
            f'''SELECT name FROM users where login = "{login}"''').fetchall()
        result = cur.execute(
            f'''SELECT name FROM users where login = "{login}" and password = "{password}"
            ''').fetchall()
        con.close()
        if len(result_login) == 0:
            return 'login'
        if len(result_login) > 0:
            # last_user = login
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
            if self.check_login() == 'login':
                self.error_box.setText('Такого login нет в системе.'
                                       '\nПроверьте правильность написания.')
            elif len(self.check_login()) == 0:
                self.error_box.setText('Ошибка: не верный пароль.'
                                       '\nПроверьте введенный пароль.')
            else:
                self.error_box.setText(f'Добрый день,  {self.check_login()[0][0]}\n'
                                       f'Загружаю базу перелётов.')
            self.password_input.setText('')

    def initUI(self):
        self.login_submit_btn.clicked.connect(self.login)
        self.login_input.setText(last_user)


def main():
    app = QApplication(sys.argv)
    ex = Ui()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
