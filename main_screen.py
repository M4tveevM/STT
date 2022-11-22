import sqlite3
import sys
import requests
from bs4 import BeautifulSoup
import pymorphy2

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView

morph = pymorphy2.MorphAnalyzer()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.search_btn.clicked.connect(self.show_flight_information)
        self.update_btn.clicked.connect(self.find_flights)
        self.additional_weather.setText(self.get_weather())
        self.welcome_title.setText('Добрый день,  ' + self.connect_db(
            f'SELECT name FROM users WHERE login = "{login}"')[0][0] +
                                   '! Вот список рейсов вашей авиа компании:''')
        self.find_flights()

    def connect_db(self, request):
        con = sqlite3.connect('airport.db')
        cur = con.cursor()
        result = cur.execute(
            f'''{request}''').fetchall()
        con.close()
        return result

    def get_weather(self, city='Таллинн'):
        url = f'https://sinoptik.ua/погода-{city.lower()}'
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
        AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
            'Accept-Language': 'en-US,en;q=0.9'}
        response = requests.get(url, headers=headers)
        bs = BeautifulSoup(response.text, "html.parser")
        try:
            temp = bs.find("p", {
                "class": "today-temp"}).get_text(strip=True)
            description = bs.find("div", {
                "class": "description"}).get_text(strip=True)
            return f"Температура воздуха сейчас {temp}\n{description}"
        except:
            print(f'Город "{city}" не найден.')

    def find_flights(self):
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

    def show_flight_information(self):
        flight = self.search_input.text().upper()
        if len(flight) > 0:
            aircraft_id = self.connect_db(
                f'''SELECT aircraft_id from flights where flight_id = "{flight}"''')
            if aircraft_id:
                destination = self.connect_db(f'''
                SELECT destination from flights where flight_id = "{flight}"''')[0][0]
                self.destination_weather_header.setText(f"Прогноз погоды в {destination}")
                self.destination_weather.setText(self.get_weather(destination))
                aircraft_db_info = self.connect_db(f'''SELECT model, date_of_manufacture, mileage,
                speed, engines, wingspan, height, length FROM aircrafts where aircrafts.id
                 = "{aircraft_id[0][0]}"''')
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


if __name__ == '__main__' and len(sys.argv) == 2:
    login = sys.argv[1]
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
else:
    print("Вы запустили не тот файл. Данный файл должен запускаться только от main.py.")
