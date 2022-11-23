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


def url_cache(url):
    import hashlib
    import json
    salt = 'my_salt'

    try:
        open('url_cache.json', 'r+')
    except FileNotFoundError:
        with open('url_cache.json', 'w+') as f:
            data = {}
            url_hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
            data[url] = url_hash
            json.dump(data, f)
    else:
        f = open('url_cache.json', 'r+')
        file_data = f.read()
        if file_data == '':
            data = {}
            url_hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
            data[url] = url_hash
            json.dump(data, f, indent=4)
            f.close()
        else:
            data = json.loads(file_data)
            if url in data:
                print(data[url])
                f.close()
            else:
                f.close()
                with open('url_cache.json', 'w+') as f:
                    url_hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
                    data[url] = url_hash
                    f.write(json.dumps(data, indent=4))


url_cache('https://www.ya.ru/')
url_cache('https://www.mail.ru/')
url_cache('https://www.google.com/')
url_cache('https://www.amazon.com/')
