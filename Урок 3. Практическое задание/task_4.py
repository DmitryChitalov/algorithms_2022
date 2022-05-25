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

from uuid import uuid4
import csv
import hashlib

def saltHesh():

    webPage1 = r'https://www.mazila@yandex.ru (https://www.mazila@yandex.ru/)'
    salt1 = uuid4().hex
    res1 = hashlib.sha256(salt1.encode('utf8') + webPage1.encode('utf8')).hexdigest()

    webPage2 = r'https://www.digicert.com'
    salt2 = uuid4().hex
    res2 = hashlib.sha256(salt2.encode('utf8') + webPage2.encode('utf8')).hexdigest()

    with open('url.csv', 'w') as csvfile:
        fieldnames = ['url_addres', 'hesh_url_a']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'url_addres': '{}'.format(webPage1), 'hesh_url_a': '{}'.format(res1)})
        writer.writerow({'url_addres': '{}'.format(webPage2), 'hesh_url_a': '{}'.format(res2)})


def webPageCaching(page):
    saltHesh()

    with open('url.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if page == row['url_addres']:
                print 'hesh_url_a: ' + str(row['hesh_url_a'])
            else:
                print 'Такой страницы нет'
                
    salt = uuid4().hex
    res = hashlib.sha256(salt.encode('utf8') + page.encode('utf8')).hexdigest()

    with open('url.csv', 'w') as csvfile1:
        fieldnames1 = ['url_addres', 'hesh_url_a']
        writer = csv.DictWriter(csvfile1, fieldnames=fieldnames1)

        writer.writeheader()
        writer.writerow({'url_addres': '{}'.format(page), 'hesh_url_a': '{}'.format(res)})


if name == 'main':
    webPage = str(raw_input('Введите веб-страницу: '))
    webPageCaching(webPage)
