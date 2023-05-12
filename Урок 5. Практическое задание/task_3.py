"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
import random
import timeit


def test_app_deq():
    d = deque()
    for i in range(1000):
        d.append(i)

def test_app_li():
    l = list()
    for i in range(1000):
        l.append(i)


def test_appleft_deq():
    for i in range(1000):
        d.appendleft(i)

def test_appleft_li():
    for i in range(1000):
        l.insert(0,i)


def test_ext_deq():
    d = deque()
    d.extend(data)

def test_ext_li():
    l = list()
    l.extend(data)

def test_extleft_deq():
    global d
    d.extendleft(data)

def test_extleft_li():
    global l
    l = data + l


def test_pop_deq():
    for i in range(1000):
        d.pop()

def test_pop_li():
    for i in range(1000):
        l.pop()

def test_popleft_deq():
    for i in range(1000):
        d.popleft()

def test_popleft_li():
    for i in range(1000):
        del l[0]


def getitem_deq():
    for i in range(0,1000):
        yield d[i]

def getitem_li():
    for i in range(0,1000):
        yield l[i]


d = deque()
l = list()
data = []
for i in range(1000):
    data.append(random.randint(-10000000000,10000000000))
#print(data)
print("deque append: ",timeit.timeit( test_app_deq, number=10000)) #список быстрее, странно
print("list append: ",timeit.timeit( test_app_li, number=10000))

d = deque()
l = list()
print("deque appendleft: ", timeit.timeit( test_appleft_deq, number=1000)) #дека быстрее
print("list appendleft: ", timeit.timeit( test_appleft_li, number=1000))


d = deque()
l = list()
#print(data)
print("deque ext: ", timeit.timeit(test_ext_deq, number=10000)) # дека быстрее
print("list ext: ", timeit.timeit(test_ext_li, number=10000))


d = deque(data[:])
l = data[:]
#print(data)
print("deque extendleft: ", timeit.timeit(test_extleft_deq, number=1000))# дека быстрее за исключением случаев когда
# список пустой
print("list extendleft: ", timeit.timeit(test_extleft_li, number=1000))


d = deque(data[:])
l = data[:]
print("deque pop: ", timeit.timeit(test_pop_deq, number=1))#pop быстрее в списке
print("list pop: ", timeit.timeit(test_pop_li, number=1))

d = deque(data[:])
l = data[:]
print("deque popleft: ", timeit.timeit(test_popleft_deq, number=1))#popleft быстрее в деке
print("list popleft: ", timeit.timeit(test_popleft_li, number=1))

d = deque(data[:])
l = data[:]
print("deque get: ", timeit.timeit(getitem_deq, number=1))
print("list get: ", timeit.timeit(getitem_li, number=1)) #случайный доступ быстрее в списке

