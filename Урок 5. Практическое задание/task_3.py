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


def create_list(n=100):
    return [el for el in range(n)]


def create_deque(n=100):
    return deque(el for el in range(n))


# Задание 1
def append_func(data, n=100):
    for i in range(n):
        data.append(i)
    return data


def pop_func(data, n=100):
    for i in range(n):
        data.pop()
    return data


def extend_func(data, ext_list=[0, 1, 2], n=100):
    for i in range(n):
        data.extend(ext_list)
    return data


# Задание 2
def append_left_func(data, user_deq=True, n=100):
    for i in range(n):
        if user_deq:
            data.appendleft(i)
        else:
            data.insert(0, i)
    return data


def pop_left_func(data, user_deq=True, n=100):
    for i in range(n):
        if user_deq:
            data.popleft()
        else:
            data.pop(0)
    return data


def extend_left_func(data, user_deq=True, ext_list=[0, 1, 2], n=100):
    for i in range(n):
        if user_deq:
            data.extendleft(ext_list)
        else:
            for el in ext_list:
                data.insert(0, el)
    return data


# Задание 3
def get_item(data, n=100):
    for i in range(n):
        data[i] = i
    return data




if __name__ == '__main__':
    my_list = create_list(200)
    deq_obj = create_deque(200)

    # Задание 1
    # все функции которые работает с концом массива работают плюс минус одинаково
    print('Задание № 1')
    print(timeit('append_func(my_list.copy())', number=10000, globals=globals()))
    print(timeit('append_func(deq_obj.copy())', number=10000, globals=globals()))
    print(timeit('pop_func(my_list.copy())', number=10000, globals=globals()))
    print(timeit('pop_func(deq_obj.copy())', number=10000, globals=globals()))
    print(timeit('extend_func(my_list.copy())', number=10000, globals=globals()))
    print(timeit('extend_func(deq_obj.copy())', number=10000, globals=globals()))

    # Задание 2
    # все функции которые работает с началом массива быстрее у коллекций, на то они и придуманы :)
    print('Задание № 2')
    print(timeit('append_left_func(my_list.copy(), False)', number=10000, globals=globals()))
    print(timeit('append_left_func(deq_obj.copy())', number=10000, globals=globals()))
    print(timeit('pop_left_func(my_list.copy(), False)', number=10000, globals=globals()))
    print(timeit('pop_left_func(deq_obj.copy())', number=10000, globals=globals()))
    print(timeit('extend_left_func(my_list.copy(), False)', number=10000, globals=globals()))
    print(timeit('extend_left_func(deq_obj.copy())', number=10000, globals=globals()))

    # Задание 3
    # получение элемента быстрее в простом списке как и гласит документация
    print('Задание № 3')
    print(timeit('get_item(my_list.copy())', number=1000, globals=globals()))
    print(timeit('get_item(deq_obj.copy())', number=1000, globals=globals()))
