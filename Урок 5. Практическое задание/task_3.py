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

lst = []
lst_deque = deque(lst)
adding_list = ['adding' for i in range(1, 5)]

# -------------------------------------------------------------------------------
#  1) сравнить операции append, pop, extend -------------------------------------


def lst_append():  # В конец списка
    for i in range(1, 10000):
        lst.append(i)


def lst_pop():  # Удаление по индексу
    for i in range(1, 9999):
        lst.pop()


def lst_extend():  # Все элементы в др. список
    for i in range(1, 10000):
        lst.extend(adding_list)


def deque_append():
    for i in range(1, 10000):
        lst_deque.append(i)


def deque_pop():
    for i in range(1, 9999):
        lst_deque.pop()


def deque_extend():
    for i in range(1, 10000):
        lst_deque.extend(adding_list)


print('Скорость выполнения append списка: ', end='')
print(timeit('lst_append()', setup='from __main__ import lst_append, lst', number=1000))
print('Скорость выполнения append deque:  ', end='')
print(timeit('deque_append()', setup='from __main__ import deque_append, lst_deque', number=1000))
print('Скорость выполнения pop списка:    ', end='')
print(timeit('lst_pop()', setup='from __main__ import lst_pop, lst', number=1000))
print('Скорость выполнения pop deque:     ', end='')
print(timeit('deque_pop()', setup='from __main__ import deque_pop, lst_deque', number=1000))
print('Скорость выполнения extend списка: ', end='')
print(timeit('lst_extend()', setup='from __main__ import lst_extend, lst', number=1000))
print('Скорость выполнения extend deque:  ', end='')
print(timeit('deque_extend()', setup='from __main__ import deque_extend, lst_deque', number=1000))

'''
В целом, ощутимой разницы в скорости выполнения append и pop нет.
Но, операция extend deque в 1,5 раза быстрее чем для списка.
    Скорость выполнения append списка: 0.7377967999782413
    Скорость выполнения append deque:  0.5379500000271946
    Скорость выполнения pop списка:    0.5532398000359535
    Скорость выполнения pop deque:     0.5246504999813624
    Скорость выполнения extend списка: 1.4352625000174157
    Скорость выполнения extend deque:  0.9965021000243723
'''
print('-----------------------------------------------------------------------------')

# -------------------------------------------------------------------------------------------
#  2) сравнить операции appendleft, popleft, extendleft -------------------------------------

lst.clear()
lst_deque.clear()

def lst_insert():
    for i in range(1, 100):
        lst.insert(0, i)


def lst_pop_left():
    for i in range(1, 99):
        lst.pop(0)


def lst_extend_left():
    for i in range(1, 100):
        for j in range(len(adding_list)):
            lst.insert(0, adding_list[j])


def deque_appendleft():
    for i in range(1, 100):
        lst_deque.appendleft(i)


def deque_popleft():
    for i in range(1, 99):
        lst_deque.popleft()


def deque_extendleft():
    for i in range(1, 100):
        lst_deque.extendleft(adding_list)


print('Скорость выполнения insert списка:     ', end='')
print(timeit('lst_insert()', setup='from __main__ import lst_insert, lst', number=1000))
print('Скорость выполнения appendleft deque:  ', end='')
print(timeit('deque_appendleft()', setup='from __main__ import deque_appendleft, lst_deque', number=1000))
print('Скорость выполнения pop списка:        ', end='')
print(timeit('lst_pop_left()', setup='from __main__ import lst_pop_left, lst', number=1000))
print('Скорость выполнения poplift deque:     ', end='')
print(timeit('deque_popleft()', setup='from __main__ import deque_popleft, lst_deque', number=1000))
print('Скорость выполнения extend списка:     ', end='')
print(timeit('lst_extend_left()', setup='from __main__ import lst_extend_left, lst', number=100))
print('Скорость выполнения extendleft deque:  ', end='')
print(timeit('deque_extendleft()', setup='from __main__ import deque_extendleft, lst_deque', number=100))

'''
Операции для deque (appendleft, popleft, popleft) заничетльно быстрее анналогичных операция для списка.
    Скорость выполнения insert списка:     1.617312900023535
    Скорость выполнения appendleft deque:  0.004523899988271296
    Скорость выполнения pop списка:        0.8555674999952316
    Скорость выполнения poplift deque:     0.006087800022214651
    Скорость выполнения extend списка:     27.200590200023726
    Скорость выполнения extendleft deque:  0.00887180003337562
'''

print('-----------------------------------------------------------------------------')
# -------------------------------------------------------------------------------------------
#  3) сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее

def extraction_lst():
    for i in range(len(lst)):
        test = lst[i]

def extraction_deque():
    for i in range(len(lst_deque)):
        test = lst_deque[i]


print('Скорость получения элемента списка:', end='')
print(timeit('extraction_lst()', setup='from __main__ import extraction_lst, lst', number=1000))
print('Скорость получения элемента deque: ', end='')
print(timeit('extraction_deque()', setup='from __main__ import extraction_deque, lst', number=1000))

'''
Скорость получения элемента в списке по индексу значительно быстрее.
    Скорость получения элемента списка:1.371283000044059
    Скорость получения элемента deque: 9.645437799976207
'''