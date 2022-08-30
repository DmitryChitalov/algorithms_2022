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

'''
Выводы и аналитика. Ожидание против реальности. Я ожидал, что "стандартные" для списков операции, такие как .append,
pop будут быстрее работать именно с list-ом, а не с деком. Однако, произведенные мною замеры показали, что deque-объект
опережает список по скорости по этим операциям, хоть и не намного. По второму блоку задач, я предполагал, что операции,
"специализированные" для коллекции deque, такие как .appenleft, .popleft, .extendleft будут быстрее аналогичных действий
для обычного списка, что логично, ибо зачем тогда дек был бы нужен. Произведенные замеры подтвердили мои ожидания, 
показав полное превосходство deque над списком. По третьему блоку задач выяснилось, что получение элемента списка по 
индексу быстрее происходит у list-объекта, чем у deque.
Выводы: использование коллекции deque может помочь ускорить выполнение кода, особенно если вам нужны операции
двустороннего добавления и удаления элементов. Однако, если в коде будут операции с индексами, а .appendleft и .popleft
не нужны, то тогда предпочтительнее применение стандартного списка. 
'''
# 1) append, pop, extend списка и дека
my_list = list(range(11))
my_deque = deque(my_list)
lst_to_extend = []


def append_el(lst, num):
    for i in range(num):
        lst.append(i)
    return lst


def pop_el(lst, num):
    for i in range(num):
        lst.pop()
    return lst


lst_to_extend = append_el(lst_to_extend, 6)
print(timeit('append_el(my_list, 11)', globals=globals()))  # => append списка - 0.7487014000071213
print(timeit('append_el(my_deque, 11)', globals=globals()))  # => append дека - 0.6169445999839809
my_list = list(range(111))
my_deque = deque(my_list)
print(timeit('pop_el(my_list, 2)', globals=globals(), number=55))  # => pop списка - 2.1300045773386955e-05
print(timeit('pop_el(my_deque, 2)', globals=globals(), number=55))  # => pop deque - 1.9799976143985987e-05
my_list = list(range(11))
my_deque = deque(my_list)
print(timeit('my_list.extend(lst_to_extend)', globals=globals()))  # => extend списка - 0.20616359999985434
print(timeit('my_deque.extend(lst_to_extend)', globals=globals()))  # => extend deque - 0.1603911000129301

# 2) appendleft, popleft, extendleft
my_list = list(range(11))
my_deque = deque(my_list)


def appendleft_el(lst, num):
    for i in range(num):
        lst = [i] + lst
    return lst


def appendleft_el_2(some_deque, num):
    for i in range(num):
        some_deque.appendleft(i)
    return some_deque


def popleft_el(lst, num):
    for i in range(num):
        del lst[0]
    return lst


def popleft_el_2(some_deque, num):
    for i in range(num):
        some_deque.popleft()
    return some_deque


def extend_left(lst, lst_to_ext):
    for i in lst_to_ext:
        lst = [i] + lst
    return lst


print(timeit('appendleft_el(my_list, 12)', globals=globals()))  # => "appendleft" списка - 1.129416800045874
print(timeit('appendleft_el_2(my_deque, 12)', globals=globals()))  # => appendleft deque - 0.6193740000016987
my_list = list(range(111))
my_deque = deque(my_list)
print(timeit('popleft_el(my_list, 2)', globals=globals(), number=50))  # => "popleft" списка - 2.1299987565726042e-05
print(timeit('popleft_el_2(my_deque, 2)', globals=globals(), number=50))  # => popleft deque - 1.7200014553964138e-05
my_list = list(range(11))
my_deque = deque(my_list)
print(timeit('extend_left(my_list, lst_to_extend)', globals=globals()))  # => "extendleft" списка - 0.45993740000994876
print(timeit('my_deque.extendleft(lst_to_extend)', globals=globals()))  # => extendleft deque - 0.0957291999948211


# 3) получение элемента

def get_el(some_list, num):
    for i in range(num):
        some_list[i]
    return some_list


my_list = list(range(11))
my_deque = deque(my_list)

print(timeit('get_el(my_list, 5)', globals=globals()))  # => 0.29364350001560524
print(timeit('get_el(my_deque, 5)', globals=globals()))  # => 0.3301187999895774
