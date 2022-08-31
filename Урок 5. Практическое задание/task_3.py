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
from timeit import timeit, default_timer


def append_test():
    my_lst = []
    for i in range(1000):
        my_lst.append(i)


def deque_append_test():
    deq_obj = deque()
    for i in range(1000):
        deq_obj.append(i)


"""

Далее для технических целей тестирования функции pop и extend создадим функции формирующие тестовые массивы данных 


"""


def append_test_to_pop():
    my_lst1 = []
    for i in range(1000):
        my_lst1.append(i)
    return my_lst1


def deque_append_test_to_pop():
    deq_obj1 = deque()
    for i in range(1000):
        deq_obj1.append(i)
    return deq_obj1


def pop_test(list1):
    start_time = default_timer()
    for i in range(len(list1)):
        list1.pop()
        i += 1
    duration = default_timer() - start_time
    return duration


def deque_pop_test(deq_obj1):
    start_time1 = default_timer()
    for i in range(len(deq_obj1)):
        deq_obj1.pop()
        i += 1
    duration1 = default_timer() - start_time1
    return duration1


def extend_test(list11, list12):
    start_time2 = default_timer()
    list11.extend(list12)
    duration2 = default_timer() - start_time2
    return duration2


def deque_extend_test(deq_obj11, deq_obj12):
    start_time3 = default_timer()
    deq_obj11.extend(deq_obj12)
    duration3 = default_timer() - start_time3
    return duration3


def appendleft_test():
    my_lst111 = []
    start_time4 = default_timer()
    for i in range(1000):
        my_lst111.insert(0, i)
    duration4 = default_timer() - start_time4
    return duration4


def deque_appendleft_test():
    deq_obj111 = deque()
    start_time5 = default_timer()
    for i in range(1000):
        deq_obj111.appendleft(i)
    duration5 = default_timer() - start_time5
    return duration5


def popleft_test(list122):
    start_time6 = default_timer()
    for i in range(len(list122)):
        list122.pop(0)
        i += 1
    duration6 = default_timer() - start_time6
    return duration6


def deque_popleft_test(deq_obj122):
    start_time7 = default_timer()
    for i in range(len(deq_obj122)):
        deq_obj122.popleft()
        i += 1
    duration7 = default_timer() - start_time7
    return duration7


def extendleft_test(list1133, list1233):
    start_time8 = default_timer()
    list1133.insert(0, list1233)
    duration8 = default_timer() - start_time8
    return duration8


def deque_extendleft_test(deq_obj1133, deq_obj1233):
    start_time9 = default_timer()
    deq_obj1133.extendleft(deq_obj1233)
    duration9 = default_timer() - start_time9
    return duration9


print("________________Сравнение времени функции append________________________")
print(timeit("append_test()", setup="from __main__ import append_test",
             number=1000))
print(timeit("deque_append_test()", setup="from __main__ import deque_append_test",
             number=1000))

lst_test = append_test_to_pop()
dqe_test = deque_append_test_to_pop()
lst_test1 = append_test_to_pop()
dqe_test1 = deque_append_test_to_pop()

print("________________Сравнение времени функции pop________________________")

print(f'Время выполнения операции pop_test: {pop_test(lst_test)}')
print(f'Время выполнения операции deque_pop_test: {deque_pop_test(dqe_test)}')

print("________________Сравнение времени функции extend________________________")

print(f'Время выполнения операции extend_test: {extend_test(lst_test1, lst_test1)}')
print(f'Время выполнения операции deque_extend_test: {deque_extend_test(dqe_test1, dqe_test1)}')

print("________________Сравнение времени функции appendleft________________________")

print(f'Время выполнения операции appendleft_test: {appendleft_test()}')
print(f'Время выполнения операции deque_appendleft_test: {deque_appendleft_test()}')

lst_test2 = append_test_to_pop()
dqe_test2 = deque_append_test_to_pop()
lst_test3 = append_test_to_pop()
dqe_test3 = deque_append_test_to_pop()

print("________________Сравнение времени функции popleft________________________")

print(f'Время выполнения операции popleft_test: {popleft_test(lst_test2)}')
print(f'Время выполнения операции deque_popleft_test: {deque_popleft_test(dqe_test2)}')

print("________________Сравнение времени функции extendleft________________________")

print(f'Время выполнения операции extendleft_test: {extendleft_test(lst_test3, lst_test3)}')
print(f'Время выполнения операции deque_extendleft_test: {deque_extendleft_test(dqe_test3, dqe_test3)}')

print("________________Сравнение времени получения 1 элемента________________________")
start_time10 = default_timer()
m = lst_test3[500]
print(default_timer() - start_time10)
start_time11 = default_timer()
n = dqe_test3[500]
print(default_timer() - start_time11)

"""

Вывод 1: методы append, pop и extend при замерах времени чуть быстрее отрабатывает для списка, чем для дека 
(поэтому в случаях, когда требуется типовое расширение списка справа 
лучше использовать стандартные списки)

Вывод 2: appendleft, popleft  для дека при замерах времени выдают
меньшие значения чем соответствующие им функции списка (т.к. имеют константную сложность, 
в отличие от линейной для списков),  а метод списка, соответствующий методу extendleft дека 
отрабатывает для списка быстрее, чем для дека 
(поэтому в случаях, когда требуется расширение списка слева на готовый список, а не отдельные значения
лучше использовать стандартные списки).

Вывод 3: получение элемента списка медленнее, чем получение элемента дека, поэтому когда требуется 
индексированное получение элемента лучше использовать deque


"""
