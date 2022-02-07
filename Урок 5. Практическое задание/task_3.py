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
from timeit import default_timer
from collections import deque


def time_it(n):
    def deco(func):
        def wrapper(*args):
            t_sum = 0
            for el in range(n):
                start_time = default_timer()
                func(*args)
                delta = default_timer() - start_time
                t_sum += delta
            return f'{func.__name__}: {t_sum}'
        return wrapper
    return deco


just_list = []
just_deque = deque(just_list)


@time_it(100)
def deque_append(number):
    for i in range(number):
        just_deque.append(i)
    return just_deque


@time_it(100)
def deque_extend(number):
    for i in range(number):
        just_deque.extend([i])
    return just_deque


@time_it(100)
def deque_pop(number):
    for i in range(number):
        just_deque.pop()
    return just_deque


@time_it(100)
def list_append(number):
    for i in range(number):
        just_list.append(i)
    return just_list


@time_it(100)
def list_extend(number):
    for i in range(number):
        just_list.extend([i])
    return just_list


@time_it(100)
def list_pop(number):
    for i in range(number):
        just_list.pop()
    return just_list


@time_it(100)
def deque_appendleft(number):
    for i in range(number):
        just_deque.appendleft(i)
    return just_deque


@time_it(100)
def deque_extendleft(number):
    for i in range(number):
        just_deque.extendleft([i])
    return just_deque


@time_it(100)
def deque_popleft(number):
    for i in range(number):
        just_deque.popleft()
    return just_deque


@time_it(100)
def list_appendleft(number):
    for i in range(number):
        just_list.insert(0, i)
    return just_list


@time_it(100)
def list_extendleft(number):
    for i in range(number):
        just_list.insert(0, [i])
    return just_list


@time_it(100)
def list_popleft(number):
    for i in range(number):
        just_list.pop(0)
    return just_list


@time_it(100)
def deque_getting(number):
    for i in range(number):
        just_deque[i] = i
    return just_deque


@time_it(100)
def list_getting(number):
    for i in range(number):
        just_list[i] = i
    return just_list


print(deque_append(1000))
print(list_append(1000), '\n')
print(deque_extend(1000))
print(list_extend(1000), '\n')
print(deque_pop(1000))
print(list_pop(1000), '\n')
print(deque_appendleft(1000))
print(list_appendleft(1000), '\n')
print(deque_extendleft(1000))
print(list_extendleft(1000), '\n')
print(deque_popleft(1000))
print(list_popleft(1000), '\n')
print(deque_getting(1000))
print(list_getting(1000), '\n')

print('Вывод: список имеет очень небольшое преимущество по времени (и то не всегда, \n'
      'но в нескольких прогонах зачастую список был быстрее) перед деком в операциях вставки справа, \n'
      'удаления справа и извлечения элемента, но когда дело доходит до вставки в начало или удаления \n'
      'в начале списка, то у дека просто невероятное преимущество по времени перед списком')
