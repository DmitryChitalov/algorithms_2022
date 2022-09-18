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

Это файл для третьего скрипта
"""
from memory_profiler import memory_usage
from random import randrange, sample
from collections import namedtuple


def memoriser(func, *args):
    def wrapper(*args):
        start = memory_usage()[0]
        res = func(*args)
        mem = memory_usage()[0] - start
        print(func)
        print(mem)
        return res

    return wrapper


tovary = []
count_tov = 0
string = "QWERTYUIOPASDFGHJKLZXCVBNM"
atr = namedtuple("atr", 'name price count ed')


#  Исходный код
def get_tovar():
    tname = ''.join(sample(string, 5))
    tprice = randrange(200)
    tcount = randrange(1000)
    ted = ''.join(sample(string, 3))
    return {'name': tname, 'price': tprice, 'count': tcount, 'ed': ted}


@memoriser
def get_analys(tov):
    names, prices, countes, eds = set(), set(), set(), set()
    for i in tov:
        names.add(i[1]['name'])
        prices.add(i[1]['price'])
        countes.add(i[1]['count'])
        eds.add(i[1]['ed'])
    analitics = {'названия': list(names), 'цены': list(prices), 'количества': list(countes), 'единицы': list(eds)}
    return analitics


@memoriser
def products():
    global tovary
    global count_tov
    for i in range(1000):
        count_tov += 1
        tovary.append((count_tov, get_tovar()))


# Оптимизированный код
def get_tovar1():
    tname = ''.join(sample(string, 5))
    tprice = randrange(200)
    tcount = randrange(1000)
    ted = ''.join(sample(string, 3))
    return atr(name=tname, price=tprice, count=tcount, ed=ted)


@memoriser
def get_analys1(tov):
    names, prices, countes, eds = set(), set(), set(), set()
    for i in tov:
        names.add(i[1].name)
        prices.add(i[1].price)
        countes.add(i[1].count)
        eds.add(i[1].ed)
    analitics = {'названия': list(names), 'цены': list(prices), 'количества': list(countes), 'единицы': list(eds)}
    return analitics


@memoriser
def products1():
    global tovary
    global count_tov
    for i in range(1000):
        count_tov += 1
        tovary.append((count_tov, get_tovar1()))


print('Старый вариант - со словарем')
products()
get_analys(tovary)

# очищаем переменные
tovary = []
count_tov = 0

print(("Новый вариант - с именованным кортежем"))
products1()
get_analys1(tovary)

"""
Старый вариант - со словарем
<function products at 0x0000016B61ADE4D0>
0.3828125
<function get_analys at 0x0000016B61ADE8C0>
0.125
Новый вариант - с именованным кортежем
<function products1 at 0x0000016B61ADFF40>
0.01171875
<function get_analys1 at 0x0000016B61ADE710>
0.0703125

Ничего себе выигрыш в памяти!
Заменила словарь именнованым кортежем.
Я понимаю, почему выигрыш в пямяти при заполнении словаря/кортежа,
и не понимаю, почему при составлении аналитики.
"""
