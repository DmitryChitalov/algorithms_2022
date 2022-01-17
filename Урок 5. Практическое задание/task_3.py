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
import collections
from timeit import timeit
from collections import deque

list1 = ['1', '2', '3']
deque1 = ['1', '2', '3']
deque1 = collections.deque(deque1)


#
#
# def func_list_1():
#     list1.append('2')
#
#
# print(timeit(
#     "func_list_1()",
#     setup='from __main__ import func_list_1',
#     number=10000))
# " list1.append('2') 0.00214990000000001"
#
#
# def func_list_2():
#     list1.pop()
#
#
# print(timeit(
#     "func_list_2()",
#     setup='from __main__ import func_list_2',
#     number=10000))
# "list1.pop() 0.0021486000000000005"
#
#
# def func_list_3():
#     list1.extend('1')
#
#
# print(timeit(
#     "func_list_3()",
#     setup='from __main__ import func_list_3',
#     number=10000))
# 'list1.extend(1) 0.0033667000000000002'
#
#
# def func_deque_1():
#     deque1.append('1')
#
#
# print(timeit(
#     "func_deque_1()",
#     setup='from __main__ import func_deque_1',
#     number=10000))
# 'deque1.append("1") 0.0018883999999999984'
#
#
# def func_deque_2():
#     deque1.pop()
#
#
# print(timeit(
#     "func_deque_2()",
#     setup='from __main__ import func_deque_2',
#     number=10000))
# 'deque1.pop() 0.002039199999999991'
#
#
# def func_deque_3():
#     deque1.extend('1')
#
#
# print(timeit(
#     "func_deque_3()",
#     setup='from __main__ import func_deque_3',
#     number=10000))
# 'deque1.extend("1") 0.002933999999999992'

############################"2 задание"##################################

# def func_list_2_1():
#     list1.insert(0, '2')
#
#
# print(timeit(
#     "func_list_2_1()",
#     setup='from __main__ import func_list_2_1',
#     number=10000))
# " list1.insert() 0.031069799999999995"


# def func_list_2_2():
#     list3.pop(0)
#
#
# print(timeit(
#     "func_list_2_2()",
#     setup='from __main__ import func_list_2_2',
#     number=3))
# "list1.pop() 2.300000000003688e-06"
# 'чем больше циклов, тем сложнее становится поиск О(n)'

# def func_list_2_3():
#     return ['2', '2', '2'] + list1
#
#
# print(timeit(
#     "func_list_2_3()",
#     setup='from __main__ import func_list_2_3',
#     number=10000))
# 'list1.extend() 0.002748500000000001'

# def func_deque_2_1():
#     deque1.appendleft('1')
#
#
# print(timeit(
#     "func_deque_2_1()",
#     setup='from __main__ import func_deque_2_1',
#     number=10000))
# 'deque1.appendleft("1") 0.016792300000000003'
#
#
# def func_deque_2_2():
#     deque1.popleft()
#
#
# print(timeit(
#     "func_deque_2_2()",
#     setup='from __main__ import func_deque_2_2',
#     number=10000))
# 'deque1.popleft() 0.0019679000000000016'
#
#
# def func_deque_2_3():
#     deque1.extendleft('1')
#
#
# print(timeit(
#     "func_deque_2_3()",
#     setup='from __main__ import func_deque_2_3',
#     number=10000))
# 'deque1.extendleft("1") 0.003035900000000001'

#####################"3 задание"#####################

# def func_list1():
#     return list1[list1.index(x)]
#
#
# x = '2'
# print(func_list1())
# print(timeit(
#     "func_list1()",
#     setup='from __main__ import func_list1',
#     number=10000))
# 'deque1.extendleft("1") 0.002804899999999999'


def func_deque1():
    return deque1[deque1.index(x)]


x = '2'
print(func_deque1())
print(timeit(
    "func_deque1()",
    setup='from __main__ import func_deque1',
    number=10000))
'deque1.extendleft("1") 0.0032041999999999973'

