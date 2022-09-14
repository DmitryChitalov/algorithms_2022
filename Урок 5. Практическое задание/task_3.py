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


def sep():
    print("_" * 75)


lst = [i for i in range(1000)]
deq_lst = deque(lst)

"""
1) Сравение операций append, pop, extend списка и дека
"""


def append_lst(lst):
    for i in range(100):
        lst.append(i)
    return lst


def append_deq_lst(deq_lst):
    for i in range(100):
        deq_lst.append(i)
    return deq_lst


def pop_lst(lst):
    for i in range(10000):
        lst.pop(i)
    return lst


def pop_deq_lst(deq_lst):
    for i in range(10000):
        deq_lst.pop()
    return deq_lst


def extand_lst(lst, lst_2):
    for i in range(100):
        lst.extand(lst_2)
    return lst


def extand_deq_lst(deq_lst, deq_lst_2=deque()):
    for i in range(100):
        deq_lst.extand(deq_lst_2)
    return deq_lst


print(timeit("append_lst", globals=globals()))      # 0.023968699970282614
print(timeit("append_deq_lst", globals=globals()))  # 0.02210699999704957
print(timeit("pop_lst", globals=globals()))         # 0.02203150000423193
print(timeit("pop_deq_lst", globals=globals()))     # 0.024970199912786484
print(timeit("extand_lst", globals=globals()))      # 0.03091239999048412
print(timeit("extand_deq_lst", globals=globals()))  # 0.019949399982579052

"""
Вывод: функции append, pop, extend по времени работают однаково у дек и списка.
"""
sep()

"""
2) Сравнение операций appendleft, popleft, extendleft дека и соответствующих им операций списка
"""


def insert_lst(lst):
    for i in range(1000):
        lst.insert(0, i)
    return lst


def appendleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.appendleft(0, i)
    return deq_lst


def popleft_lst(lst):
    for i in range(1000):
        lst.pop(i)
    return lst


def popleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.popleft()
    return deq_lst


def extendleft_lst(lst, lst_2):
    for i in range(1000):
        for i in lst_2:
            lst.insert(0, i)
        return lst_2


def extendleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.extendleft(i)
    return deq_lst


print(timeit("insert_lst", globals=globals()))          # 0.021939300000667572
print(timeit("appendleft_deq_lst", globals=globals()))  # 0.02072909998241812
print(timeit("popleft_lst", globals=globals()))         # 0.0200627000303939
print(timeit("popleft_deq_lst", globals=globals()))     # 0.0198017000220716
print(timeit("extendleft_lst", globals=globals()))      # 0.021646800101734698
print(timeit("extendleft_deq_lst", globals=globals()))  # 0.021319599938578904

"""
Вывод: исполнение операции дека appendleft, popleft, extendleft производится быстрей,
чем соответствующие операций списка
"""

sep()

"""
3) Сравнение операций получения элемента списка и дека
"""


def el_from_lst(x):
    for i in range(len(lst)):
        lst[i] = x
    return x


def el_from_deq_lst(x):
    for i in range(len(deq_lst)):
        deq_lst[i] = x
    return x


print(timeit("el_from_lst", globals=globals()))      # 0.021423200028948486
print(timeit("el_from_deq_lst", globals=globals()))  # 0.020857700030319393

"""
Вывод: извлечение элемента быстрей происходит из списка, чем из дека.
"""
