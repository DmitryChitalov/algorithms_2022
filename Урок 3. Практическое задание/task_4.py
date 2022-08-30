"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib

data_base_url = set()


def check_url(login, url_address):
    print("Ваш аккаунт -", login)
    hash_url_address = set()
    hash_url_address = (hashlib.sha256(url_address.encode("utf-8") + login.encode("utf-8")).hexdigest())
    if url_address or login == '0':
        print("выход")
    else:
        if hash_url_address in data_base_url:
            print("Ссылка есть в базе ", hash_url_address)
        else:
            print("Ссылка добавлена в базу", hash_url_address)
            data_base_url.add(hash_url_address)
        return check_url(input("enter login: "), input("enter url: "))


check_url(input("enter login: "), input("enter url: "))
