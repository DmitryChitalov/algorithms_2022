"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта

В качестве примера выбрана 4 задача из третьего урока по Алгоритмам
"""


from pympler import asizeof
from os import urandom
from hashlib import pbkdf2_hmac


class Cash:

    def __init__(self):
        self.urls = {}
        self.salt = urandom(32)

    def check_url(self, url):
        rep_url = self.urls.get(url)
        if rep_url is None:
            self.urls.setdefault(url, pbkdf2_hmac('sha512', url.encode('utf-8'), self.salt, 1000))
            return f'Добавлен хэш для {url}'
        else:
            return f'хэш {url} - {rep_url.hex()}'


class CashOptimize:
    __slots__ = ['urls', 'salt']

    def __init__(self):
        self.urls = {}
        self.salt = urandom(32)

    def check_url(self, url):
        rep_url = self.urls.get(url)
        if rep_url is None:
            self.urls.setdefault(url, pbkdf2_hmac('sha512', url.encode('utf-8'), self.salt, 1000))
            return f'Добавлен хэш для {url}'
        else:
            return f'хэш {url} - {rep_url.hex()}'


cash_obj = Cash()
cash_obj_optimize = CashOptimize()
print(cash_obj.check_url('www.123.ru'))
print(cash_obj.check_url('www.123.ru'))

print(cash_obj.check_url('www.qwerty.ru'))
print(cash_obj.check_url('www.qwerty.ru'))

print(cash_obj_optimize.check_url('www.123.ru'))
print(cash_obj_optimize.check_url('www.123.ru'))

print(cash_obj_optimize.check_url('www.qwerty.ru'))
print(cash_obj_optimize.check_url('www.qwerty.ru'))

print(f'size cash_obj - {asizeof.asizeof(cash_obj)}')
print(f'size cash_obj_optimize - {asizeof.asizeof(cash_obj_optimize)}')


r"""
C:\Python3\python.exe "C:/GIT/exchange/Урок 6. Практическое задание/task_1_5.py"
Добавлен хэш для www.123.ru
хэш www.123.ru - 7a7cf942ec7c5d3e763c54c9b8f614b03857c7cec5b690ec13805ad20d0e951c1de6944cbec6f2b6313bbfcd9cb78e49796e932322993115dd80768141c8ba71
Добавлен хэш для www.qwerty.ru
хэш www.qwerty.ru - d7102545fe4e30acdfc89cc61ea5ccad2001ab6b0d57cc43f4854cb1134a130e964cc7b266e9a2463e32c3eedda01f8818f6229c589d69818542894a98c4369c
Добавлен хэш для www.123.ru
хэш www.123.ru - e512f241da89ae361946a708ae0e47c66ee5a3fbf2d009eed9f21fefb51c7f4254268376750bc5a94e6b1435fb3945db79f0c7285efdc84093c6ea4bea39ee92
Добавлен хэш для www.qwerty.ru
хэш www.qwerty.ru - f50faaf323cb4899dbe98948fb364e854b963a53c1e7758142424342eee842be4a847091b63bef6406c5fea8c28168060856e6ef00583a8682e6b984b47e6708
size cash_obj - 904
size cash_obj_optimize - 688

Выводы: при использовании слотов размер объекта меньше, в нашем случае это 904 против 688
"""