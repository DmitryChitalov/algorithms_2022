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

from timeit import timeit
from collections import deque
from random import randint


#  сравнить операции append, pop, extend списка и дека
def fanc_ap_lst(x, y):
    for i in y:
        x.append(i)


def fanc_ap_deq(x, y):
    for i in y:
        x.append(i)


def fanc_pop_lst(x):
    for i in range(len(x)):
        x.pop()


def fanc_pop_deq(x):
    for i in range(len(x)):
        x.pop()


def fanc_ex_lst(x, y):
    x.extend(y)


def fanc_ex_deq(x, y):
    x.extend(y)


some_lst_1 = list('geek')
some_lst_2 = list('brains')
deq_obj = deque(some_lst_1)

print(timeit("fanc_ap_lst(some_lst_1, some_lst_2)", globals=globals(),
             number=1000), ' - append список')
print(timeit("fanc_ap_deq(deq_obj, some_lst_2)", globals=globals(),
             number=1000), ' - append deque')
print(timeit("fanc_pop_lst(some_lst_1)", globals=globals(),
             number=1000), ' - pop список')
print(timeit("fanc_pop_deq(deq_obj)", globals=globals(),
             number=1000), ' - pop deque')
print(timeit("fanc_ex_lst(some_lst_1, some_lst_2)", globals=globals(),
             number=1000), ' - extend список')
print(timeit("fanc_ex_deq(deq_obj, some_lst_2)", globals=globals(),
             number=1000), ' - extend deque')
print('!' * 100)
"""
0.00045509999836212955  - append список
0.0004879000007349532  - append deque
0.0005632000011246419  - pop список
0.0005674999993061647  - pop deque
0.0001593000015418511  - extend список
0.0002330999996047467  - extend deque
"""
"""
При операциях  append, pop, extend списка и дека, в некоторых моментах список
выигрывает по времени, но отклонение небольшое
"""


# сравнить операции appendleft, popleft, extendleft дека и
# соответствующих им операций списка
def fanc_ap_lf_lst(x, y):
    for i in y:
        x.insert(0, i)


def fanc_ap_lf_deq(x, y):
    for i in y:
        x.appendleft(i)


def fanc_pop_lf_lst(x):
    for i in range(len(x)):
        x.pop(0)


def fanc_pop_lf_deq(x):
    for i in range(len(x)):
        x.popleft()


def fanc_ex_lf_lst(x, y):
    for i in y:
        x.insert(0, i)


def fanc_ex_lf_deq(x, y):
    x.extendleft(y)


print(timeit("fanc_ap_lf_lst(some_lst_1, some_lst_2)", globals=globals(),
             number=1000), ' - аналог append left список')
print(timeit("fanc_ap_lf_deq(deq_obj, some_lst_2)", globals=globals(),
             number=1000), ' - append left deque')
print(timeit("fanc_pop_lf_lst(some_lst_1)", globals=globals(),
             number=1000), ' - аналог pop left список')
print(timeit("fanc_pop_lf_deq(deq_obj)", globals=globals(),
             number=1000), ' - pop left deque')
print(timeit("fanc_ex_lf_lst(some_lst_1, some_lst_2)", globals=globals(),
             number=1000), ' - аналог extend left список')
print(timeit("fanc_ex_lf_deq(deq_obj, some_lst_2)", globals=globals(),
             number=1000), ' - extend left deque')
print('!' * 100)

"""
0.021842100000867504  - аналог append left список
0.0004515000000537839  - append left deque
0.017288100001678686  - аналог pop left список
0.0008472000008623581  - pop left deque
0.006878300000607851  - аналог extend left список
0.00019579999934649095  - extend left deque
"""
"""
По полученным данным видно, что в случае работы с началом списка коллекция
deque работает на порядок быстрее, чем опирации со списком
"""


# сравнить операции получения элемента списка и дека
def fanc_lst(x):
    for i in range(len(some_lst_1)):
        x[i]


def fanc_deq(x):
    for i in range(len(deq_obj)):
        x[i]


print(timeit("fanc_lst(some_lst_1)", globals=globals(),
             number=1000), ' - перебор элементов списка')
print(timeit("fanc_deq(deq_obj)", globals=globals(),
             number=1000), ' - перебор элементов deque')


def fanc_lst_1(x, i):
    x[i]


def fanc_deq_1(x, i):
    x[i]


rand_num = randint(0, len(deq_obj))

print(timeit("fanc_lst_1(some_lst_1, rand_num)", globals=globals(),
             number=1000), ' - случайный элемент списка')
print(timeit("fanc_deq_1(deq_obj, rand_num)", globals=globals(),
             number=1000), ' - случайный элемент deque')
"""
0.19422639999902458  - перебор элементов списка
0.3668634999994538  - перебор элементов deque
0.00012870000136899762  - случайный элемент списка
0.00012240000069141388  - случайный элемент deque
"""
"""
Перебор элементов списка производится быстрее. Но если, брать кокой-то 
конкретный элемент списка или deque, скорость почти одинакова 
"""
