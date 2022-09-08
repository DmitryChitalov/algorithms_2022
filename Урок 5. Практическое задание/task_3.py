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


def append_list(num):
    my_list = []
    for i in range(num):
        my_list.append(i)
    return my_list


def append_deque(num):
    my_deque = deque()
    for i in range(num):
        my_deque.append(i)
    return my_deque


def extend_list(my_list):
    for i in range(10000):
        my_list.extend([5, 6, 7, 8])
    return my_list


def extend_deque(my_deque):
    for i in range(10000):
        my_deque.extend([5, 6, 7, 8])
    return my_deque


def pop_list(my_list):
    for i in range(1000):
        my_list.pop()
    return my_list


def pop_deque(my_deque):
    for i in range(1000):
        my_deque.pop()
    return my_deque


def append_left_list(my_list):
    for i in range(1000):
        my_list.insert(0, i)
    return my_list


def append_left_deque(my_deque):
    for i in range(1000):
        my_deque.appendleft(i)
    return my_deque


def pop_left_list(my_list):
    for i in range(1000):
        my_list.pop(0)
    return my_list


def pop_left_deque(my_deque):
    for i in range(1000):
        my_deque.popleft()
    return my_deque


def extend_left_list(my_list):
    for i in range(1000):
        my_list.insert(0, [5, 6, 7])
    return my_list


def extend_left_deque(my_deque):
    for i in range(1000):
        my_deque.extendleft([5, 6, 7])
    return my_deque


def change_left_list(my_list):
    for i in range(10000):
        my_list[i] = 10
    return my_list


def change_left_deque(my_deque):
    for i in range(10000):
        my_deque[i] = 10
    return my_deque


if __name__ == '__main__':
    number = 10 ** 4
    list_test = append_list(number)
    deque_test = append_deque(number)
    print('1.')
    print('Test append list', timeit('append_list(number)', globals=globals(), number=1000))
    print('Test append deque', timeit('append_deque(number)', globals=globals(), number=1000))
    print('Test extend list', timeit('extend_list(list_test)', globals=globals(), number=100))
    print('Test extend deque', timeit('extend_deque(deque_test)', globals=globals(), number=100))
    print('Test pop list', timeit('pop_list(list_test)', globals=globals(), number=1000))
    print('Test pop deque', timeit('pop_deque(deque_test)', globals=globals(), number=1000))

    """
    1)
    1-ый результат замера:
    Test append list 0.6168255999218673
    Test append deque 0.8332854999462143
    Test extend list 0.17027550004422665
    Test extend deque 0.18397349992301315
    Test pop list 0.059010199969634414
    Test pop deque 0.0496733000036329
    2-ой результат:
    Test append list 0.6631418000906706
    Test append deque 0.6395079999929294
    Test extend list 0.1608629000838846
    Test extend deque 0.1716821000445634
    Test pop list 0.046705399989150465
    Test pop deque 0.04461699991952628
    При данных замерах результаты не однозначные когда-то list быстрее, когда-то deque
    """

    print('2.')
    print('Test append left list', timeit('append_left_list(list_test)', globals=globals(), number=3))
    print('Test append left deque', timeit('append_left_deque(deque_test)', globals=globals(), number=3))
    print('Test pop left list', timeit('pop_left_list(list_test)', globals=globals(), number=3))
    print('Test pop left deque', timeit('pop_left_deque(deque_test)', globals=globals(), number=3))
    print('Test extend left list', timeit('extend_left_list(list_test)', globals=globals(), number=3))
    print('Test extend left deque', timeit('extend_left_deque(deque_test)', globals=globals(), number=3))

    """
    2)
    Результат замеров:
    Test append left list 8.14375819999259
    Test append left deque 0.00017870008014142513
    Test pop left list 8.903481500106864
    Test pop left deque 0.0002933000214397907
    Test extend left list 8.21757640002761
    Test extend left deque 0.0005440999520942569
    
    Операции append, pop, extend в deque происходят значительно быстрее чем в списке
    """

    print('3.')
    print('Test change left list', timeit('change_left_list(list_test)', globals=globals(), number=1000))
    print('Test change left deque', timeit('change_left_deque(deque_test)', globals=globals(), number=1000))

    """
    3)
    Результат замеров:
    Test change left list 0.44698699994478375
    Test change left deque 1.5630390000296757
    
    Выборка элемента и его изменение происходит в списке значительно быстрее чем в deque
    Таким образом deque наиболее эффективнее по сравнению со списком при операциях 
    в начале, такими как добавление и удаление (appendleft, extendleft, popleft) 
    """
