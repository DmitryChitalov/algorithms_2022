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


import hashlib
import MySQLdb


class CheckPasswordClass:
    def __init__(self):
        self.db = MySQLdb.connect("192.168.42.134","user","password","vk")
        self.curs = self.db.cursor()

    def create_table(self):
        self.curs.execute("DROP TABLE IF EXISTS usr")
        self.curs.execute("CREATE TABLE usr (user_login VARCHAR(150), "
                          "password_hash VARCHAR(150))")
        self.db.commit()
        print("Таблица пользователей добавлена")

    def usr_hash(self):
        login = input("Введите логин: ")
        passwd = input("Введите пароль: ")
        # солим хеш пароля через login
        hash_pwd = hashlib.sha256(login.encode() + passwd.encode()).hexdigest()
        #print(login, hash_pwd)
        return login, hash_pwd

    def reg(self):
        login, hash_pwd = self.usr_hash()
        user_insert = (login, hash_pwd)
        insert_stmt = "INSERT INTO usr (user_login, password_hash) VALUES (%s, %s)"
        pwd_update = (hash_pwd, login)
        update_stmt = "UPDATE usr SET password_hash = %s WHERE user_login = %s"

        check_name_stmt = "SELECT COUNT(*) FROM usr WHERE user_login = %s"
        self.curs.execute(check_name_stmt, [login])
        res = self.curs.fetchone()
        try:
            if res[0]:
                self.curs.execute(update_stmt, pwd_update)
                print(f'Для пользователя "{login}" в БД \n'
                      f'хеш пароля обновлён на: {hash_pwd}')
            else:
                self.curs.execute(insert_stmt, user_insert)
                print(f'Пользователь "{login}" добавлен в БД \n'
                      f'с хешем пароля: {hash_pwd}')
        except MySQLdb.ProgrammingError:
            print("Not all arguments converted during bytes formatting")
        else:
            self.db.commit()

    def compare(self):
        login, hash_pwd = self.usr_hash()
        get_pwd_stmt = "SELECT password_hash FROM usr WHERE user_login = %s"
        self.curs.execute(get_pwd_stmt, [login])
        get_pwd = self.curs.fetchone()
        try:
            if get_pwd[0] == hash_pwd:
                print("Вы ввели правильный пароль")
            else:
                print("Введён неверный пароль!")
        except TypeError:
            print(f'Пользователя "{login}" в БД не существует!')


if __name__ == '__main__':
    test = CheckPasswordClass()
    #test.create_table()   # создадим таблицу usr для опытов
    #test.get_hash()
    print("Регистрация пользователей в БД")
    test.reg()
    test.reg()
    test.reg()

    print()
    print("Проверка пароля пользователя")
    test.compare()
    test.compare()
    test.compare()

"""
Регистрация пользователей в БД
Введите логин: 111
Введите пароль: pwd111
Пользователь "111" добавлен в БД 
с хешем пароля: 11e9a9a97d6a5c210af518bc491daf8effb8c39b9ca0c16b16ea253c14e7f852
Введите логин: 222
Введите пароль: pwd222
Пользователь "222" добавлен в БД 
с хешем пароля: 2d78a80dab296b960b4bfd69b761ca3f63603d601ac90f18c9e4fb87ddf79f76
Введите логин: 222
Введите пароль: pwd333
Для пользователя "222" в БД 
хеш пароля обновлён на: ef7903fed58842a7be31427a9379d7edab3ff7f1101bc368040de914c8dc01a5

Проверка пароля пользователя
Введите логин: 222
Введите пароль: pwd333
Вы ввели правильный пароль
Введите логин: 111
Введите пароль: qweqe
Введён неверный пароль!
Введите логин: 333
Введите пароль: ewfwe
Пользователя "333" в БД не существует!
"""
