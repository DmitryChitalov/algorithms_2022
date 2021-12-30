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

from collections import deque
from timeit import timeit

my_list = []
my_deque = deque()
list_1 = [1, 2]
n = 100000

# 1)
def append_list(my_list):
    for i in range(n):
        my_list.append("_")
    return my_list
append_list(my_list)

def append_deque(my_deque):
    for i in range(n):
        my_deque.append('_')
    return my_deque
append_deque(my_deque)

#print(timeit('append_list(my_list.copy())', globals=globals(),number=100))  # 3.3322939
#print(timeit('append_list(my_deque.copy())', globals=globals(),number=100))  # 3.1007219
#Операции append примерно однаковы в списке и в deque

def pop_list(my_list):
    for i in range(n):
        my_list.pop()
    return my_list

def pop_deque(my_deque):
    for i in range(n):
        my_deque.pop()
    return my_deque

#print(timeit('pop_list(my_list.copy())', globals=globals(), number=100))  # 2.2110874999999997
#print(timeit('pop_deque(my_deque.copy())', globals=globals(), number=100))  # 2.4850788
# операции pop примерно одинаковы и в списке и в deque

def extend_list(my_list):
    for i in range(n):
        my_list.extend(list_1)
    return my_list

def extend_deque(my_deque):
    for i in range(n):
        my_deque.extend(list_1)
    return my_deque

#print(timeit('extend_list(my_list.copy())', globals=globals(), number=100))  # 5.517878300000001
#print(timeit('extend_deque(my_deque.copy())', globals=globals(), number=100))  # 5.144756100000002
# операции extend примерно одинаковы

# 2)
def insert_list(my_list):
    for i in range(100):
        my_list.insert(0, list_1)
    return my_list

def append_left_deque(my_deque):
    for i in range(100):
        my_deque.appendleft('0')
    return my_deque

#print(timeit('insert_list(my_list.copy())', globals=globals(), number=100))  # 2.4011183000000003
#print(timeit('append_left_deque(my_deque.copy())', globals=globals(), number=100))  # 0.3450916000000004

def popleft_list(my_list):
    for i in range(100):
        my_list.pop(0)
    return my_list

def popleft_deque(my_deque):
    for i in range(100):
        my_deque.popleft()
    return my_deque

#print(timeit('popleft_list(my_list.copy())', globals=globals(), number=100))  # 11.4036198
#print(timeit('popleft_deque(my_deque.copy())', globals=globals(), number=100)) # 0.44853250000000067

def extendleft_list(my_list):
    for i in range(100):
        my_list.insert(0, list_1)
    return my_list

def extendleft_deque(my_deque):
    for i in range(100):
        my_deque.extend(list_1)
    return my_deque

#print(timeit('extendleft_list(my_list.copy())', globals=globals(), number=100))  # 2.3823975
#print(timeit('extendleft_deque(my_deque.copy())', globals=globals(), number=100))  # 0.4582151999999997
# операции из 2го пункта задачи в deque намного быстрее чем в списке

my_list.clear()
my_deque.clear()

# 3)
for i in range(100001):
    my_list.append(0)
    my_deque.append(1)

def get_elem_list(my_list):
    for i in range(100000):
        elem = my_list[i]
    return elem

def get_elem_deque(my_deque):
    for i in range(100000):
        elem = my_deque[i]
    return elem

#print(timeit('get_elem_list(my_list)', globals=globals(), number=100))  # 1.6376079
#print(timeit('get_elem_deque(my_deque)', globals=globals(), number=100))  # 33.543159499999994
# операции получения элемента в списке намного быстрее чем в deque
