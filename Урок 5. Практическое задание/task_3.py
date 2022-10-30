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
import random
from collections import deque
from functools import partial
from timeit import timeit

sample_list = list([random.randint(1, 100) for i in range(5000000)])
sample_deque = deque(sample_list)
test_list = [333, 222, 3423, 443]
operation_cnt = 1000
modes = ['list', 'deque']

# 1) сравнить операции append, pop, extend списка и дека и сделать выводы что и где быстрее
operations = ['append', 'pop', 'extend']


def list_op1(in_obj, op: str):
    if op == 'append':
        for i in range(operation_cnt):
            in_obj.append(i + 666)
    elif op == 'pop':
        for i in range(operation_cnt):
            in_obj.pop()
    elif op == 'extend':
        for i in range(operation_cnt):
            in_obj.extend(test_list)
    return in_obj


for op in operations:
    print(f"{op}, list: {timeit(partial(list_op1,in_obj=sample_list.copy(), op=op), globals=globals(), number=1000)}")
    print(f"{op}, deque: {timeit(partial(list_op1,in_obj=sample_deque.copy(), op=op), globals=globals(), number=1000)}")

# append, list: 0.081891349000216
# append, deque: 0.07397307699966404
# pop, list: 0.04226122000000032
# pop, deque: 0.04268167400005041
# extend, list: 0.07260183800008235
# extend, deque: 0.08818045799989704
# Вывод: добавление в конец работает немного быстрее для дека, массовое добавление - медленнее, pop примерно одинаково

# 2) сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее
operations = ['appendleft', 'popleft', 'extendleft']


def list_op2(in_obj, op: str):
    if op == 'appendleft':
        if type(in_obj) == list:
            for i in range(operation_cnt):
                in_obj.insert(0, i*2)
        else:
            for i in range(operation_cnt):
                in_obj.appendleft(i * 2)
    elif op == 'popleft':
        if type(in_obj) == list:
            for i in range(operation_cnt):
                in_obj.pop(1)
        else:
            for i in range(operation_cnt):
                in_obj.popleft()
    elif op == 'extendleft':
        if type(in_obj) == list:
            for i in range(operation_cnt):
                in_obj.insert(0, test_list)
        else:
            for i in range(operation_cnt):
                in_obj.extendleft(test_list)
    return in_obj


for op in operations:
    print(f"{op}, list: {timeit(partial(list_op2,in_obj=sample_list.copy(), op=op), globals=globals(), number=10)}")
    print(f"{op}, deque: {timeit(partial(list_op2,in_obj=sample_deque.copy(), op=op), globals=globals(), number=10)}")

# appendleft, list: 67.81270779099987
# appendleft, deque: 0.0006810899999436515
# popleft, list: 73.19576722300008
# popleft, deque: 0.0004858580000473012
# extendleft, list: 67.99702185500018
# extendleft, deque: 0.000931446999857144
# Вывод: преимущество дека налицо

# 3) сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее
operations = ['get', 'get_random']
indexes = list([random.randint(i * 0, len(sample_list)) for i in range(1, operation_cnt)])


def list_op3(in_obj, op: str):
    if op == 'get':
        for i in range(operation_cnt):
            el = in_obj[i]
    elif op == 'popleft':
        for i in range(operation_cnt):
            el = in_obj[indexes[i]]
    return in_obj


for op in operations:
    print(f"{op}, list: {timeit(partial(list_op3,in_obj=sample_list.copy(), op=op), globals=globals(), number=1000)}")
    print(f"{op}, deque: {timeit(partial(list_op3,in_obj=sample_deque.copy(), op=op), globals=globals(), number=1000)}")
# get, list: 0.029976972000440583
# get, deque: 0.03771809799945913
# get_random, list: 0.00018321999959880486
# get_random, deque: 0.0003350870001668227
# Для доступа к случайному элементу лист лучше