import sqlite3
import sys
import requests
from bs4 import BeautifulSoup
import pymorphy2

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTextBrowser

morph = pymorphy2.MorphAnalyzer()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.additional_weather.setText(self.get_weather())
        self.welcome_title.setText('Добрый день, ' + self.connect_db(
            f"SELECT name FROM users WHERE login = '{login}'")[0][0] +
                                   ', выберите рейс для просмотра информации о нём.''')
        self.find_flights()

    def connect_db(self, request):
        con = sqlite3.connect('login.db')
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
        con = sqlite3.connect('login.db')
        cur = con.cursor()
        result = cur.execute(
            f'''SELECT destination, date, time_in_flight, airline FROM flights where
             flights.airline = (select users.airline from users where login = "{login}"
             )''').fetchall()
        self.airline_flights.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        else:
            self.statusBar().showMessage(f"Найдено {len(result)}" +
                                         morph.parse('рейс')[0].make_agree_with_number(
                                             len(result)).word + " вашей авиакомпании")
        self.airline_flights.setColumnCount(len(result[0]))
        airline_table_tooltips = ["Пункт назначения", "Дата и время вылета",
                                  "Время в пути", "Авиакомпания"]
        for elem in range(4):
            self.airline_flights.horizontalHeaderItem(elem).setToolTip(
                airline_table_tooltips[elem])
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.airline_flights.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__' and len(sys.argv) > 1:
    login = sys.argv[1]
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
else:
    print(
        'Вы запустили не тот файл. Данный файл должен запускаться отлько от main.py')
