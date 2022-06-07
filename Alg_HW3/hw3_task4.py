import hashlib
from uuid import uuid4
from binascii import hexlify


class UrlPage:
    base_cash = {}

    def __init__(self, url):
        self.url = url

    @classmethod
    def check_in_base(cls, url_add: str):
        if url_add in cls.base_cash.keys():
            print(cls.base_cash[url_add])
        else:
            url_dict = {url_add: hexlify(hashlib.pbkdf2_hmac
                                         (hash_name='sha256', password=url_add.encode(),
                                          salt=uuid4().bytes, iterations=1000))}
            cls.base_cash.update(url_dict)


page1 = UrlPage('https://gb.ru/lessons/195674')
UrlPage.check_in_base(page1.url)
print(UrlPage.base_cash)
page2 = UrlPage('https://gb.ru/lessons/195673')
UrlPage.check_in_base(page2.url)
print(UrlPage.base_cash)
page3 = UrlPage('https://gb.ru/lessons/195673')  # дублирую страницу 2
UrlPage.check_in_base(page3.url)
print(UrlPage.base_cash)
