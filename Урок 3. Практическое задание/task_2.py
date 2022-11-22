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
   

def create_password():
    '''
    Функция принимает от пользователя данные для создания пароля
    :return: str
    '''
    password = input('Введите пароль: ')
    check_password = input('Повторите пароль: ')
    if password == check_password:
        return password
    else:
        print('Пароль не совпадает. Повторите ввод')
        return create_password()


def create_login():
    '''
    Функция принимает от пользователя данные для создания логина
    :return: str
    '''
    login = input('Введите логин(6-10 символов): ')
    if 5 < len(login) < 11:
        return login
    else:
        print('Длина логина неверная. Повторите ввод')
        return create_login()


def create_salt(a: str):
    '''
    Функция принимает строковые данные перемешивает и возвращае
    :param a: str
    :return: str
    '''
    return a[-3:] + a[2:5] + a[:3]


def create_hash(a, b):
    '''
    Функция созадает хеш-пароль и солит его
    :param a:
    :param b:
    :return:
    '''
    from hashlib import pbkdf2_hmac
    from binascii import hexlify
    password = b
    salt = create_salt(a)
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=password.encode('utf-8'),
                      salt=salt.encode('utf-8'),
                      iterations=100000)
    result = hexlify(obj)
    print(result)
    return result


def write_data(login, hash):
    '''
    Функция принимает данные логина и хеш пароля и сохраняет в data_login.csv
    :param login:
    :param hash:
    :return:
    '''
    import csv
    with open('data_login.csv', 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([login, hash])
    file.close()


def save_data():
    '''
    Функция вызывает функции для создания логина и пароля пользователем,
    создания из полученных данных хеш-пароля и записи в файл созданных учетных данных
    :return:
    '''
    print('Регистрация')
    login = create_login()
    password = create_password()
    user_hash = create_hash(login, password)
    write_data(login, user_hash)


def check_data(login: str, hash_password: str):
    '''
    Функция принимает логин и хеш-пароль и сверяет с сохраннеными в файле(БД) данными
    :param login: str
    :param hash_password: str
    :return:
    '''
    login_list = []
    password_list = []
    hash_password = str(hash_password)
    with open('data_login.csv', 'r') as file:
        for line in file:
            one_line = line.strip('\n').split(',')
            login_list.append(one_line[0])
            password_list.append(one_line[1])
    file.close()
    if login not in login_list:
        print('Логина не существует')
        return False
    for i in range(len(login_list)):
        if login_list[i] == login and password_list[i] == hash_password:
            print('Добро пожаловать!')
            return True
    print('Пароль неверный')
    return False


def login():
    '''
    Функция для входа в систему. Принисает от пользователя Логин и Пароль.
    Вызывает функции для созндания хеш-пароля
     и проверки полученных от пользователя данных на соответствие сохраненным данным для входа
    :return:
    '''
    print('Вход в систему')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    user_hash = create_hash(login, password)
    result = check_data(login, user_hash)


def program_3_2():
    '''
    Программа запускает функции создания логина и пароля и функциию для входа в систему
    :return:
    '''
    # save_data()
    login()


program_3_2()
