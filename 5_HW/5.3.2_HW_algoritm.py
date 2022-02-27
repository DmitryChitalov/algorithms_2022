"""
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""
from timeit import timeit
from collections import deque

just_list = [i for i in range(1000)]
just_deque = deque([i for i in range(1000)])
count = 1000

"""Во всех проделанных операций быстрее работает Дэк"""

# ______________Операция appendleft (добавление элементов в начало) во много раз быстрее происходит у дэка


# Добавление элементов в список в начало
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# append_list_left ---- 0.051382599999999994
def append_list_left(my_list):
    for i in range(count):
        my_list.insert(0, i)
    return my_list


append_list_left(just_list.copy())


# Добавление элементов в дэк
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# append_deque_left ---- 0.0028789000000000037
def append_deque_left(my_deque):
    for i in range(count):
        my_deque.appendleft(i)
    return my_deque


append_deque_left(just_deque.copy())


# ______________Операция extendleft (добавление списка в начало) во много раз быстрее происходит у дэка


ex_list = [i for i in range(count)]


# Добавление списка в список в начало
# extend_list_left ---- 0.1157607
def extend_list_left(list_1, list_2):
    for i in list_2:
        list_1.insert(0, i)



extend_list_left(just_list.copy(), ex_list.copy())


# Добавление списка в дэк
# deque([3, 2, 1, 0, 3, 2, 1, 0])
# extend_deque_left ---- 0.0022000000000000075
def extend_deque_left(deque_1, deque_2):
    deque_1.extendleft(deque_2)



extend_deque_left(just_deque.copy(), ex_list.copy())


# ______________Операция popleft (удаление элементов в начале) быстрее у дэка


# Удаление элементов в списке
# pop_list_left ---- 0.023932300000000017
def pop_list_left(my_list):
    for _ in range(count):
        my_list.pop(0)
    return my_list


pop_list_left((just_list.copy()))


# удаление элементов в дэке
# pop_deque_left ---- 0.005602700000000016
def pop_deque_left(my_deque):
    for _ in range(count):
        my_deque.pop()
    return my_deque


pop_deque_left((just_deque.copy()))


print(f'append_list_left ---- {timeit("append_list_left(just_list.copy())", globals=globals(), number=40)}')
print(f'append_deque_left ---- {timeit("append_deque_left(just_deque.copy())", globals=globals(), number=40)}')

print(f'extend_list_left{timeit("extend_list_left(just_list.copy(), ex_list.copy())", globals=globals(), number=90)}')
print(f'extend_deque_lef{timeit("extend_deque_left(just_deque.copy(), ex_list.copy())", globals=globals(), number=90)}')

print(f'pop_list_left ---- {timeit("pop_list_left(just_list.copy())", globals=globals(), number=90)}')
print(f'pop_deque_left ---- {timeit("pop_deque_left(just_deque.copy())", globals=globals(), number=90)}')
