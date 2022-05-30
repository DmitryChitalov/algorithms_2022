from collections import deque
import cProfile
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

test_lst = [i for i in range(1000)]
test_deque = deque(test_lst)

"""
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
"""


def lst_append(lst):
    for i in range(10000):
        lst.append(i)


def lst_pop(lst):
    for i in range(10000):
        lst.pop()


def lst_extend(lst):
    for i in range(10000):
        lst.extend([i])


def deq_append(deq):
    for i in range(10000):
        deq.append(i)


def deq_pop(deq):
    for i in range(10000):
        deq.pop()


def deq_extend(deq):
    for i in range(10000):
        deq.extend([i])


def main_1():
    lst_append(test_lst)
    lst_pop(test_lst)
    lst_extend(test_lst)
    deq_append(test_deque)
    deq_pop(test_deque)
    deq_extend(test_deque)


cProfile.run('main_1()')

"""
60010 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
        1    0.001    0.001    0.002    0.002 task_3.py:40(lst_append)
        1    0.001    0.001    0.002    0.002 task_3.py:45(lst_pop)
        1    0.001    0.001    0.002    0.002 task_3.py:50(lst_extend)
        1    0.001    0.001    0.002    0.002 task_3.py:55(deq_append)
        1    0.001    0.001    0.002    0.002 task_3.py:60(deq_pop)
        1    0.001    0.001    0.002    0.002 task_3.py:65(deq_extend)
        1    0.000    0.000    0.012    0.012 task_3.py:70(main_1)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'append' of 'collections.deque' objects}
    10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10000    0.001    0.000    0.001    0.000 {method 'extend' of 'collections.deque' objects}
    10000    0.001    0.000    0.001    0.000 {method 'extend' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'pop' of 'collections.deque' objects}
    10000    0.001    0.000    0.001    0.000 {method 'pop' of 'list' objects}

Вывод:
Согласно результатам замеров разницы между методами append, pop, extend
для списка и дека нет, выполняются с одинаковой скоростью.
"""

"""
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""

def lst_appendleft(lst):
    for i in range(10000):
        lst.insert(0, i)


def lst_popleft(lst):
    for i in range(10000):
        lst.pop(0)


def lst_extendleft(lst):
    for i in range(10000):
        lst.insert(0, [i])


def deq_appendleft(deq):
    for i in range(10000):
        deq.appendleft(i)


def deq_popleft(deq):
    for i in range(10000):
        deq.popleft()


def deq_extendleft(deq):
    for i in range(10000):
        deq.extendleft([i])


def main_2():
    lst_appendleft(test_lst)
    lst_popleft(test_lst)
    lst_extendleft(test_lst)
    deq_appendleft(test_deque)
    deq_popleft(test_deque)
    deq_extendleft(test_deque)


cProfile.run('main_2()')

"""
60010 function calls in 0.125 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.125    0.125 <string>:1(<module>)
        1    0.002    0.002    0.049    0.049 task_3.py:115(lst_appendleft)
        1    0.002    0.002    0.020    0.020 task_3.py:120(lst_popleft)
        1    0.003    0.003    0.050    0.050 task_3.py:125(lst_extendleft)
        1    0.001    0.001    0.002    0.002 task_3.py:130(deq_appendleft)
        1    0.001    0.001    0.002    0.002 task_3.py:135(deq_popleft)
        1    0.001    0.001    0.002    0.002 task_3.py:140(deq_extendleft)
        1    0.000    0.000    0.125    0.125 task_3.py:145(main_2)
        1    0.000    0.000    0.125    0.125 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'appendleft' of 'collections.deque' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10000    0.001    0.000    0.001    0.000 {method 'extendleft' of 'collections.deque' objects}
    20000    0.093    0.000    0.093    0.000 {method 'insert' of 'list' objects}
    10000    0.018    0.000    0.018    0.000 {method 'pop' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'popleft' of 'collections.deque' objects}

Вывод:
методы appendleft, popleft, extendleft дека выполняются быстрее чем 
соответствующие им операции списка
"""

"""
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
"""


def get_elem_lst(lst):
    for i in range(10000):
        a = lst[i]


def get_elem_deq(deq):
    for i in range(10000):
        a = deq[i]


def main_3():
    get_elem_lst(test_lst)
    get_elem_deq(test_deque)


cProfile.run('main_3()')

"""
6 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_3.py:189(get_elem_lst)
        1    0.002    0.002    0.002    0.002 task_3.py:194(get_elem_deq)
        1    0.000    0.000    0.003    0.003 task_3.py:199(main_3)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Вывод: взятие елемента выполняется быстрее у списка
"""
