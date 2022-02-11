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

from timeit import timeit
from collections import deque
from random import randint


def check_list_append(my_lst):
    for i in range(0, 10000):
        my_lst.append(i)


def check_deque_append(my_deque):
    for i in range(0, 10000):
        my_deque.append(i)


new_lst = list(randint(0, 10000) for i in range(1000))
new_deque = deque(randint(0, 10000) for j in range(1000))
print("list append", timeit("check_list_append(new_lst)", number=2000, globals=globals()))
print("deque append", timeit("check_deque_append(new_deque)", number=2000, globals=globals()))

"""
Все скрипты прогонял по 4 раза.
Что бы не делать текстовый файл из дз , прикреплю по 1 самому меньшему результату.
Операция list append выполняется чуть медленнее чем deque append.

list append 1.8056761 
deque append 1.4272487999999999 
"""


def check_list_pop(my_lst):
    for i in range(0, 10000):
        my_lst.pop()


def check_deque_pop(my_deque):
    for i in range(0, 10000):
        my_deque.pop()


print("list pop", timeit("check_list_pop(new_lst)", number=2000, globals=globals()))
print("deque pop", timeit("check_deque_pop(new_deque)", number=2000, globals=globals()))

"""
Операция list pop выполняется чуть медленнее deque pop
list pop 1.4931855999999994 
deque pop 1.3252319999999997 
"""


def check_list_extend(my_lst):
    add_lst = list(randint(0, 10000) for i in range(10))
    for i in range(0, 1000):
        my_lst.extend(add_lst)


def check_deque_extend(my_deque):
    add_deque = list(randint(0, 10000) for i in range(10))
    for i in range(0, 1000):
        my_deque.extend(add_deque)


print("list extend", timeit("check_list_extend(new_lst)", number=2000, globals=globals()))
print("deque extend", timeit("check_deque_extend(new_deque)", number=2000, globals=globals()))

"""
Операция list extend выполняется на много медленне чем deque extend.
list extend 1.3252319999999997
deque extend 0.40657819999999933
"""


def check_list_insert(my_lst):
    for i in range(0, 1000):
        my_lst.insert(0, i)


def check_deque_appendleft(my_deque):
    for i in range(0, 1000):
        my_deque.appendleft(i)


new_lst = list(randint(0, 10000) for i in range(1000))
new_deque = deque(randint(0, 10000) for j in range(1000))

print("list insert", timeit("check_list_insert(new_lst)", number=200, globals=globals()))
print("deque appendleft", timeit("check_deque_appendleft(new_deque)", number=200, globals=globals()))

"""
Операция list insert выполняется гораздо медленнее, чем deque appendleft
list insert 12.872783900000002
deque appendleft 0.013674599999998094
"""


def check_list_popleft(my_lst):
    for i in range(1, 10):
        my_lst.pop(i)


def check_deque_popleft(my_deque):
    for i in range(1, 10):
        my_deque.popleft()


print("list popleft", timeit("check_list_popleft(new_lst)", number=20000, globals=globals()))
print("deque popleft", timeit("check_deque_popleft(new_deque)", number=20000, globals=globals()))

"""
Операция list popleft выполняется гораздо медленнее,  чем deque popleft
list popleft 8.8502209
deque popleft 0.015984899999999413
"""


def check_list_extendleft(my_lst):
    add_lst = list(randint(0, 10000) for i in range(10))
    for i in range(0, 1000):
        my_lst.insert(0, add_lst)


def check_deque_extendleft(my_deque):
    add_deque = deque(randint(0, 10000) for i in range(10))
    for i in range(0, 1000):
        my_deque.extendleft(add_deque)


print("list extendleft", timeit("check_list_extendleft(new_lst)", number=200, globals=globals()))
print("deque extendleft", timeit("check_deque_extendleft(new_deque)", number=200, globals=globals()))

"""
Операция list extendleft намного медленнее, чем deque extendleft
list extendleft 14.9917072
deque extendleft 0.044279500000001804
"""


def list_get(my_lst, idx):
    return my_lst[idx]


def deque_get(my_deque, idx):
    return my_deque[idx]


def check_list_get(my_lst):
    for i in range(0, 10000):
        list_get(my_lst, randint(1, 10))


def check_deque_get(my_deque):
    for i in range(0, 10000):
        deque_get(my_deque, randint(1, 10))


print("list get", timeit("check_list_get(new_lst)", number=200, globals=globals()))
print("deque get", timeit("check_deque_get(new_deque)", number=200, globals=globals()))

"""
Время обращения по индексу у list get  и у deque get примерно одинаковое
list get 2.2448137999999958
deque get 2.1987516000000014
"""

"""
Итоговый вывод
Дека везде быстрее
Но! Если необходимо использовать операции appendleft, popleft, extendleft то конечно стоит пользоваься деком .
Так как у этих операций скорость выполнения намного больше.
"""
