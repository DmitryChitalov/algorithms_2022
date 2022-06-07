import hashlib
from uuid import uuid4
from binascii import hexlify


def check_url(url_in):
    salt = uuid4().hex
    salt = 'my_salt'
    hash = hashlib.sha256(salt.encode() + url_in.encode()).hexdigest()
    res1 = hashlib.sha256(salt.encode() + 'https://mail.ru/'.encode()).hexdigest()
    res2 = hashlib.sha256(salt.encode() + 'https://yandex.ru/'.encode()).hexdigest()
    cash = {'https://mail.ru/': res1, 'https://yandex.ru/': res2}
    if url_in not in cash.keys():
        cash[url_in] = hash
        print(f'Такого хеша нет. Был добавлен в кэш новый хеш для {url_in}: {hash}')
    else:
        print(f'Хеш {url_in} : {hash}')


check_url('https://mail.ru/')
