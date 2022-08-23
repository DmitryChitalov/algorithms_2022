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


from json import dump, load
from hashlib import sha256
from datetime import datetime
from re import search


class DataBaseClass:
    id = 0

    def __init__(self):
        with open('database_file.json', 'w', encoding='utf-8') as w_file:
            dump({}, w_file)

    @staticmethod
    def _birthday():
        b_day = input('Введите дату рождения (в формате ДД.ММ.ГГГГ): ')
        b_day = datetime.strptime(b_day, '%d.%m.%Y').date()
        today = datetime.now().date()
        if (today.year - b_day.year - ((today.month, today.day) < (b_day.month, b_day.day))) < 14:
            return False, b_day
        return True, b_day

    @staticmethod
    def _input_login():
        login = input('Введите логин: ').lower()

        with open('database_file.json', 'r', encoding='utf-8') as r_file:
            db_dict = load(r_file)

        if db_dict.get(login):
            return False, login
        return True, login

    @staticmethod
    def _input_password():
        password = input('Введите пароль (буквы верхнего, нижнего регистра и цифры): ')
        if len(password) >= 8 and search(r'[a-z]', password) and \
                search(r'[A-Z]', password) and search(r'[0-9]', password):
            return True, password
        return False, password

    def registration(self):
        print('-----Регистрация-----')

        b_day = self._birthday()
        if not b_day[0]:
            print('Мы не можем Вас зарегистрировать. Попробуйте позже')
            return 0

        login = self._input_login()
        if login[0]:
            password = self._input_password()
            if password[0]:
                password = sha256(login[1].encode() + password[1].encode()).hexdigest()

                DataBaseClass.id += 1
                surname, name = input('Введите фамилию и имя: ').split()

                with open('database_file.json', 'r', encoding='utf-8') as r_file:
                    db_dict = load(r_file)
                    db_dict.setdefault(login[1], {'_id': DataBaseClass.id, '_surname': surname, '_name': name,
                                                  'birthday': str(b_day[1]), 'password': password})

                with open('database_file.json', 'w', encoding='utf-8') as w_file:
                    dump(db_dict, w_file, sort_keys=True, indent=4, ensure_ascii=False)

            else:
                print(f'Пароль {password[1]} не соответствует требованиям. Придумайте другой')
                self.registration()
        else:
            print(f'Вы ввели {login[1]}. Такое имя пользователя существует. Придумайте другой')
            self.registration()

    @staticmethod
    def authorization(login, password):
        with open('database_file.json', 'r', encoding='utf-8') as r_file:
            db_dict = load(r_file)

        if db_dict.get(login):
            if sha256(login.encode() + password.encode()).hexdigest() == db_dict[login]['password']:
                print('Вы успешно авторизованы')
                return 1
        print('Неправильно введен логин/пароль')
        return 0
