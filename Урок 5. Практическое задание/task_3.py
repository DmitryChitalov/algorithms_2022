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


from collections import deque
import cProfile


def append_in_lst():
    lst = []
    for i in range(1000000):
        lst.append(i)
    return lst


def pop_in_lst():
    lst = append_in_lst()
    for _ in lst.copy():
        lst.pop()
    return lst


def extend_in_lst():
    lst = []
    for i in range(1000):
        lst.extend(range(1000))
    return lst


def insert_in_lst():
    lst = []
    for i in range(100000):
        lst.insert(0, i)
    return lst


def pop_in_begin_lst():
    lst = list(range(100000))
    for _ in lst.copy():
        lst.pop(0)
    return lst


def append_in_deq():
    deq = deque([])
    for i in range(1000000):
        deq.append(i)
    return deq


def pop_in_deq():
    deq = append_in_deq()
    for _ in deq.copy():
        deq.pop()
    return deq


def extend_in_deq():
    deq = deque([])
    for i in range(1000):
        deq.extend(range(1000))
    return deq


def left_append_in_deq():
    deq = deque([])
    for i in range(100000):
        deq.appendleft(i)
    return deq


def index_in_deq():
    deq = deque(list(range(1000000)))
    for i in range(100000):
        el = deq[i]
        return el


def index_in_lst():
    lst = list(range(1000000))
    for i in range(100000):
        el = lst[i]
        return el


def pop_in_begin_deq():
    deq = deque(list(range(100000)))
    for _ in deq.copy():
        deq.popleft()
    return deq


if __name__ == '__main__':

    def main():
        append_in_lst()
        pop_in_lst()
        extend_in_lst()
        insert_in_lst()
        pop_in_begin_lst()
        append_in_deq()
        pop_in_deq()
        extend_in_deq()
        left_append_in_deq()
        pop_in_begin_deq()
        index_in_deq()
        index_in_lst()

    cProfile.run('main()')


#      ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         2    0.213    0.106    0.355    0.178   task_3.py:34(append_in_lst)
#         1    0.100    0.100    0.342    0.342   task_3.py:41(pop_in_lst)
#         1    0.104    0.104    0.339    0.339   task_3.py:76(pop_in_deq)
#         1    0.000    0.000    0.023    0.023   task_3.py:48(extend_in_lst)
#         1    0.022    0.022    1.564    1.564   task_3.py:55(insert_in_lst)
#         1    0.012    0.012    0.636    0.636   task_3.py:62(pop_in_begin_lst)
#         2    0.210    0.105    0.330    0.165   task_3.py:69(append_in_deq)
#         1    0.000    0.000    0.013    0.013   task_3.py:83(extend_in_deq)
#         1    0.011    0.011    0.016    0.016   task_3.py:90(left_append_in_deq)
#         1    0.002    0.002    0.002    0.002   task_3.py:97(pop_in_begin_deq)
#         1    0.012    0.012    0.012    0.012   task_3.py:104(index_in_lst)
#         1    0.023    0.023    0.023    0.023   task_3.py:97(index_in_deq)
#
#  Добавление нового элемента (или элементов) в конец, удаление с конца осуществляется в примерно одинаково.
#  Добавление нового элемента в начало быстрее в деке.
#  Удаление элемента с начала быстрее в деке.
#  Взятие по индексу осуществляется быстрее в списке, чем в деке.
