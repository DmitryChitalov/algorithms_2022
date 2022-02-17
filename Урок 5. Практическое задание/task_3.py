"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

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
(append, pop и т.д.) проводить в циклах
"""

from random import randint
from collections import deque
from timeit import timeit

arr = []
deq = deque()


def append_to(struct):
    for i in range(1000):
        struct.append(randint(0, 10))
    return struct


def pop_from(struct):
    for i in range(1000):
        struct.pop()
    return struct


def extend_to(struct):
    for i in range(1000):
        struct.extend([randint(0, 10), randint(0, 10)])
    return struct


for arg in (arr, deq):
    for func in (append_to, pop_from, extend_to):
        print(f"{func.__name__}: затраченое время {timeit('func(arg)', globals=globals(), number=100)}")


def insert_el_arr(array: list):
    for i in range(100):
        array.insert(0, randint(0, 10))
    return array


def insert_el_deq(my_deq: deque):
    for i in range(100):
        my_deq.appendleft(randint(0, 10))
    return my_deq


def pop_arr(array: list):
    for i in range(100):
        array.pop(0)
    return array


def pop_deq(my_deq: deque):
    for i in range(100):
        my_deq.popleft()
    return my_deq


def insert_list_arr(array: list):
    for i in range(100):
        array.insert(0, [randint(0, 10), randint(0, 10)])
    return array


def extleft_deq(my_deq: deque):
    for i in range(100):
        my_deq.extendleft([randint(0, 10), randint(0, 10)])
    return my_deq


def get_el(struct):
    return [struct[i] for i in range(len(struct))]


print("________________________________________________________________")
for func in (insert_el_arr, pop_arr, insert_list_arr, get_el):
    print(f"{func.__name__}: затраченое время {timeit('func(arr)', globals=globals(), number=100)}")
print("________________________________________________________________")
for func in (insert_el_deq, pop_deq, extleft_deq, get_el):
    print(f"{func.__name__}: затраченое время {timeit('func(deq)', globals=globals(), number=100)}")

"""
Учитывая наследственность интерфейса списка, дека показывает тот же результат по времени с методами
append, pop и extend, что и список

appendleft имеет константную сложность, что даёт преимущество над методом insert у списка с линейной сложностью 
insert_el_arr: затраченое время 0.6682050420000001
insert_el_deq: затраченое время 0.006907167000000047
Преимущество в ~100 раз
popleft справился с задачей колоссально быстрее, чем pop(0) в списке
pop_arr: затраченое время 0.45491150000000014
pop_deq: затраченое время 0.0004129170000002347
Операция вставки списка в начало списка и дека показал внушительное преимущество дека над списком
insert_list_arr: затраченое время 0.6701565000000003
extleft_deq: затраченое время 0.014378000000000224
И только при обращении к элементам списка и дека показало список в превосходящем над деком виде!
get_el: затраченое время 0.922702208
get_el: затраченое время 61.154712708999995
"""
