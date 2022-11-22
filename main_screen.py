# --- <imports> ---
import sqlite3
import sys
import requests
from bs4 import BeautifulSoup
import pymorphy2

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtWidgets

# --- </imports> ---


# Вывод метода анализа текста, для удобного использования в коде.

morph = pymorphy2.MorphAnalyzer()


# Класс основного окна
class MainWindow(QMainWindow):
    def setupUi(self):
        # Основной экран

        self.setObjectName("MainWindow")
        self.resize(970, 540)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(580, 10, 381, 231))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.main_weather_header = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.main_weather_header.setMaximumSize(QtCore.QSize(16777215, 20))
        self.main_weather_header.setObjectName("main_weather_header")
        self.verticalLayout_3.addWidget(self.main_weather_header)
        self.main_weather_info = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.main_weather_info.setMaximumSize(QtCore.QSize(16777215, 30))
        self.main_weather_info.setObjectName("main_weather_info")
        self.verticalLayout_3.addWidget(self.main_weather_info)
        self.additional_weather = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.additional_weather.setObjectName("additional_weather")
        self.verticalLayout_3.addWidget(self.additional_weather)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(580, 250, 381, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.destination_weather_header = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.destination_weather_header.setMaximumSize(QtCore.QSize(16777215, 20))
        self.destination_weather_header.setObjectName("destination_weather_header")
        self.verticalLayout_4.addWidget(self.destination_weather_header)
        self.destination_weather_info = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.destination_weather_info.setMaximumSize(QtCore.QSize(16777215, 30))
        self.destination_weather_info.setObjectName("destination_weather_info")
        self.verticalLayout_4.addWidget(self.destination_weather_info)
        self.destination_weather = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.destination_weather.setObjectName("destination_weather")
        self.verticalLayout_4.addWidget(self.destination_weather)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcome_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.welcome_title.setMaximumSize(QtCore.QSize(16777215, 20))
        self.welcome_title.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.welcome_title.setObjectName("welcome_title")
        self.verticalLayout.addWidget(self.welcome_title)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 240, 571, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(560, 0, 20, 511))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 461, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.airline_flights = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.airline_flights.setObjectName("airline_flights")
        self.airline_flights.setColumnCount(0)
        self.airline_flights.setRowCount(0)
        self.verticalLayout_2.addWidget(self.airline_flights)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 280, 461, 201))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.aircraft_information = QtWidgets.QTableWidget(self.verticalLayoutWidget_5)
        self.aircraft_information.setObjectName("aircraft_information")
        self.aircraft_information.setColumnCount(0)
        self.aircraft_information.setRowCount(0)
        self.verticalLayout_5.addWidget(self.aircraft_information)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(480, 120, 81, 41))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.update_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.update_btn.setObjectName("update_btn")
        self.verticalLayout_6.addWidget(self.update_btn)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 281, 16))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(480, 280, 81, 121))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.search_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.search_input.setObjectName("search_input")
        self.verticalLayout_7.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.search_btn.setObjectName("search_btn")
        self.verticalLayout_7.addWidget(self.search_btn)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "UpdatingSpace / SmartTimeTable"))
        self.main_weather_header.setText(_translate("MainWindow", "Погода Tallinn:"))
        self.main_weather_info.setText(_translate("MainWindow", "Прогноз на сегодня:"))
        self.destination_weather_header.setText(
            _translate("MainWindow", "Погода в пункте назначения:"))
        self.destination_weather_info.setText(
            _translate("MainWindow", "Прогноз на сегодня:"))
        self.welcome_title.setText(
            _translate("MainWindow", "Добрый день, user. Вот список рейсов вашей авиа\n"
                                     "компании:"))
        self.update_btn.setText(_translate("MainWindow", "Обновить"))
        self.label_2.setText(_translate("MainWindow", "Информация о самолёте:"))
        self.label.setText(_translate("MainWindow", "Рейс:"))
        self.search_btn.setText(_translate("MainWindow", "Искать"))

    def __init__(self):
        # инициализация UI

        super().__init__()
        self.setupUi()
        self.search_btn.clicked.connect(self.show_flight_information)
        self.update_btn.clicked.connect(self.find_flights)
        self.additional_weather.setText(self.get_weather())
        self.welcome_title.setText('Добрый день,  ' + self.connect_db(
            f'SELECT name FROM users WHERE login = "{login}"')[0][0] +
                                   '! Вот список рейсов вашей авиа компании:''')
        self.find_flights()

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

    def get_weather(self, city='Таллинн'):
        # Функция поиска погоды по параметру city.

        try:
            url = f'https://sinoptik.ua/погода-{city.lower()}'
            headers = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
            AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                'Accept-Language': 'en-US,en;q=0.9'}
            response = requests.get(url, headers=headers)
            bs = BeautifulSoup(response.text, "html.parser")
        except:
            return 'Ну удаётся подключится к сайту. Проверьте соединение с интернетом \n' \
                   'Но а так же проверьте не заблокирован ли сайт https://sinoptik.ua/' \
                   'в вашей стране.'
        try:
            temp = bs.find("p", {
                "class": "today-temp"}).get_text(strip=True)
            description = bs.find("div", {
                "class": "description"}).get_text(strip=True)
        except:
            return f'Город "{city}" не найден. Либо отсутствует соединение с интернетом'
        return f"Температура воздуха сейчас {temp}\n{description}"

    def find_flights(self):
        # Функция нахождения рейсов авикомпании user'a.

        result = self.connect_db(
            f'''SELECT flight_id, destination, date, time_in_flight, airline FROM flights 
            where flights.airline = (select users.airline from users where login =
            "{login}") order by flights.date''')
        if not result:
            self.statusBar().showMessage(
                'К сожалению, рейсы вашей авиа компании не найдены')
            return
        else:
            self.statusBar().showMessage(f"Найдено {len(result)}" +
                                         morph.parse('рейс')[0].make_agree_with_number(
                                             len(result)).word + "  вашей авиакомпании")
        self.airline_flights.setColumnCount(len(result[0]))
        self.airline_flights.setRowCount(len(result))
        self.airline_flights.setHorizontalHeaderLabels(
            ["Номер рейса", "Пункт назначения", "Дата и время вылета", "Время в пути",
             "Авиакомпания"])

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.airline_flights.setItem(i, j, QTableWidgetItem(str(val)))
        self.airline_flights.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.airline_flights.horizontalHeader().setMinimumSectionSize(0)

        # Обновление показаний погоды(на случай если до этого не было интернета)
        self.additional_weather.setText(self.get_weather())

    def show_flight_information(self):
        # функция выдающая информацию о самолёте из рейса.
        # А так же показывающая погоду основываясь на destanation рейса.

        flight = self.search_input.text().upper()
        if flight:
            aircraft_id = self.connect_db(
                f'''SELECT aircraft_id from flights where flight_id = "{flight}"''')
            if aircraft_id:
                destination = self.connect_db(f'''
                SELECT destination from flights where flight_id = "{flight}"''')[0][0]
                self.destination_weather_header.setText(f"Прогноз погоды в {destination}")
                self.destination_weather.setText(self.get_weather(destination))
                aircraft_db_info = self.connect_db(f'''SELECT model, date_of_manufacture,
                mileage, speed, engines, wingspan, height, length FROM aircrafts where 
                aircrafts.id = "{aircraft_id[0][0]}"''')
                self.aircraft_information.setRowCount(len(aircraft_db_info))
                self.statusBar().showMessage(f"Загружаю данные по рейсу {flight}")
                self.aircraft_information.setColumnCount(len(aircraft_db_info[0]))
                self.aircraft_information.setHorizontalHeaderLabels(
                    ["Модель", "Дата начала эксплуатации", "Пробег (miles)",
                     "Круизная скорость",
                     "Двигатели", "размах крыльев", "Высота", "Ширина"])
                for i, elem in enumerate(aircraft_db_info):
                    for j, val in enumerate(elem):
                        self.aircraft_information.setItem(i, j,
                                                          QTableWidgetItem(str(val)))
                self.aircraft_information.horizontalHeader().setSectionResizeMode(
                    QHeaderView.ResizeToContents)
                self.aircraft_information.horizontalHeader().setMinimumSectionSize(0)
            else:
                self.statusBar().showMessage("Рейс не найден")
        else:
            self.statusBar().showMessage("Поле поиска не может оставаться пустым!")

        # Обновление показаний погоды(на случай если до этого не было интернета)
        self.additional_weather.setText(self.get_weather())


if __name__ == '__main__' and len(sys.argv) == 2:
    # Запуск файла.
    # А так же защита от самопроизвольного запуска пользователя
    # (с его обходом авторизации через login.ui)

    login = sys.argv[1]
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
else:
    print("Вы запустили не тот файл. Данный файл должен запускаться только от main.py.")
