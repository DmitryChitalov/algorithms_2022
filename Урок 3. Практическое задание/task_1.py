"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

import time
from timeit import timeit
from random import randint
import functools


def gettime(func):
    def inner():
        t = time.time()

        retval = func()

        t = time.time() - t
        print(t)
        return retval
    return inner




LEN = 100000

gen1 = [randint(-100,100) for i in range(LEN)]
gen2 = [(i,randint(-100,100)) for i in range(LEN)]



def _fillList(li = [],data = gen1) -> None:
    """
    Сложность: o(n), где n равно длине data
    """
    for el in data:
        li.append(el)



def _fillDict(di = {},pairs = gen2) -> None:
    """
    Сложность: o(2n), где n равно длине pairs
    """
    for el in pairs:
        di[el[0]] = el[1]

fillDict = gettime(_fillDict)
fillList = gettime(_fillList) #Можно было использовать wrapped, но у меня SDK не работает и модули не ставятся

fillList()
fillDict()

################################

l = []
_fillList(li=l)
d = {}
_fillDict(di=d)

def iterate(func):
    def inner():
        retval = []
        for i in range(LEN):
            retval.append(func())

        return retval
    return inner

@gettime
@iterate
def getElLi(l=l):
    """
    Сложность константная, одинаковая для обоих функций
    """
    for i in range(0,LEN):
        yield l[i]

@gettime
@iterate
def getElDi(d=d):
    for k in d.keys():
        yield d[k]


getElDi()
getElLi()

@gettime
def delLi(l=l):
    """
    Сложность о(n)
    """
    for i in range(LEN):
        l.pop()

@gettime
def delDi(d=d):
    """
    Сложность o(2n)
    """
    for i in range(LEN):
        d.pop(i)

l = []
_fillList(li=l)
d = {}
_fillDict(di=d)

delLi()
delDi()

"""

  






print(
    timeit(
        fillList,
        number=10000))


print(
    timeit(
        fillDict,
        number=10000))


print(
    timeit(
        gel,
        number=10000))

print(
    timeit(
        ged,
        number=10000))
    
    
    """