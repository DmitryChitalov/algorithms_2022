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

import collections
import timeit

lst = [123, 1, 34245, 32432, 23432, 432134, 23423, 234]
for i in range(1000000):
    lst.append(i)

deq = collections.deque(lst)
"""
Задание 1
"""

print("Добавления элемента в список", timeit.timeit('lst.append(10)', number=1000000, globals=globals()))
print("Добавления элемента в deq", timeit.timeit('deq.append(10)', number=1000000, globals=globals()))
"""
Практически равны
"""
print("\n")

print("POP элемента в список", timeit.timeit('lst.pop()', number=1000000, globals=globals()))
print("POP элемента в deq", timeit.timeit('deq.pop()', number=1000000, globals=globals()))
"""
Практически равны
"""
print("\n")

mas = []
for i in range(10000):
    mas.append(i)

print("Extend списока", timeit.timeit('lst.extend(mas)', number=10000, globals=globals()))
print("Extend deq", timeit.timeit('deq.extend(mas)', number=10000, globals=globals()))
"""
Из за оптимизации дека прирост скорости значительный
"""
print("\n")

"""
Задание 2
"""

print("AppendLeft списока", timeit.timeit('lst.insert(0,4)', number=100, globals=globals()))
print("AppendLeft deq", timeit.timeit('deq.appendleft(4)', number=100, globals=globals()))
"""
Из за оптимизации дека прирост скорости значительный в десятки раз
"""
print("\n")

print("Popleft списока", timeit.timeit('lst.pop(0)', number=1, globals=globals()))
print("Popleft deq", timeit.timeit('deq.popleft()', number=100, globals=globals()))
"""
Из за оптимизации дека прирост скорости значительный в сотни раз
"""
print("\n")

print("Popleft deq", timeit.timeit('deq.extendleft(mas)', number=100, globals=globals()))
"""
Отсутствую старндартные средства для расширения массива с лева. Прийдется писать свой код для 
вставки в массив с лева.
"""

print("\n")

"""
Задание 2
"""

print("Получение элемента списока", timeit.timeit('lst[4]', number=100000000, globals=globals()))
print("Получение элемента deq", timeit.timeit('deq[4]', number=100000000, globals=globals()))
"""
Получения элемента из списка незначильно быстрее получения элмента из дека
"""
print("\n")
