from hashlib import sha512


dic = dict()
salt = sha512('salt'.encode()).hexdigest()


def hash(url):
    if url in dic:
        print('Уже есть в кэше:', dic[url])
    else:
        res = salt + sha512(url.encode()).hexdigest()
        dic[url] = res
        print('Хэш: ', res)
        print('Кэш: ', dic)


while len(dic) != 5:
    ur = input('Введите url: ')
    hash(ur)
