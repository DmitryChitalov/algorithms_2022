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
from sqlite3 import connect, OperationalError, IntegrityError
from hashlib import sha256
from os.path import join, dirname

# Решееие с использованием базы sqlite.
class HashClass:
    def __init__(self):
        self.db_obj = join(dirname(__file__), 'DB_Hash')
        self.conn = connect(self.db_obj)
        self.crs = self.conn.cursor()

    def create_table(self):
        create_stmt = "CREATE TABLE user_info(user_login varchar(255) unique, user_password varchar(255));"
        try:
            self.crs.execute(create_stmt)
        except OperationalError:
            print('Таблица уже есть! Не создаём её.')
        else:
            self.conn.commit()
            print('Операция прошла успешно таблица добавлена в базу данных DB_Hash!')

    @staticmethod
    def create_hash():
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        hash_obj = sha256(login.encode() + password.encode()).hexdigest()
        return login, hash_obj

    def register(self):
        print('Регистрация!')
        login, reg_hash = self.create_hash()

        insert_stmt = 'INSERT INTO user_info(user_login, user_password) VALUES(?,?)'
        user_info = (login, reg_hash)

        try:
            self.crs.execute(insert_stmt, user_info)
        except IntegrityError:
            print('Такой login уже существует. Войдите в систему или введите другой login.')
        else:
            self.conn.commit()
            print('Вы зарегестрированы!')

    def log_in(self):
        print('Вход на сайт!')
        login, check_hash = self.create_hash()

        select_stmt = 'SELECT user_password FROM user_info WHERE user_login = ?'

        self.crs.execute(select_stmt, (login,))

        out_hash = self.crs.fetchone()

        if check_hash == out_hash[0]:
            print('Вы ввели правильный пароль!')
        else:
            print('Вы ввели неправильный пароль или не зарегестрировались!')


network = HashClass()
network.create_table()
network.register()
network.register()
network.register()
network.log_in()


# Решение с хранением логина и хэша-пароля в файле log_pass_hash.csv.
def create_hash():
    login = input('Введите логин: ')
    us_pass = input('Введите пароль: ')
    hash_passwd = sha256(login.encode() + us_pass.encode()).hexdigest()
    return login, hash_passwd


def save_hash(login, hash_passwd):
    with open('log_pass_hash.csv', 'a+', encoding='utf-8') as fa:
        fa.writelines(f'{login};{hash_passwd}\n')  # Записывает в файл логин и хэш пароля.


def read_hash():
    dict_hash = {}
    with open('log_pass_hash.csv', 'r+', encoding='utf-8') as fr:
        for _ in fr:
            dict_hash.setdefault(_.strip().split(";")[0], _.strip().split(";")[1])

    return dict_hash


def log_in(dict_hash):
    u_login = input('Введите логин: ')

    if u_login in dict_hash:
        u_password = input('Введите пароль: ')
        hash_u_password = sha256(u_login.encode() + u_password.encode()).hexdigest()
        if hash_u_password == dict_hash[u_login]:
            print('Доступ разрешён!')
            return exit(0)
        else:
            print('Неверный пароль!')
            return exit(1)
    else:
        print('Пользователь не зарегестрирован!')
        return exit(1)


login, hash_passwd = create_hash()
print(login, hash_passwd)
save_hash(login, hash_passwd)
log_in(read_hash())