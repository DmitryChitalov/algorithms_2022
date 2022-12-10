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
"""

from memory_profiler import profile
from json import dumps, loads
import hashlib

my_dict = {}


@profile()
def check_url(my_url):
    salt = 'peper'
    if my_url in my_dict:
        return 'хеш уже есть в кэше', my_dict[my_url]
    else:
        my_dict[my_url] = (hashlib.sha512(salt.encode('utf-8') + my_url.encode('utf-8'))).hexdigest()
        return 'хеш добавлен в кэш', my_dict[my_url]


my_dict2 = {}
my_json_dict = dumps(my_dict2)


@profile()
def check_url2(my_url):
    salt = 'peper'
    if my_url in loads(my_json_dict):
        return f'хеш уже есть в кэше, {loads(my_json_dict)[my_url]}'
    else:
        loads(my_json_dict)[my_url] = (hashlib.sha512(salt.encode('utf-8') + my_url.encode('utf-8'))).hexdigest()
        return f'хеш добавлен в кэш, {loads(my_json_dict)[my_url]}'

check_url('https://gb.ru/')
check_url2('https://gb.ru/')

"""
Использовал сериализацию данных и f-строки для вывода данных, чтобы уменьшить потребление памяти.
"""
