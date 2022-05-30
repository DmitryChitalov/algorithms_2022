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
from random import randrange
from collections import deque

arr = []
dq = deque()

def arr_fill():
    arr.clear()
    for i in range(size):
        arr.append(randrange(100))

# beg        
def dq_fill():
    dq.clear()
    for i in range(size):
        dq.append(randrange(100))

def list_app():
    for i in range(n):
        arr.append(1)

def deque_app():
    for i in range(n):
        dq.append(1)

def list_pop():
    for i in range(n):
        arr.pop()
    
def deque_pop():
    for i in range(n):
        dq.pop()
    
def list_extend():
    for i in range(n):
        arr.extend([2, 2])

def deque_extend():
    for i in range(n):
        dq.extend([2, 2])

# end
def list_app_beg():
    for i in range(n):
        arr.insert(0, 1)

def deque_appleft():
    for i in range(n):
        dq.appendleft(1)

def list_pop_beg():
    for i in range(n):
        arr.remove(arr[0])
    
def deque_popleft():
    for i in range(n):
        dq.popleft()
    
def list_extend_beg():
    for i in range(n):
        for item in [2, 2]:
            arr.insert(0, item)

def deque_extendleft():
    for i in range(n):
        dq.extendleft([2, 2])
        
# извлечение
def list_get():
    for i in range(n):
        item = arr[index]

def deque_get():
    for i in range(n):
        for j in range(index + 1):
            item = dq.popleft()
        
size = 100
arr_fill()
dq_fill()
print('Операции в конце:')
n = 100
for func_name in (
    'list_app()', 'deque_app()' 
    , 'list_pop()', 'deque_pop()'
    , 'list_extend()', 'deque_extend()'
):
    print(f'{func_name}: время = {timeit(func_name, globals=globals(), number=100000)}')

print('Операции в начале:')
n = 100
for func_name in (
    'list_app_beg()', 'deque_appleft()' 
    , 'list_pop_beg()', 'deque_popleft()'
    , 'list_extend_beg()', 'deque_extendleft()'
):
    print(f'{func_name}: время = {timeit(func_name, globals=globals(), number=1)}')

print('Операции извлечения:')
size = 1000000
arr_fill()
dq_fill()
n = 300
index = 100
for func_name in (
    'list_get()', 'deque_get()' 
):
    print(f'{func_name}: время = {timeit(func_name, globals=globals(), number=1)}')

'''
Скорость выполнения операций в конце для списка и дека практически одинаковая.
Скорость выполнения операций в начале списка на порядки ниже скорости для дека. Разница сильно зависит от размера списка.
Скорость извлечения элемента из списка на порядки выше скорости для дека. Сильная зависимость от размера дека.
'''    