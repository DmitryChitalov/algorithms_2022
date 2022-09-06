import hashlib
salt = 'some_salt'
cache = {}


def check_pade(url):
    if cache.get(url):
        print(f'Хэш url {url} уже присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = res
        print(cache)


check_pade('https://gb.ru')
check_pade('https://github.com')
check_pade('https://gb.ru')