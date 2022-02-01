"""
Задание 1.
Реализуйте:
a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.
b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.
ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import random

my_list = []
my_dict = {}


def timer(func):
    from time import time

    def mer(*args):
        start = time()
        func(*args)
        finish = time()
        print(f'{func} took {finish - start}')
    return mer


@timer
def fill_list(f_list):
    for i in range(10000):     # O(n)
        f_list.append(random.randint(0, 100))  # O(1)


@timer
def fill_dict(f_dict):
    for i in range(10000):     # O(n)
        f_dict[i] = random.randint(0, 100)  # O(1)


fill_list(my_list)
fill_dict(my_dict)
# Значения времени постоянно меняются в замерах. Я думаю словарь должен заполняться немного дольше из-за хеширования.


@timer
def change_list(ch_list):
    for i in range(10000):     # O(n)
        ch_list[i] = random.randint(0, 100)  # O(1)


@timer
def change_dict(ch_dict):
    for i in range(10000):     # O(n)
        ch_dict[i] = random.randint(0, 100)  # O(1)


change_list(my_list)
change_dict(my_dict)
# Значения практически идентичны. Судя по О-нотации, так и должно быть.


@timer
def del_from_list(d_list):
    for i in range(10000):     # O(n)
        del(d_list[10000 - 1 - i])      # O(n), как и у remove()


@timer
def del_from_dict(d_dict):
    for i in range(10000):     # O(n)
        d_dict.popitem()   # О-нотация все равно O(1), а так нам не нужны ключи


del_from_list(my_list)
del_from_dict(my_dict)
# В замерах все равно постоянно изменяются цифры. Удаление элемента из списка должно быть медленнее.


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
from uuid import uuid4
import hashlib
import json


def registration():
    name = hashlib.sha256(input('Input your name: ').encode('utf-8')).hexdigest()

    with open('users_data.json', 'r') as f:
        users_data = json.load(f)

        if name in users_data.keys():
            name = hashlib.sha256(input('Input your name, it has to be unique: ').encode('utf-8')).hexdigest()
        salt = uuid4().hex
        passwd = hashlib.sha256(salt.encode() + input('Input your password: ').encode('utf-8')).hexdigest()
        users_data[name] = [salt, passwd]
        with open('users_data.json', 'w') as file:
            json.dump(users_data, file)


def chek():
    chek_name = hashlib.sha256(input('Input your name: ').encode('utf-8')).hexdigest()

    with open('users_data.json', 'r', encoding='utf-8') as f:
        users_data = json.load(f)

        if chek_name in users_data.keys():
            salt = users_data[chek_name][0]
            chek_passwd = hashlib.sha256(salt.encode() + input('Input your password: ').encode('utf-8')).hexdigest()
            if chek_passwd == users_data[chek_name][1]:
                return print('OK, come in')
            else:
                return print('password is wrong')
        else:
            return print('No such user')


def choice():
    ch = input('input "r" if you want to register, or "l" if you want to log in')
    if ch == 'r':
        return registration()
    elif ch == 'l':
        return chek()
    else:
        return choice()


choice()
# Это выглядит ужасно нагроможденно и скорее всего куча ошибок, посоветуйте пожадуйста, как лучше разобраться
# с этими переводами в джейсон. Разбор с урока если успею тоже постараюсь сделать, пока не успеваю совсем(


"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""
import hashlib

base_str = 'papa'

unique = set()
n = 0

while n < len(base_str):
    for i in range(1, len(base_str)):
        if n+i <= len(base_str):
            sub_str = hashlib.sha256(base_str[n:n+i].encode('utf-8')).hexdigest()
            unique.add(sub_str)
            print(unique)
    n += 1

print(f'this string contains {len(unique)} unique substrings')



"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет.
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""


class UrlCaching:
    def __init__(self):
        import uuid
        self.cache_dict = {}
        self.salt = uuid.uuid4().hex

    def get_cache(self, url):
        if self.cache_dict.get(url):
            return print('url is already in cache ', self.cache_dict[url])
        else:
            import hashlib
            self.cache_dict[url] = hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()
            return print('url added to cache ', self.cache_dict[url])


today_cache = UrlCaching()
today_cache.get_cache('https://github.com/DmitryChitalov/algorithms_2022/task_4.py')
today_cache.get_cache('https://github.com/DmitryChitalov/algorithms_2022/task_4.py')
