"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для третьего скрипта
"""

from hashlib import pbkdf2_hmac
from binascii import hexlify
import json
from memory_profiler import memory_usage, profile
from recordclass import recordclass
import pickle


def password_hash_sha(password: bytes, salt=str(), algorithm='sha256'):
    """
    Функция для создания хэша введенного пароля по алгоритму sha256.
    Возвращает строку из шестандцатиричных чисел.
    """
    password_hash = pbkdf2_hmac(hash_name=algorithm,
                                password=password,
                                salt=bytes(salt, 'utf-8'),
                                iterations=100)
    return password_hash # str(hexlify(password_hash))[2:][:-1]


def password_hash_sha_old(password: str, salt=str(), algorithm='sha256'):
    """
    Функция для создания хэша введенного пароля по алгоритму sha256.
    Возвращает строку из шестандцатиричных чисел.
    """
    password_hash = pbkdf2_hmac(hash_name=algorithm,
                                password=bytes(password, 'utf-8'),
                                salt=bytes(salt, 'utf-8'),
                                iterations=100)
    return str(hexlify(password_hash))[2:][:-1]


def create_passwords(file_name: str, number=2):
    """
    Функция запрашивает логин, пароль и соль и записывает в файл json.
    В качестве аргументов функции задаются путь до файла и количество записей.
    Примечание. При обращении к функции файл перезаписывается.
    """
    user_dict = dict()
    for i in range(0, 1000):
        login = str(i)
        password = bytes(str(i), 'utf-8')
        salt = str(i)
        password_hash = password_hash_sha(password, salt)
        user_dict.setdefault(login, (salt, password_hash))
    with open(file_name, 'wb') as fp:
        pickle.dump(user_dict, fp)


def create_passwords_old(file_name: str, number=2):
    """
    Функция запрашивает логин, пароль и соль и записывает в файл json.
    В качестве аргументов функции задаются путь до файла и количество записей.
    Примечание. При обращении к функции файл перезаписывается.
    """
    user_dict = dict()
    for i in range(0, 1000):
        login = str(i)
        password = str(i)
        salt = str(i)
        password_hash = password_hash_sha_old(password, salt)
        user_dict.setdefault(login, (salt, password_hash))
    with open(file_name, 'w') as fp:
        json.dump(user_dict, fp)


@profile
def password_check(file_name: str, login=str(), ask_login=True):
    """
    Функция запрашивает логин пользователя и проверяет, есть ли пользователь в файле .json, который указан в
    качестве аргумента. Если пользователь есть в файле, функция запрашивает пароль. Если хэш пароля есть в файле
    .json, пользователю предоставляется доступ. Если нет, функция просит пользователя повторно пройти аутентификацию.
    """
    try:
        if ask_login:
            print('Пожалуйста, введите Ваш логин: ', end='')
            login = input()
        with open(file_name, 'rb') as fp:
            users_dict = pickle.load(fp)
        salt = users_dict[login][0]
        print('Пожалуйста, введите Ваш пароль: ', end='')
        password = bytes(input(), 'utf-8')
        password_hash = password_hash_sha(password, salt)
        print(f'Хэш введенного пароля: {password_hash}')
        if password_hash == users_dict[login][1]:
            print('Пожалуйста, введите Ваш пароль еще раз: ', end='')
            password = bytes(input(), 'utf-8')
            password_hash = password_hash_sha(password, salt)
            print(f'Хэш введенного пароля: {password_hash}')
            if password_hash == users_dict[login][1]:
                print(f'Пароль верный. Добро пожаловать, {login}')
            else:
                print('Произошла ошибка. Попробуйте пройти аутентификацию еще раз: ', end='')
                password_check(file_name)
        else:
            print('Неверный пароль. Попробуйте еще раз: ', end='')
            password_check(file_name, login=login, ask_login=False)
    except KeyError:
        print('Неверный логин. Попробуйте еще раз. ', end='')
        password_check(file_name)


@profile
def password_check_old(file_name: str, login=str(), ask_login=True):
    """
    Функция запрашивает логин пользователя и проверяет, есть ли пользователь в файле .json, который указан в
    качестве аргумента. Если пользователь есть в файле, функция запрашивает пароль. Если хэш пароля есть в файле
    .json, пользователю предоставляется доступ. Если нет, функция просит пользователя повторно пройти аутентификацию.
    """
    try:
        if ask_login:
            print('Пожалуйста, введите Ваш логин: ', end='')
            login = input()
        with open(file_name, 'r') as fp:
            users_dict = json.load(fp)
        salt = users_dict[login][0]
        print('Пожалуйста, введите Ваш пароль: ', end='')
        password = input()
        password_hash = password_hash_sha_old(password, salt)
        print(f'Хэш введенного пароля: {password_hash}')
        if password_hash == users_dict[login][1]:
            print('Пожалуйста, введите Ваш пароль еще раз: ', end='')
            password = input()
            password_hash = password_hash_sha_old(password, salt)
            print(f'Хэш введенного пароля: {password_hash}')
            if password_hash == users_dict[login][1]:
                print(f'Пароль верный. Добро пожаловать, {login}')
            else:
                print('Произошла ошибка. Попробуйте пройти аутентификацию еще раз: ', end='')
                password_check(file_name)
        else:
            print('Неверный пароль. Попробуйте еще раз: ', end='')
            password_check_old(file_name, login=login, ask_login=False)
    except KeyError:
        print('Неверный логин. Попробуйте еще раз. ', end='')
        password_check_old(file_name)


if __name__ == '__main__':
    print('\nСкрипт №2 из д/з №3 курса "Алгоритмы и структуры данных Python".\n'
          'Скрипт модифицирован за счет бинарной сериализации pickle (в исходном коде был json), а также за счет того\n'
          'что вводимый пользователем пароль и вычисленный хэш хранятся и сравниваются в бинарном виде, т. е. без \n'
          'преобразования в строку как было в исходном варианте.\n')
    create_passwords('./passwords')
    create_passwords_old('./passwords.json')
    print('Генерируется словарь вида {"login": ("salt", "password_hash")} со значениями: \n'
          '  {"1": ("1", "...sha256..."),\n'
          '   "2": ("2", "...sha256...")...\n'
          '..."100": ("100", "...sha256...")}\n')
    print('Работу какой функции вы хотите проверить? (1 - исходная, 2 - оптимизированная): ', end='')
    mode = int(input())
    '''
    Примечание.
    Профилирование вынес в функцию main, потому в функциях есть рекурсия.
    '''
    if mode == 1:
        mem_1 = memory_usage(max_usage=True)
        password_check_old('./passwords.json')
        mem_2 = memory_usage(max_usage=True)
        print(f'Выполнение занимает {mem_2 - mem_1} MiB')
    if mode == 2:
        mem_1 = memory_usage(max_usage=True)
        password_check('./passwords')
        mem_2 = memory_usage(max_usage=True)
        print(f'Выполнение занимает {mem_2 - mem_1} MiB')