"Очередь работает медленнее чем лист, поиск по индексу дольше "
import collections
from timeit import timeit
from collections import deque

list1 = ['1', '2', '3']
deque1 = ['1', '2', '3']
deque1 = collections.deque(deque1)


#
#
# def func_list_1():
#     list1.append('2')
#
#
# print(timeit(
#     "func_list_1()",
#     setup='from __main__ import func_list_1',
#     number=10000))
# " list1.append('2') 0.00214990000000001"
#
#
# def func_list_2():
#     list1.pop()
#
#
# print(timeit(
#     "func_list_2()",
#     setup='from __main__ import func_list_2',
#     number=10000))
# "list1.pop() 0.0021486000000000005"
#
#
# def func_list_3():
#     list1.extend('1')
#
#
# print(timeit(
#     "func_list_3()",
#     setup='from __main__ import func_list_3',
#     number=10000))
# 'list1.extend(1) 0.0033667000000000002'
#
#
# def func_deque_1():
#     deque1.append('1')
#
#
# print(timeit(
#     "func_deque_1()",
#     setup='from __main__ import func_deque_1',
#     number=10000))
# 'deque1.append("1") 0.0018883999999999984'
#
#
# def func_deque_2():
#     deque1.pop()
#
#
# print(timeit(
#     "func_deque_2()",
#     setup='from __main__ import func_deque_2',
#     number=10000))
# 'deque1.pop() 0.002039199999999991'
#
#
# def func_deque_3():
#     deque1.extend('1')
#
#
# print(timeit(
#     "func_deque_3()",
#     setup='from __main__ import func_deque_3',
#     number=10000))
# 'deque1.extend("1") 0.002933999999999992'

############################"2 задание"##################################

# def func_list_2_1():
#     list1.insert(0, '2')
#
#
# print(timeit(
#     "func_list_2_1()",
#     setup='from __main__ import func_list_2_1',
#     number=10000))
# " list1.insert() 0.031069799999999995"


# def func_list_2_2():
#     list3.pop(0)
#
#
# print(timeit(
#     "func_list_2_2()",
#     setup='from __main__ import func_list_2_2',
#     number=3))
# "list1.pop() 2.300000000003688e-06"
# 'чем больше циклов, тем сложнее становится поиск О(n)'

# def func_list_2_3():
#     return ['2', '2', '2'] + list1
#
#
# print(timeit(
#     "func_list_2_3()",
#     setup='from __main__ import func_list_2_3',
#     number=10000))
# 'list1.extend() 0.002748500000000001'

# def func_deque_2_1():
#     deque1.appendleft('1')
#
#
# print(timeit(
#     "func_deque_2_1()",
#     setup='from __main__ import func_deque_2_1',
#     number=10000))
# 'deque1.appendleft("1") 0.016792300000000003'
#
#
# def func_deque_2_2():
#     deque1.popleft()
#
#
# print(timeit(
#     "func_deque_2_2()",
#     setup='from __main__ import func_deque_2_2',
#     number=10000))
# 'deque1.popleft() 0.0019679000000000016'
#
#
# def func_deque_2_3():
#     deque1.extendleft('1')
#
#
# print(timeit(
#     "func_deque_2_3()",
#     setup='from __main__ import func_deque_2_3',
#     number=10000))
# 'deque1.extendleft("1") 0.003035900000000001'

#####################"3 задание"#####################

# def func_list1():
#     return list1[list1.index(x)]
#
#
# x = '2'
# print(func_list1())
# print(timeit(
#     "func_list1()",
#     setup='from __main__ import func_list1',
#     number=10000))
# 'deque1.extendleft("1") 0.002804899999999999'


def func_deque1():
    return deque1[deque1.index(x)]


x = '2'
print(func_deque1())
print(timeit(
    "func_deque1()",
    setup='from __main__ import func_deque1',
    number=10000))
'deque1.extendleft("1") 0.0032041999999999973'

