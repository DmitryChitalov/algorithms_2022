"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
from hashlib import sha256
from os.path import join, dirname
import csv


class HashClass:
    def __init__(self):
        self.csv_obj = join(dirname(__file__), "logins.csv")
        self.field_names = ["login", "hash_obj"]
        self.logins_dict = {}

    def create_file(self):
        with open(self.csv_obj, mode='w+', encoding='utf-8') as c_file:
            file_writer = csv.DictWriter(c_file,
                                         delimiter=",",
                                         lineterminator="\r",
                                         fieldnames=self.field_names
                                         )
            file_writer.writeheader()

    def write_file(self):
        with open(self.csv_obj, mode='w', encoding='utf-8') as w_file:
            file_writer = csv.DictWriter(w_file,
                                         delimiter=",",
                                         lineterminator="\r",
                                         fieldnames=self.field_names
                                         )
            file_writer.writeheader()
            for key, value in self.logins_dict.items():
                file_writer.writerow({self.field_names[0]: key, self.field_names[1]: value})

    def read_file(self):
        with open(self.csv_obj, mode='r', encoding='utf-8') as r_file:
            file_reader = csv.DictReader(r_file, delimiter=",")
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count != 1:
                    key = row["login"]
                    value = row["hash_obj"]

                    self.logins_dict[key] = value

    @staticmethod
    def get_hash():

        login = input('Введите логин: ')
        passwd = input('Введите пароль: ')
        hash_obj = sha256(login.encode() + passwd.encode()).hexdigest()
        return login, hash_obj

    def register(self):

        login, reg_hash = self.get_hash()

        self.read_file()

        if self.logins_dict.get(login) is not None:
            print("Вы уже есть в файле, выполните вход.")
        else:
            self.logins_dict[login] = reg_hash
            self.write_file()
            print("Операция прошла успешно, вы зарегистрировались.")


    def log_in(self):
        self.read_file()
        login, check_hash = self.get_hash()

        if check_hash == self.logins_dict[login]:
            print("Это Вы!")
        else:
            print("Вы ввели неверный пароль или ещё не регистрировались!")


work = HashClass()
work.create_file()
work.register()
work.log_in()





