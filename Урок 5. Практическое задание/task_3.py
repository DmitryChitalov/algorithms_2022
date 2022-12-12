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



3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
import timeit
import time

'''
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
'''

list_test = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57]
dq_test = deque([0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

def append_func(list_dq):
    for i in range(100):
        list_dq.append(i)
    return list_dq


count, res_list, res_dq = 0, 0, 0
while count < 10:
    res_list += timeit.timeit(stmt=f'append_func(list_test)', setup=f'from __main__ import append_func, list_test',
                              number=1000)
    time.sleep(1)
    res_dq += timeit.timeit(stmt=f'append_func(dq_test)', setup=f'from __main__ import append_func, dq_test',
                            number=1000)
    time.sleep(1)
    count += 1
print(res_list, res_dq, sep='\n')

'''deque быстрее списка
0.12359739991370589
0.08861209987662733'''


def pop_func(list_dq):
    for i in range(100):
        list_dq.pop()
    return list_dq


count, res_list, res_dq = 0, 0, 0
while count < 10:
    res_list += timeit.timeit(stmt=f'pop_func(list_test)', setup=f'from __main__ import pop_func, list_test',
                              number=1000)
    time.sleep(1)
    res_dq += timeit.timeit(stmt=f'pop_func(dq_test)', setup=f'from __main__ import pop_func, dq_test',
                            number=1000)
    time.sleep(1)
    count += 1
print(res_list, res_dq, sep='\n')

'''list немного быстрее deque
0.1164308000006713
0.11915870010852814'''

'''
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
'''


def app_ins_func(list_dq):
    if isinstance(list_dq, deque):
        for i in range(100):
            list_dq.appendleft(i)
        return list_dq
    else:
        for i in range(100):
            list_dq.insert(0, i)
        return list_dq


count, res_list, res_dq = 0, 0, 0
while count < 10:
    res_list += timeit.timeit(stmt=f'app_ins_func(list_test)', setup=f'from __main__ import app_ins_func, list_test',
                              number=100)
    time.sleep(1)
    res_dq += timeit.timeit(stmt=f'app_ins_func(dq_test)', setup=f'from __main__ import app_ins_func, dq_test',
                            number=100)
    time.sleep(1)
    count += 1
print(res_list, res_dq, sep='\n')

'''deque значительно быстрее списка
3.3932631001225673
0.016997500031720847'''