import sys

import difflib  # библеотека сравнивающая что либо
import re  # библеотека регулярных выражений
import csv  # библеотека работы с csv фаилами
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_00 import Main_Start
from ui_01 import Authorization
from ui_02 import Registration
from ui_03 import Ui_Dialog


class Start(QMainWindow, Main_Start):
    def __init__(self):
        super().__init__()
        self.setupUi1(self)
        self.btn.clicked.connect(self.toAuth)

    def toAuth(self):
        widget.setCurrentWidget(widget_Authorization)  # переход на следующий экран


class MyWidget_A(QMainWindow, Authorization):  # авторизация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.reg.clicked.connect(self.toReg)

        self.log_in.clicked.connect(self.check_pas)

    def check_pas(self):
        emails = []
        names = []
        surnames = []
        logins = []
        passwords = []
        ages = []
        genders = []
        with open('users.csv', encoding='utf-8') as csvfile:  # получение данныхи из csv файли для дальнейшего сравнивания
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                names.append(row['name'])
                surnames.append(row['surname'])
                ages.append(row['age'])
                genders.append(row['gender'])
                emails.append(row['email'])
                logins.append(row['login'])
                passwords.append(row['password'])

        login = str(self.login.text())
        password = str(self.login.text())
        if login in logins and password in passwords:  # сравнивание введеных пользователем данных и имющихся в базе
            widget.setFixedWidth(900)
            widget.setFixedHeight(500)
            widget.setCurrentWidget(widget_Sravni)

    def toReg(self):

        widget.setCurrentWidget(widget_Registration)


class MyWidget_R(QMainWindow, Registration):  # регстрация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.reg_2.clicked.connect(self.toReg)

    def toReg(self):
        self.error_txt.setText("")
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  # создание регулярного выражения
        email = self.Email.text()
        name = self.name.text()
        surname = self.surname.text()
        login = self.login.text()
        password = self.password.text()
        age = self.spinBox.value()
        gender = str(self.man.text()) if self.man.isChecked() == True else str(self.woman.text())

        emails = ["email"]
        names = ["name"]
        surnames = ["surname"]
        logins = ["login"]
        passwords = ["password"]
        ages = ["age"]
        genders = ["gender"]
        if not re.fullmatch(regex, email):  # проверка верности введной почты через регулярное вырадение
            self.error_txt.setText("Неверно указаная почта")
        if name == "Имя" and name <= 2 or name == "":  # проверка введеного имени
            self.error_txt.setText("Ввeдите совё имя")
        if surname == "Фамилия" or surname == "":  # проверка введеной фамилии
            self.error_txt.setText("Ввeдите свою фамилию")
        if age == 0:  # проверка введнного возроста
            self.error_txt.setText("Ввeдите свой возраст")
        if self.error_txt.text() == "":
            with open('users.csv', encoding='utf-8') as csvfile:   # получение данных пользователей
                reader = csv.DictReader(csvfile, delimiter=";")
                for row in reader:
                    names.append(row['name'])
                    surnames.append(row['surname'])
                    ages.append(row['age'])
                    genders.append(row['gender'])
                    emails.append(row['email'])
                    logins.append(row['login'])
                    passwords.append(row['password'])

            if email in emails:  # сравнение имеется ли такая почта у пользователя
                self.error_txt.setText("Данная почта уже указана")
            if login in logins:  # проверка на существующий логин
                self.error_txt.setText("Такой логин уже существует")
            if login == "Логин" or login == "":  # проверка введеного имени
                self.error_txt.setText("Ввeдите совё имя")
            if password == "Пароль" or password == "":  # проверка введеной фамилии
                self.error_txt.setText("Ввeдите свою фамилию")

            if self.error_txt.text() == "":  # проверка отсутсвия ошибки
                data = []
                names.append(name)
                surnames.append(surname)
                ages.append(age)
                genders.append(gender)
                emails.append(email)
                logins.append(login)
                passwords.append(password)
                for i in range(len(names)):
                    data.append([names[i], surnames[i], str(ages[i]), genders[i], emails[i], logins[i], passwords[i]])

                with open('users.csv', mode="w", encoding='utf-8') as csvfile:  # запись новых данных пользователя
                    writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
                    for i in data:
                        writer.writerow(i)
                widget.setCurrentWidget(widget_Authorization)


class Sravni(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.pusk()

    def pusk(self):
        self.setupUi(self)
        self.btn.clicked.connect(self.sravni)

    def sravni(self):
        str1 = self.str1.toPlainText()
        str2 = self.str2.toPlainText()  # считвание первого и втого текста

        y = difflib.SequenceMatcher(None, str1.lower(), str2.lower()).ratio() * 100  # сравнение двух текстов
        if self.Porog.value():
            if int(self.Porog.value()) >= round(y, 2):  # сравниванеи схожести и порга
                self.label_3.setText(f"Текст похож на {round(y, 2)}%")
                self.label_3.setStyleSheet('QLabel {background-color: green;'
                                           'color: white;'
                                           'border-radius: 5px;}')
            else:
                self.label_3.setText(f"Текст похож на {round(y, 2)}%")
                self.label_3.setStyleSheet('QLabel {background-color: red;'
                                           'color: white;'
                                           'border-radius: 5px;}')
        else:
            self.label_3.setText("Введите порог сравнения")
            self.label_3.setStyleSheet('QLabel {background-color: red;'
                                       'color: white;'
                                       'border-radius: 5px;')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    widget_Start = Start()
    widget_Authorization = MyWidget_A()
    widget_Registration = MyWidget_R()
    widget_Sravni = Sravni()

    widget.addWidget(widget_Start)
    widget.addWidget(widget_Authorization)
    widget.addWidget(widget_Registration)
    widget.addWidget(widget_Sravni)

    widget.setFixedWidth(400)
    widget.setFixedHeight(350)
    widget.show()
    sys.exit(app.exec_())
