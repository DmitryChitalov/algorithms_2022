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

test_list = []
test_deque = deque()

# 1)
test_data = list(str(98765 ** 99))


def append_test(lst, data):
    for elem in data:
        lst.append(elem)


def pop_test(lst):
    for i in range(1000):
        lst.pop()


def extend_test(lst, data):
    for elem in data:
        lst.extend(elem)


print(timeit("append_test(test_list, test_data)", globals=globals(), number=1000))
print(timeit("append_test(test_deque, test_data)", globals=globals(), number=1000))  # быстрее

print(timeit("pop_test(test_list)", globals=globals(), number=100))
print(timeit("pop_test(test_deque)", globals=globals(), number=100))  # быстрее

print(timeit("extend_test(test_list, test_data)", globals=globals(), number=1000))
print(timeit("extend_test(test_deque, test_data)", globals=globals(), number=1000))  # быстрее

"""
Вывод 1: для операций append, pop и extend дека отрабатывает быстрее списка, что согласуется с документацией
"""


# 2)) сравнить операции
# appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее


def appendleft_list(lst, data):
    for elem in data:
        lst = list(elem) + lst


def appendleft_deque(lst, data):
    for elem in data:
        lst.appendleft(elem)


def popleft_list(lst):
    for i in range(500):
        lst.remove(lst[0])


def popleft_deque(lst):
    for i in range(500):
        lst.popleft()


def extendleft_list(lst, data):
    lst = data + lst


def extendleft_deque(lst, data):
    lst.extendleft(data)


print(timeit("appendleft_list(test_list, test_data)", globals=globals(), number=1))
print(timeit("appendleft_deque(test_deque, test_data)", globals=globals(), number=100))  # быстрее

print(timeit("popleft_list(test_list)", globals=globals(), number=1))
print(timeit("popleft_deque(test_deque)", globals=globals(), number=100))  # быстрее

print(timeit("extendleft_list(test_list, test_data)", globals=globals(), number=1000))
print(timeit("extendleft_deque(test_deque, test_data)", globals=globals(), number=1000))  # быстрее

"""
Вывод 2: встроенные методы деки работают быстрее аналогичных реализаций у списков.
"""


# 3) сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее

def get_elem_test(lst, tst_lst=[]):
    for i in range(1000):
        tst_lst.append(lst[i])


print(timeit("get_elem_test(test_list)", globals=globals(), number=10000))  # быстрее
print(timeit("get_elem_test(test_deque)", globals=globals(), number=10000))

"""
Вывод 3: как и указано в документации, взятие элементов по индексу в списке происходит быстрее чем в деке, 
хотя разница по времени не очень большая.
"""