"Очередь работает медленнее чем лист, поиск по индексу дольше "
import collections
from timeit import timeit
from collections import deque

list1 = ['1', '2', '3']
deque1 = ['1', '2', '3']
deque1 = collections.deque(deque1)


#
#
# def func_list_1():
#     list1.append('2')
#
#
# print(timeit(
#     "func_list_1()",
#     setup='from __main__ import func_list_1',
#     number=10000))
# " list1.append('2') 0.00214990000000001"
#
#
# def func_list_2():
#     list1.pop()
#
#
# print(timeit(
#     "func_list_2()",
#     setup='from __main__ import func_list_2',
#     number=10000))
# "list1.pop() 0.0021486000000000005"
#
#
# def func_list_3():
#     list1.extend('1')
#
#
# print(timeit(
#     "func_list_3()",
#     setup='from __main__ import func_list_3',
#     number=10000))
# 'list1.extend(1) 0.0033667000000000002'
#
#
# def func_deque_1():
#     deque1.append('1')
#
#
# print(timeit(
#     "func_deque_1()",
#     setup='from __main__ import func_deque_1',
#     number=10000))
# 'deque1.append("1") 0.0018883999999999984'
#
#
# def func_deque_2():
#     deque1.pop()
#
#
# print(timeit(
#     "func_deque_2()",
#     setup='from __main__ import func_deque_2',
#     number=10000))
# 'deque1.pop() 0.002039199999999991'
#
#
# def func_deque_3():
#     deque1.extend('1')
#
#
# print(timeit(
#     "func_deque_3()",
#     setup='from __main__ import func_deque_3',
#     number=10000))
# 'deque1.extend("1") 0.002933999999999992'

############################"2 задание"##################################

# def func_list_2_1():
#     list1.insert(0, '2')
#
#
# print(timeit(
#     "func_list_2_1()",
#     setup='from __main__ import func_list_2_1',
#     number=10000))
# " list1.insert() 0.031069799999999995"


# def func_list_2_2():
#     list3.pop(0)
#
#
# print(timeit(
#     "func_list_2_2()",
#     setup='from __main__ import func_list_2_2',
#     number=3))
# "list1.pop() 2.300000000003688e-06"
# 'чем больше циклов, тем сложнее становится поиск О(n)'

# def func_list_2_3():
#     return ['2', '2', '2'] + list1
#
#
# print(timeit(
#     "func_list_2_3()",
#     setup='from __main__ import func_list_2_3',
#     number=10000))
# 'list1.extend() 0.002748500000000001'

# def func_deque_2_1():
#     deque1.appendleft('1')
#
#
# print(timeit(
#     "func_deque_2_1()",
#     setup='from __main__ import func_deque_2_1',
#     number=10000))
# 'deque1.appendleft("1") 0.016792300000000003'
#
#
# def func_deque_2_2():
#     deque1.popleft()
#
#
# print(timeit(
#     "func_deque_2_2()",
#     setup='from __main__ import func_deque_2_2',
#     number=10000))
# 'deque1.popleft() 0.0019679000000000016'
#
#
# def func_deque_2_3():
#     deque1.extendleft('1')
#
#
# print(timeit(
#     "func_deque_2_3()",
#     setup='from __main__ import func_deque_2_3',
#     number=10000))
# 'deque1.extendleft("1") 0.003035900000000001'

#####################"3 задание"#####################

# def func_list1():
#     return list1[list1.index(x)]
#
#
# x = '2'
# print(func_list1())
# print(timeit(
#     "func_list1()",
#     setup='from __main__ import func_list1',
#     number=10000))
# 'deque1.extendleft("1") 0.002804899999999999'


def func_deque1():
    return deque1[deque1.index(x)]


x = '2'
print(func_deque1())
print(timeit(
    "func_deque1()",
    setup='from __main__ import func_deque1',
    number=10000))
'deque1.extendleft("1") 0.0032041999999999973'

"Очередь работает медленнее чем лист, поиск по индексу дольше "
