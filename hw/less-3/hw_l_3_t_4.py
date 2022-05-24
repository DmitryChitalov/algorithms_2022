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
from hashlib import sha256

salt = uuid4()
memory = {
    'http://example.com/aftermath': '6161c25fbaea608aa3a336279edd6ff2b977a0169b27713654778c0c492f050a',
    'http://example.com/angle': 'd63ceb7d3b860eb14fea60c1f9b9ed22ce232c0bdb4c9ef591e2adfcf70357ce',
    'https://birthday.example.com/': '31ac3e87547a0a09ea3f12936da37564d9e57077838daf4375550e263695d71d',
    'https://www.example.com/#box': '7aa75f7ec3054d8168e3ba3b09d2c2462bfb37b6e49e30a5286641bc2146b39a',
    'http://blood.example.com/border.php?advice=beds': '4c1f6d138b09a4815b32bc5b155731b40306390cb21cf3a190f95adc44000b45',
    'https://www.example.com/': 'c7eaf2fd5f953ac558df0e05cccda07a3efaf1cbf179e6c3619ab815c4a90e76'
}


def check_hash(url):
    hash_url = memory.get(url)
    if hash_url is None:
        hash_url = sha256(f'{salt}{url}'.encode()).hexdigest()
        memory[url] = hash_url
        print(memory)
    else:
        print(f'Кэш содержит {url}')


check_hash('http://example.com/aftermath')
check_hash('http://example.com/angle')
check_hash('https://birthday.example.com/')
check_hash('https://www.example.com/#box')
check_hash('http://blood.example.com/border.php?advice=beds')
check_hash('https://www.example.com/')
check_hash('url-адрес')
