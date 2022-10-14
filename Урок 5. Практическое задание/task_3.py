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

my_list = [i for i in range(10 ** 5)]

my_deque = deque([i for i in range(10 ** 5)])

n = 10 ** 4


# сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее

# append
def append_list(some_list):
    for i in range(n):
        some_list.append(i)
    return some_list


# append
def append_deque(some_deque):
    for i in range(n):
        some_deque.append(i)
    return some_deque


# print(timeit("append_list(my_list.copy())", globals=globals(), number=100))  # 0.17446650005877018
# print(timeit("append_deque(my_deque.copy())", globals=globals(), number=100))  # 0.17004949995316565


# pop
def pop_list(some_list):
    for i in range(n):
        some_list.pop()
    return some_list


# pop
def pop_deque(some_deque):
    for i in range(n):
        some_deque.pop()
    return some_deque


# print(timeit("pop_list(my_list.copy())", globals=globals(), number=100))  # 0.131336500053294
# print(timeit("pop_deque(my_deque.copy())", globals=globals(), number=100))  # 0.1309716000687331


# extend
def extend_list(some_list):
    for i in range(n):
        some_list.extend([1, 2, 3])
    return some_list


# extend
def extend_deque(some_deque):
    for i in range(n):
        some_deque.extend([1, 2, 3])
    return some_deque


# print(timeit("extend_list(my_list.copy())", globals=globals(), number=100))  # 0.2577919999603182
# print(timeit("extend_deque(my_deque.copy())", globals=globals(), number=100))  # 0.2849671000149101

"""
Примерно одинаковое время выполнения у всех операций
"""


# сравнить операции
# appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее

# appendleft
def appendleft_list(some_list):
    for i in range(n):
        some_list.insert(0, i)
    return some_list


# appendleft
def appendleft_deque(some_deque):
    for i in range(n):
        some_deque.appendleft(i)
    return some_deque


# print(timeit("appendleft_list(my_list.copy())", globals=globals(), number=100))  # 32.72861540003214
# print(timeit("appendleft_deque(my_deque.copy())", globals=globals(), number=100))  # 0.10327569989021868

"""
Встроенный тип list не оптимизирован для совершения частых вставок в начало списка. 
При осуществлении частых вставок элементов в начало списка или любое другое место (кроме конца списка), 
код будет значительно притормаживать (из за частого изменения индексов элементов списка).
Для оптимизации таких действий, лучше применять двустороннюю очередь collections.deque(). 
"""


# pop
def popleft_list(some_list):
    for i in range(n):
        some_list.pop(i)
    return some_list


# popleft
def popleft_deque(some_deque):
    for i in range(n):
        some_deque.popleft()
    return some_deque


# print(timeit("popleft_list(my_list.copy())", globals=globals(), number=100))  # 13.740709099918604
# print(timeit("popleft_deque(my_deque.copy())", globals=globals(), number=100))  # 0.09592009999323636

"""
Удаление из списка стандартным методом pop выполняется значительно дольше, 
чем при использовании popleft для дека.
"""


# extendleft
def extendleft_list(some_list):
    for i in range(n):
        some_list.extend([1, 2, 3])
        some_list.sort()
    return some_list


# extendleft
def extendleft_deque(some_deque):
    for i in range(n):
        some_deque.extendleft([1, 2, 3])
    return some_deque


# print(timeit("extendleft_list(my_list.copy())", globals=globals(), number=10))  # на 10 итераций - 43.76801390002947
# print(timeit("extendleft_deque(my_deque.copy())", globals=globals(), number=100))  # 0.172807399998419

"""
Вставка нескольких элементов элементов в деке выполняется значительно быстрее.
"""


# сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее

def get_el_list(some_list):
    for i in range(n):
        some_list[i] = i
    return some_list


def get_el_deque(some_deque):
    for i in range(n):
        some_deque[i] = i
    return some_deque


print(timeit("get_el_list(my_list.copy())", globals=globals(), number=10))  # 0.007695000036619604
print(timeit("get_el_deque(my_deque.copy())", globals=globals(), number=100))  # 0.2791145999217406

"""
Замеры показали, что получение элементов списка 
выполняется быстрее, чем получение элемента дека.
Как и указано в документации.
"""
