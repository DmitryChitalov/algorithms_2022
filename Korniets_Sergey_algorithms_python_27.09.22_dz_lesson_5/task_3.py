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

normal_list = [i for i in range(10000)]
normal_deque = deque([i for i in range(10000)])
elem = 1000


# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы, что и где быстрее

def append_list(normal_list):
    for i in range(elem):
        normal_list.append(i)
    return normal_list


def append_deque(normal_deque):
    for i in range(elem):
        normal_deque.append(i)
    return normal_deque


print('Замеры функции append для list')
print(timeit('append_list(normal_list.copy())', globals=globals(), number=1000))  # 0.09573989998898469, 0.10267230001045391
print('Замеры функции append для deque')
print(timeit('append_deque(normal_deque.copy())', globals=globals(), number=1000))  # 0.1593601999920793, 0.1504166999948211
print('-' * 50)


def pop_list(normal_list):
    for i in range(elem):
        normal_list.pop()
    return normal_list


def pop_deque(normal_deque):
    for i in range(elem):
        normal_deque.pop()
    return normal_deque


print('Замеры функции pop для list')
print(timeit('pop_list(normal_list.copy())', globals=globals(), number=1000))  # 0.07415150001179427, 0.07461970002623275
print('Замеры функции pop для deque')
print(timeit('pop_deque(normal_deque.copy())', globals=globals(), number=1000))  # 0.13166610000189394, 0.13638390001142398
print('-' * 50)


def extend_list(normal_list):
    for i in range(elem):
        normal_list.extend([1, 2, 3])
    return normal_list


def extend_deque(normal_deque):
    for i in range(elem):
        normal_deque.extend([1, 2, 3])
    return normal_deque


print('Замеры функции extend для list')
print(timeit('extend_list(normal_list.copy())', globals=globals(), number=1000))  # 0.13061790002393536, 0.13864679998368956
print('Замеры функции extend для deque')
print(timeit('extend_list(normal_deque.copy())', globals=globals(), number=1000))  # 0.24488129999372177, 0.241495299997041
print('-' * 50)

'''Выводы
Функции append, рор, extend выполняется быстрее в list , чем в deque
'''


# 2) сравнить операции
# appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее


def appendleft_list(normal_list):
    for i in range(elem):
        normal_list.insert(0, i)
    return normal_list


def appendleft_deque(normal_deque):
    for i in range(elem):
        normal_deque.appendleft(i)
    return normal_deque


print('Замеры функции appendleft для list')
print(timeit('appendleft_list(normal_list.copy())', globals=globals(), number=1000))  # 4.135610800003633, 4.162483899999643
print('Замеры функции appendleft для deque')
print(timeit('appendleft_list(normal_deque.copy())', globals=globals(), number=1000))  # 0.17796959998668171, 0.1783931000099983
print('-' * 50)


def popleft_list(normal_list):
    for i in range(elem):
        normal_list.pop(i)
    return normal_list


def popleft_deque(normal_deque):
    for i in range(elem):
        normal_deque.popleft()
    return normal_deque



print('Замеры функции popleft для list')
print(timeit('popleft_list(normal_list.copy())', globals=globals(), number=1000))  # 1.6790553999890108, 1.6630890000087675
print('Замеры функции popleft для deque')
print(timeit('popleft_deque(normal_deque.copy())', globals=globals(), number=1000))  # 0.17390510000404902, 0.1395401999761816
print('-' * 50)


def extendleft_list(normal_list):
    for i in range(elem):
        normal_list.extend([1, 2, 3])
        normal_list.sort()
    return normal_list



def extendleft_deque(normal_deque):
    for i in range(elem):
        normal_deque.extendleft([1, 2, 3])
    return normal_deque


print('Замеры функции extendleft для list')
print(timeit('extendleft_list(normal_list.copy())', globals=globals(), number=100))  # 5.571673300000839, 5.770495700009633
print('Замеры функции extendleft_deque для deque')
print(timeit('extendleft_deque(normal_deque.copy())', globals=globals(), number=100))  # 0.023057799990056083, 0.023916900012409315
print('-' * 50)

'''Выводы
Все функции, которые взаимодействуют с началом массива быстрее выполняются в deque
'''

# 3) сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее


def get_element_list(normal_list):
    for i in range(elem):
        x = normal_list[i]


def get_element_deque(normal_deque):
    for i in range(elem):
        x = normal_deque[i]


print('Замеры функции get_element_list() для list')
print(timeit('get_element_list(normal_list.copy())', globals=globals(), number=1000))  # 0.06486119999317452, 0.06682249999721535
print('Замеры функции get_element_deque для deque')
print(timeit('get_element_deque(normal_deque.copy())', globals=globals(), number=1000))  # 0.13895960000809282, 0.1400761999830138
print('-' * 50)

'''Выводы
Получение элемента по индексу быстрее проходит в list, чем в deque
'''
