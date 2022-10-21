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

list_ = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
deque_ = deque(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])


# 1)

def func_1():
    for i in range(11, 20):
        list_.append(i)


print(f'Append списка: {timeit(stmt="func_1()", globals=globals(), number=10000)}')


def func_2():
    for i in range(11, 20):
        deque_.append(i)


print(f'Append очереди: {timeit(stmt="func_2()", globals=globals(), number=10000)}')


def func_3():
    for i in range(11, 20):
        list_.pop()


print(f'Pop списка: {timeit(stmt="func_3()", globals=globals(), number=10000)}')


def func_4():
    for i in range(11, 20):
        deque_.pop()


print(f'Pop очереди: {timeit(stmt="func_4()", globals=globals(), number=10000)}')


def func_5():
    for i in range(11, 20):
        list_.extend('asdffsa')


print(f'Extend списка: {timeit(stmt="func_5()", globals=globals(), number=10000)}')


def func_6():
    for i in range(11, 20):
        deque_.extend('asdffsa')


print(f'Extend очереди: {timeit(stmt="func_6()", globals=globals(), number=10000)}')

'''
Append списка: 0.010232900007395074
Append очереди: 0.008866200005286373 видим, что очередь намного шустрее списка добавляет элементы.
Pop списка: 0.008485300000756979
Pop очереди: 0.008617300001787953
Extend списка: 0.03462240000953898
Extend очереди: 0.03049940000346396
Такие же показатели и с остальными операциями, делаем вывод, что очередь отрабатывает быстрее
'''


# 2)

def func_7():
    for i in range(11, 20):
        deque_.appendleft(i)


def func_8():
    for i in range(11, 20):
        list_.insert(0, i)


def func_9():
    for i in range(11, 20):
        deque_.popleft()


def func_10():
    for i in range(11, 20):
        list_.pop(0)


def func_11():
    for i in range(11, 20):
        deque_.extendleft([1, 2, 3])


def func_12():
    for i in range(11, 20):
        l = [1, 2, 3] + list_


'''
Appendleft очереди: 0.0010180000099353492
Appendleft списка: 7.204640500000096
Popleft очереди: 0.0007266000029630959
Popleft списка: 7.440425199994934
Extendleft очереди: 0.002335600001970306
Extendleft списка: 30.87559809999948
Здесь комментарии излишни, видно, что список не конкурент очереди
'''


# 3)

def func_13():
    for i in range(11, 20):
        a = deque_[0]


def func_14():
    for i in range(11, 20):
        a = list_[0]


print(f'Appendleft очереди: {timeit(stmt="func_7()", globals=globals(), number=1000)}')
print(f'Appendleft списка: {timeit(stmt="func_8()", globals=globals(), number=1000)}')
print(f'Popleft очереди: {timeit(stmt="func_9()", globals=globals(), number=1000)}')
print(f'Popleft списка: {timeit(stmt="func_10()", globals=globals(), number=1000)}')
print(f'Extendleft очереди: {timeit(stmt="func_11()", globals=globals(), number=1000)}')
print(f'Extendleft списка: {timeit(stmt="func_12()", globals=globals(), number=1000)}')
print(f'Получение элемента очереди: {timeit(stmt="func_13()", globals=globals(), number=1000)}')
print(f'Получение элемента списка: {timeit(stmt="func_14()", globals=globals(), number=1000)}')

'''
Получение элемента очереди: 0.000783500014222227
Получение элемента списка: 0.001095500003430061
Получение элемента очереди оказалось быстрее, делаем вывод, что deque быстрее list
'''