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
from hashlib import pbkdf2_hmac
from binascii import hexlify


def cash_url(url=(input('Введите url-фдрес сайта: '))):
    cash = {
        'gb.ru': b'7211a2e43cc900566136012308ea9d757ecd386b8faad83e996970326554517708a29fa58568f791e97e844391bff37ef880fe33e98e52b9919cdc98a34b906f',
        'hp.com': b'5180ab498d925ad001b24cd954334b0610d5eca875dbab975c6f846bfdd5b6fdb57cd5dee838c191b7c706640ecf1de4a81c462c3c7109334e3f5b035d01beb7',
        'apple.com': b'b81d3ebc36404cca027eae33116805dce309dd920081c1b914739c8eab955d62ef4103b8ce0fa5b11e9418a8c422bd9359377b02011f0c2a306747e9e4d60bea'}
    url_hash = pbkdf2_hmac(hash_name='sha512',
                           password=url.encode('utf-8'),
                           salt=url.encode('utf-8'),
                           iterations=1000)
    res = hexlify(url_hash)
    if res in cash.values():
        return res
    else:
        cash[url] = str(res)
        return fr'Страница {url} записана в кеш!'


print(cash_url())
