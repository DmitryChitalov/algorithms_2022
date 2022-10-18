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

lis = [i for i in range(1000)]
deq = deque(lis)

#1


def append_lst(lis):
    for i in range(100):
        lis.append(i)
    return lis


def append_deq_lst(deq):
    for i in range(100):
        deq.append(i)
    return deq


def pop_lst(lis):
    for i in range(10000):
        lis.pop(i)
    return lis


def pop_deq_lst(deq):
    for i in range(10000):
        deq.pop()
    return deq


def extand_lst(lis, lis_2):
    for i in range(100):
        lis.extand(lis_2)
    return lis


def extand_deq_lst(deq, deq_2=deque()):
    for i in range(100):
        deq.extand(deq_2)
    return deq


print(timeit("append_lst", globals=globals()))     #0.009027333000631188
print(timeit("append_deq_lst", globals=globals())) #0.009847041999615612
print(timeit("pop_lst", globals=globals()))        #0.009327500000334112
print(timeit("pop_deq_lst", globals=globals()))    #0.008634374999928696
print(timeit("extand_lst", globals=globals()))     #0.008489667000707414
print(timeit("extand_deq_lst", globals=globals())) #0.008729416000278434


"""
Вывод: функции append, pop, extend по времени работают примерно однаково у дек и списка.
"""

#2

def insert_lst(lis):
    for i in range(1000):
        lis.insert(0, i)
    return lis


def appendleft_deq_lst(deq):
    for i in range(1000):
        deq.appendleft(0, i)
    return deq


def popleft_lst(lis):
    for i in range(1000):
        lis.pop(i)
    return lis


def popleft_deq_lst(deq):
    for i in range(1000):
        deq.popleft()
    return deq


def extendleft_lst(lis, lis_2):
    for i in range(1000):
        for i in lis_2:
            lis.insert(0, i)
        return lis_2


def extendleft_deq_lst(deq):
    for i in range(1000):
        deq.extendleft(i)
    return deq


print(timeit("insert_lst", globals=globals()))          #0.008575250000831147
print(timeit("appendleft_deq_lst", globals=globals()))  #0.009363500000290514
print(timeit("popleft_lst", globals=globals()))         #0.009650332999422972
print(timeit("popleft_deq_lst", globals=globals()))     #0.008462625000196567
print(timeit("extendleft_lst", globals=globals()))      #0.010618374999969092
print(timeit("extendleft_deq_lst", globals=globals()))  #0.00835962500009191

"""
Вывод: исполнение операции дека popleft, extendleft производится
быстрей, чем соответствующие операций списка. У операция appendleft наоборот список быстрее.
"""
#3


def el_from_lst(x):
    for i in range(len(lis)):
        lis[i] = x
    return x


def el_from_deq_lst(x):
    for i in range(len(deq)):
        deq[i] = x
    return x


print(timeit("el_from_lst", globals=globals()))     #0.008397916999660083
print(timeit("el_from_deq_lst", globals=globals())) #0.009618833000582526

"""
Вывод: извлечение элемента из списка быстрее, чем из дека.
"""