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
import copy
from cProfile import run
from collections import deque

lc = [el for el in range(100000)]
test_list = copy.deepcopy(lc)
test_deque = deque(copy.deepcopy(lc))


def append(in_list, array):
    print('append')
    for el in array:
        in_list.append(el)


def pop(in_list, array):
    print('pop')
    for _ in array:
        in_list.popitem()


def extend(in_list, array):
    print('extend')
    in_list.extend(array)


def test_1_list(t_list, array):
    append(t_list, array)
    pop(t_list, array)
    extend(t_list, array)


def test_1_deque(t_deque, array):
    append(t_deque, array)
    pop(t_deque, array)
    extend(t_deque, array)


def deque_appendleft(t_deque, array):
    print('appendleft')
    for el in array:
        t_deque.appendleft(el)


def list_insert(t_list, array):
    print('insert')
    for el in array:
        t_list.insert(el, 0)


def deque_popleft(t_deque, array):
    print('popleft')
    for _ in array:
        t_deque.popleft()


def list_remove(t_list, array):
    print('remove')
    for _ in array:
        first_el = t_list[0]
        t_list.remove(0)


def deque_extendleft(t_deque, array):
    print('extendleft')
    t_deque.extendleft(array)


def list_extend_left(t_list, array):
    print('extend_left')
    temp = []
    temp.extend(array)
    temp.extend(t_list)
    t_list = temp[:]
    del temp


def test_2_list(t_list, array):
    list_insert(t_list, array)
    list_remove(t_list, array)
    list_extend_left(t_list, array)


def test_2_deque(t_deque, array):
    deque_appendleft(t_deque, array)
    deque_popleft(t_deque, array)
    deque_extendleft(t_deque, array)


def test_3_1_list(t_list):
    for _ in t_list:
        pass


def test_3_1_deque(t_deque):
    for _ in t_deque:
        pass


def test_3_2_list(t_list):
    for idx in range(len(t_list)):
        temp = t_list[idx]


def test_3_2_deque(t_deque):
    for idx in range(len(t_deque)):
        temp = t_deque[idx]


run('test_1_list(test_list, lc)')
"""
1    0.088    0.088    0.138    0.138 task_3.py:37(append)
1    0.147    0.147    0.211    0.211 task_3.py:43(pop)
1    0.000    0.000    0.003    0.003 task_3.py:49(extend)
1    0.000    0.000    0.352    0.352 task_3.py:54(test_1_list)
"""
run('test_1_deque(test_deque, lc)')
"""
1    0.053    0.053    0.078    0.078 task_3.py:37(append)
1    0.075    0.075    0.109    0.109 task_3.py:43(pop)
1    0.000    0.000    0.003    0.003 task_3.py:49(extend)
1    0.000    0.000    0.189    0.189 task_3.py:60(test_1_deque)
"""
run('test_2_list(test_list, lc)')
"""
1    0.001    0.001   44.075   44.075 task_3.py:105(test_2_list)
1    0.262    0.262   24.272   24.272 task_3.py:72(list_insert)
1    0.267    0.267   19.795   19.795 task_3.py:84(list_remove)
1    0.003    0.003    0.006    0.006 task_3.py:96(list_extend_left)
"""
run('test_2_deque(test_deque, lc)')
"""
1    0.000    0.000    0.131    0.131 task_3.py:111(test_2_deque)
1    0.043    0.043    0.065    0.065 task_3.py:66(deque_appendleft)
1    0.041    0.041    0.064    0.064 task_3.py:78(deque_popleft)
1    0.000    0.000    0.002    0.002 task_3.py:91(deque_extendleft)
"""
run('test_3_1_list(test_list)')
run('test_3_2_list(test_list)')
"""
1    0.006    0.006    0.006    0.006 task_3.py:117(test_3_1_list)
1    0.019    0.019    0.019    0.019 task_3.py:126(test_3_2_list)
"""
run('test_3_1_deque(test_deque)')
run('test_3_2_deque(test_deque)')
"""
1    0.011    0.011    0.011    0.011 task_3.py:122(test_3_1_deque)
1    4.694    4.694    4.694    4.694 task_3.py:131(test_3_2_deque)
"""
"""
Вывод:
Исходя из наблюдений, мы видим что в целом на базовых операциях оба массива показывают примерно одинаковые 
значения, отличия начинаются при использовании методов "left" у deque они выполняются значительно быстрее
Так же можем заметить что deque медленнее в переборе элементов особенно в обращении по индексу
"""
