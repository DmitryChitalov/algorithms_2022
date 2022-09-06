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

lst = [i for i in range(10)]
deq = deque(lst)
N = 50  # Счетчик для всех циклов при проверках времени


# 1. Сравнение операций: append, pop, extend из списка и дека.

def append_(seq):
    '''Добавление элементов в множество'''
    for i in range(N):
        seq.append(i)


def pop_(seq):
    '''Удаление последнего элемента из множества'''
    for i in range(N):
        seq.pop()


def extend_(seq):
    '''Добавление последовательностей в множество'''
    extended_lst = [i for i in range(10)]
    for i in range(N):
        seq.extend(extended_lst)


print(f'Append для list: {timeit("append_(lst)", globals=globals(),number=1000)}')
print(f'Append для deque: {timeit("append_(deq)", globals=globals(),number=1000)}')
print(f'Pop для list: {timeit("pop_(lst)", globals=globals(),number=1000)}')
print(f'Pop для deque: {timeit("pop_(deq)", globals=globals(),number=1000)}')
print(f'Extend для list: {timeit("extend_(lst)", globals=globals(),number=1000)}')
print(f'Extend для deque: {timeit("extend_(deq)", globals=globals(),number=1000)}')

'''
Наглядно видно, что разница в выполнении операции если и есть, то совсем незначительная
Append для list: 0.000394799979403615
Append для deque: 0.0004143000114709139
Pop для list: 0.00027840002439916134
Pop для deque: 0.00026919995434582233
Extend для list: 0.0011239000596106052
Extend для deque: 0.0011336999014019966
'''

# 2. сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка.
# Cделать выводы что и где быстрее


def append_left_(seq):
    if isinstance(seq, deque):
        for i in range(N):
            seq.appendleft(i)
        return seq
    else:
        for i in range(N):
            seq.insert(0, i)
        return seq


def popleft_(seq):
    if isinstance(seq, deque):
        for i in range(N):
            seq.popleft()
    else:
        for i in range(N):
            seq.pop(0)


def extend_left_(seq):
    extended_lst = [i for i in range(N)]
    if isinstance(seq, deque):
        for i in range(N):
            seq.extendleft(extended_lst)
    else:
        for i in range(N):
            for j in extended_lst:
                seq.insert(0, j)


print(f'Append left для list: {timeit("append_left_(lst)", globals=globals(),number=100)}')
print(f'Append left для deque: {timeit("append_left_(deq)", globals=globals(),number=100)}')
print(f'Pop left для list: {timeit("popleft_(lst)", globals=globals(),number=100)}')
print(f'Pop left для deque: {timeit("popleft_(deq)", globals=globals(),number=100)}')
print(f'Extend left для list: {timeit("extend_left_(lst)", globals=globals(),number=10)}')
print(f'Extend left для deque: {timeit("extend_left_(deq)", globals=globals(),number=10)}')


'''
Из замеров видно, что специализированные операции deque работают в десятки тысяч раз быстрее, чем аналоги у списков:
Append left для list: 0.14251979999244213
Append left для deque: 0.00040909997187554836
Pop left для list: 0.12745149992406368
Pop left для deque: 0.0004183999262750149
Extend left для list: 20.3422582000494
Extend left для deque: 0.0037296998780220747
Связано с написанием этих операций на более низкоуровневом языке (Cи)
'''

# 3) сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее


def getting_el(seq):
    for i in range(N):
        a = seq[i]


print(f'Получение элемента по индексу для list: {timeit("getting_el(lst)", globals=globals())}')
print(f'Получение элемента по индексу для deque: {timeit("getting_el(deq)", globals=globals())}')

'''
Получение элемента по индексу для list: 1.787309999926947
Получение элемента по индексу для deque: 2.822568100062199
Дэк отрабатывает медленнее, и чем дальше, тем больше будет увеличиваться разрыв. Дэк предназначен для добавления
и изъятия, для поиска по индексу подходит больше список.
'''

