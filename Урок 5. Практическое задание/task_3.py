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
соответствует действительности.

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
from random import randint


lst = [randint(0,100) for i in range(0, 20)]
deq = deque(lst)
ext_lst = [randint(0,100) for i in range(0, 10)]
print(lst)

#1  Добавление, удаление (конец)

for el in ext_lst:
    lst.append(el)
for el in ext_lst:
    deq.append(el)


for i in range(0, len(lst)):
    lst.pop()
for i in range(0, len(deq)):
    deq.pop()

count = 0
while count < 10:
    lst.extend(ext_lst)
    count += 1

count = 0
while count < 10:
    deq.extend(ext_lst)
    count += 1

print(len(lst))
print(len(deq))

#2 Добавление, удаление (в начало)

for el in ext_lst:
    lst.insert(0, el)
for el in ext_lst:
    deq.appendleft(el)

for i in range(0, len(lst)):
    lst.pop(0)
for i in range(0, len(deq)):
    deq.popleft()

i = 0
while i < 10:
    for el in ext_lst:
        lst.insert(0, el)
    i += 1

i = 0
while i < 10:
    deq.extendleft(ext_lst)
    i += 1

print(len(lst))
print(len(deq))

#3 Получение элемента

for i in lst:
    el = lst[i]

for i in deq:
    el = deq[i]

print(len(lst))
print(len(deq))

# ________________________________________________________________________

# lst = ['computers', 'lamps', 'mouses', 'tables', 'chairs']
# deq = deque(lst)
# ext_lst = ['monitors', 'pencils', 'paints']


# #1  Добавление, удаление (конец)
#
# lst.append('books')
# lst.append('papers')
# deq.append('books')
# deq.append('papers')
#
# lst.pop()
# deq.pop()
#
# lst.extend(ext_lst)
# deq.extend(ext_lst)
#
# print(lst)
# print(deq)
#
# #2 Добавление, удаление (в начало)
#
# lst.insert(0, 'notebooks')
# deq.appendleft('notebooks')
#
# lst.pop(0)
# deq.popleft()
#
# new_lst = lst
# for i in ext_lst:
#     new_lst.insert(0, i)
#
# deq.extendleft(ext_lst)
#
# # print(lst)
# print(new_lst)
# print(deq)
#
#
# #3 Получение элемента
# el = lst[2]
# el_deq = deq[2]
#
#
# print(el)
# print(el_deq)
#
#
