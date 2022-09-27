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



new_list = [el for el in range(20000)]

new_deque = [el for el in range(20000)]

my_list = [64, 38, 27, 99]

def append_lst(lst):
    for i in range(10000):
        lst.append(i)
    return lst

def append_deq(var_deque):
    for i in range(10000):
        var_deque.append(i)
    return var_deque

def pop_lst(lst):
    for i in range(10000):
        lst.pop()
    return lst

def pop_deq(var_deque):
    for i in range(10000):
        var_deque.pop()
    return var_deque

def extend_lst(lst):
    for i in range(10000):
        lst.extend(my_list)
    return lst

def extend_deq(var_deque):
    for i in range(10000):
        var_deque.extend(my_list)
    return var_deque

#print(timeit('append_lst(new_list[:])', globals=globals(), number=100))
#print(timeit('append_deq(new_deque[:])', globals=globals(), number=100))
# 0.124691109
# 0.121154496

#print(timeit('pop_lst(new_list[:])', globals=globals(), number=100))
#print(timeit('pop_deq(new_deque[:])', globals=globals(), number=100))
#0.10758199999999998
#0.101458253

#print(timeit('extend_lst(new_list[:])', globals=globals(), number=100))
#print(timeit('extend_deq(new_deque[:])', globals=globals(), number=100))
#0.191777932
#0.195250469
"""
Операции append(), pop(), extend() в list и deque
выполняются примерно за одно время
"""

new_deque = deque([el for el in range(20000)])

def appendleft_deq(var_deque):
    for i in range(10000):
        var_deque.appendleft(i)
    return var_deque

def insert_list(lst):
    for i in range(10000):
        lst.insert(0, i)
    return lst

#print(timeit('insert_list(new_list.copy())', globals=globals(), number=100))
#print(timeit('appendleft_deq(new_deque.copy())', globals=globals(), number=100))

#19.184978527
#0.12255837900000088



def popleft_lst(lst):
    for i in range(10000):
        lst.pop(0)
    return lst

def popleft_deq(var_deque):
    for i in range(10000):
        var_deque.popleft()
    return var_deque

#print(timeit('popleft_lst(new_list.copy())', globals=globals(), number=100))
#print(timeit('popleft_deq(new_deque.copy())', globals=globals(), number=100))
#5.765327558
#0.11092413800000056

"""
Не нашла полного аналого метода extendleft() для списка, поэтому для замеров 
использовала insert()
"""
def extend_lst(lst):
    for i in range(10000):
        lst.insert(0, my_list)
    return lst

def extendleft_deq(var_deque):
    for i in range(10000):
        var_deque.extendleft(my_list)
    return var_deque

#print(timeit('extend_lst(new_list.copy())', globals=globals(), number=100))
#print(timeit('extendleft_deq(new_deque.copy())', globals=globals(), number=100))
#20.625160173999998
#0.23524832600000067

"""
Из замеров очевидно, что операци appendleft(), extendleft(), popleft() выполняются
значительно быстрее, чем соответстующии им операции из списка. 
Поэтому для добавления/удаления числа/чисел в начало списка целесообразнее использовать deque.
"""

def get_el_lst(lst):
    for i in range(10000):
        lst[i] = i
    return lst

def get_el_deq(var_deque):
    for i in range(10000):
        var_deque[i] = i
    return var_deque

print(timeit('get_el_lst(new_list.copy())', globals=globals(), number=100))
print(timeit('get_el_deq(new_deque.copy())', globals=globals(), number=100))

#0.090186617
#0.27205700600000005
"""
Замеры подтвердили,что если вам нужен быстрый случайный доступ, используйте list.
"""