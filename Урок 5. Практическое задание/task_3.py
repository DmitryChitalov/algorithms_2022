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
from timeit import timeit

"""1)"""


def append_list(data):
    my_list = []
    for el in range(data):
        my_list.append(el)
    return my_list


def append_deque(data):
    my_deque = deque()
    for el in range(data):
        my_deque.append(el)
    return my_deque


def pop_list():
    my_list = append_list(n)
    for el in range(len(my_list)):
        my_list.pop()
    return my_list


def pop_deque():
    my_deque = append_deque(n)
    for el in range(len(my_deque)):
        my_deque.pop()
    return my_deque


def ext_list():
    my_list = append_list(n)
    my_list.extend([100])
    return my_list


def ext_deque():
    my_deque = append_deque(n)
    my_deque.extend([100])
    return my_deque


"""
В данном примере, операции по формированию списков и очередей, удалению элементов
из них, а также добавлению новых элементов происходило с +/- схожим временем, но в 
пользу очередей в моём случае
"""

"""2)"""


def append_left_list(data):
    my_list_2 = []
    for el in range(data):
        my_list_2.insert(0, el)
    return my_list_2


def append_left_deque(data):
    my_deque_2 = deque()
    for el in range(data):
        my_deque_2.appendleft(el)
    return my_deque_2


def pop_left_list():
    lst = append_left_list(n)
    for el in range(len(lst)):
        lst.pop()
    return lst


def pop_left_deque():
    dq = append_left_deque(n)
    for el in range(len(dq)):
        dq.popleft()
    return dq


def ext_left_list():
    my_list_2 = append_left_list(n)
    my_list_2.extend([100])
    return my_list_2


def ext_left_deque():
    my_deque_2 = append_left_deque(n)
    my_deque_2.extendleft([100])
    return my_deque_2


"""
Произведены соответсвующие замеры функций, которые показали уже более существенное 
превосходство в скорости у операций с очередями! 
"""

"""3)"""


def get_elem_list():
    for el in range(488):
        elem = lst_2[el]
    return elem


def get_elem_deque():
    for el in range(488):
        elem = dq_2[el]
    return elem


"""
Что касается данного замера, то здесь получение элемента из списка происходит быстрее, чем в очереди, 
в связи с тем, что в списке берём по индексу, а в дэке добираемся до элемента в очереди))
"""

n = 500
lst_2 = append_list(n)
dq_2 = append_deque(n)
print("**************************1***************************")

print(f"{timeit('append_list(n)', globals=globals(), number=10000)} >>> {append_list(n)}")
print(f"{timeit('append_deque(n)', globals=globals(), number=10000)} >>> {append_deque(n)}")
print(f"{timeit('pop_list()', globals=globals(), number=10000)} >>> {pop_list()}")
print(f"{timeit('pop_deque()', globals=globals(), number=10000)} >>> {pop_deque()}")
print(f"{timeit('ext_list()', globals=globals(), number=10000)} >>> {ext_list()}")
print(f"{timeit('ext_deque()', globals=globals(), number=10000)} >>> {ext_deque()}")

print("**************************2***************************")

print(f"{timeit('append_left_list(n)', globals=globals(), number=10000)} >>> {append_left_list(n)}")
print(f"{timeit('append_left_deque(n)', globals=globals(), number=10000)} >>> {append_left_deque(n)}")
print(f"{timeit('pop_left_list()', globals=globals(), number=10000)} >>> {pop_left_list()}")
print(f"{timeit('pop_left_deque()', globals=globals(), number=10000)} >>> {pop_left_deque()}")
print(f"{timeit('ext_left_list()', globals=globals(), number=10000)}) >>> {ext_left_list()}")
print(f"{timeit('ext_left_deque()', globals=globals(), number=10000)} >>> {ext_left_deque()}")

print("**************************3***************************")

print(f"{timeit('get_elem_list()', globals=globals(), number=10000)} >>> {get_elem_list()}")
print(f"{timeit('get_elem_deque()', globals=globals(), number=10000)} >>> {get_elem_deque()}")
