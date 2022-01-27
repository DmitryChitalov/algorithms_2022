"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
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


def hash_passwd(login, passwd, salt):
    """
    Функция для генерации хеша (ключа).
    """
    obj = hashlib.pbkdf2_hmac(hash_name='sha256',
                              salt=salt,
                              password=passwd.encode('utf-8'),
                              iterations=10000)
    result = hexlify(obj)
    print(f'Ключ: {result}')
    return login, result, salt


def check_user(login, passwd):
    """
    Функция для проверки пользователя.
    Если пользователь новый, он не зарегистрирован в базе.
    Если пользователь зарегистрирован, то функция возвращает
    результат сравнения ключа в базе данных
    со сгенерированным ключем пользователя
    """
    with shelve.open('data_file', writeback=True) as db:
        for key in db:
            if key == login:
                login, result, salt = hash_passwd(login, passwd, db[key][1])
                return f'Совпадение хеша: {result == db[login][0]}'
            else:
                return f'Пользователь {login} не зарегистрирован'


def add_to_base(login, passwd):
    """
    Функуия для заведения пользователя в базу данных.
    Случайным образом генерируется соль в байтах
    для использования в другой функции - hash_passwd
    """
    salt = uuid4().bytes
    login, result, salt = hash_passwd(login, passwd, salt)
    with shelve.open('data_file', writeback=True) as db:
        db[login] = result, salt
    return db


if __name__ == '__main__':
    from uuid import uuid4
    from binascii import hexlify
    import hashlib
    import shelve

    add_to_base(login=input('Введите логин(email): '), passwd=input('Введите пароль: '))
    print(check_user(login=input('Введите логин: '), passwd=input('Введите пароль: ')))
    print(check_user(login=input('Введите логин: '), passwd=input('Введите пароль: ')))
