# Please, work!
import os
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


# Класс окна ввода логина и пароля
class Login_UI(QMainWindow):

    def setupUi(self):
        # загрузка ui

        self.setObjectName("LoginWindow")
        self.resize(300, 350)
        self.setMaximumSize(QtCore.QSize(300, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 261, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.aircraft_logo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.aircraft_logo.setText("")
        self.aircraft_logo.setPixmap(QtGui.QPixmap("img/Delta-A350.png"))
        self.aircraft_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.aircraft_logo.setObjectName("aircraft_logo")
        self.verticalLayout_4.addWidget(self.aircraft_logo)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 110, 62, 46))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Login = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Login.setObjectName("Login")
        self.verticalLayout_5.addWidget(self.Login)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(80, 110, 201, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.login_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.login_input.setMaxLength(30)
        self.login_input.setObjectName("login_input")
        self.verticalLayout_6.addWidget(self.login_input)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(80, 155, 201, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.password_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.password_input.setMaxLength(30)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.verticalLayout_7.addWidget(self.password_input)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 160, 62, 46))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Pass = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.Pass.setObjectName("Pass")
        self.verticalLayout_8.addWidget(self.Pass)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 210, 261, 41))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.error_box = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.error_box.setText("")
        self.error_box.setObjectName("error_box")
        self.verticalLayout_9.addWidget(self.error_box)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(90, 260, 101, 31))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.login_submit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.login_submit_btn.setObjectName("login_submit_btn")
        self.verticalLayout_10.addWidget(self.login_submit_btn)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionMain = QtWidgets.QAction(self)
        self.actionMain.setObjectName("actionMain")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Авторизация"))
        self.Login.setText(_translate("LoginWindow", "Login:"))
        self.Pass.setText(_translate("LoginWindow", "Pass:"))
        self.login_submit_btn.setText(_translate("LoginWindow", "Login"))
        self.actionMain.setText(_translate("LoginWindow", "Main"))

    def connect_db(self, request):
        # Функция, которая упрощает соединение с ДБ.
        # А, как следствие, уменьшает количество требуемых строчек кода, для реализации
        # запроссов к бд.

        try:
            con = sqlite3.connect('airport.db')
            cur = con.cursor()
            result = cur.execute(
                f'''{request}''').fetchall()
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

    def login_pass_checking(self):
        # функция проверяющая логин и пароль по правилу.

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

    def __init__(self):
        # инициализация ui интерфейса.

        super().__init__()
        self.setupUi()
        self.login = ''
        self.login_submit_btn.clicked.connect(self.login_pass_checking)


def main():
    app = QApplication(sys.argv)
    ex = Login_UI()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
