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
from random import randint
from timeit import timeit

lst = [randint(1, 20) for i in range(50)]
dque = collections.deque(lst)

lst_append = """
for i in range(100):
    lst.append(i)
"""

dque_append = """
for i in range(100):
    dque.append(i)
"""

lst_extend = """
for i in range(100):
    lst.extend([i,1,2,3,4,5])
"""
dque_extend = """
for i in range(100):
    dque.extend([i,1,2,3,4,5])
"""
lst_pop = """
for i in range(100):
    lst.pop()
"""
dque_pop = """
for i in range(100):
    dque.pop()
"""
print("Сравниваем стандартные операции list и deque")
print('append')
print(timeit(lst_append, globals=globals(), number=1000), end='  ')
print(timeit(dque_append, globals=globals(), number=1000))
print('extend')
print(timeit(lst_extend, globals=globals(), number=1000), end='  ')
print(timeit(dque_extend, globals=globals(), number=1000))
print('pop')
print(timeit(lst_pop, globals=globals(), number=1000), end='  ')
print(timeit(dque_pop, globals=globals(), number=1000))

lst_appendleft = """
for i in range(10):
    lst.insert(0,i)
"""
dque_appendleft = """
for i in range(10):
    dque.appendleft(i)
"""
lst_extendleft = """
for i in range(10):
    lst=[1,2,3,4,5,6]+lst
"""
dque_extendleft = """
for i in range(10):
    dque.extendleft([i,1,2,3,4,5])
"""
lst_popleft = """
for i in range(10):
    a=lst[0]
    del lst[0]
"""
dque_popleft = """
for i in range(10):
    dque.popleft()
"""

print("**********************")
print("Сравниваем левые операции list и deque")
print('append')
print(timeit(lst_appendleft, globals=globals(), number=1000), end='  ')
print(timeit(dque_appendleft, globals=globals(), number=1000))
print('extend')
print(timeit(lst_extendleft, setup='from __main__ import lst', number=100), end='  ')
print(timeit(dque_extendleft, globals=globals(), number=100))
print('pop')
print(timeit(lst_popleft, globals=globals(), number=1000), end='  ')
print(timeit(dque_popleft, globals=globals(), number=1000))

lst_index = """
for i in range(20,100):
    a=lst[i]
"""
dque_index = """
for i in range(20,100):
    a=dque[i]
"""
lst_find = """
for i in range(50,100):
    lst.index(i)
"""
dque_find = """
for i in range(50,100):
    dque.index(i)
"""

print("Сравниваем поиск list и deque")
print('по индексу')
print(timeit(lst_index, globals=globals(), number=1000), end='  ')
print(timeit(dque_index, globals=globals(), number=1000))
print('по значению')
print(timeit(lst_find, globals=globals(), number=100), end='  ')
print(timeit(dque_find, globals=globals(), number=100))

'''
Ожидаемо deque сильно быстрее на операциях слева, времена операций справа сравнимы.
Нахождение элемента по индексу в list быстрее на проценты, а вот поиск по значению
в deque сильно тормозит.

Соответствует спецификации.
'''
