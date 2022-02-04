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

# a)
print('A')
num = 1000

# append
print(timeit('''for i in range(num):
                    my_list.append(i)''', "from __main__ import my_list, my_deque, num", number=1000))  # 0.1481149
print(timeit('''for i in range(num):
                    my_deque.append(i)''', "from __main__ import my_list, my_deque, num", number=1000))  # 0.1494226
# Скорость примерно одинаковая

# extend
print(timeit('''my_list.extend(my_list)''', "from __main__ import my_list, my_deque, num", number=1))  # 0.0138104
print(timeit('''my_deque.extend(my_deque)''', "from __main__ import my_list, my_deque, num", number=1))  # 0.0353
# Расширение списка быстрее

# pop
print(timeit('''for i in range(len(my_list)):
                    my_list.pop()''', "from __main__ import my_list, my_deque, num", number=1000))  # 0.0964451
print(timeit('''for i in range(len(my_deque)):
                    my_deque.pop()''', "from __main__ import my_list, my_deque, num", number=1000))  # 0.1079021
# Скорость примерно одинаковая

# b)
print('B')
my_list2 = []
my_deque2 = deque()

# appendleft
print(timeit('''for i in range(num):
                    my_list2.insert(0, i)''', "from __main__ import my_list2, num", number=100))  # 2.3321438
print(timeit('''for i in range(num):
                    my_deque2.appendleft(i)''', "from __main__ import my_deque2, num", number=100))  # 0.0060234
# Заполнение дека быстрее

# extendleft
print(timeit('''my_list2.reverse()
my_list_copy = my_list2.copy()
my_list2.extend(my_list_copy)
my_list2.reverse()''', "from __main__ import my_list2", number=1))  # 0.001638699999999993
print(timeit('''my_deque2.extendleft(my_deque2)''', "from __main__ import my_deque2", number=1))  # 0.002568599999999588
# Скорость примерно одинаковая

# popleft
print(timeit('''for i in range(len(my_list2)):
                    my_list2.pop(0)''', "from __main__ import my_list2", number=1000))  # 6.5366734
print(timeit('''for i in range(len(my_deque2)):
                    my_deque2.popleft()''', "from __main__ import my_deque2", number=1000))  # 0.010477500000000362
# Удаление элементов из дека быстрее

# c)
print('C')
my_list3 = []
my_deque3 = deque()
for i in range(num):
    my_list3.append(i)
for i in range(num):
    my_deque3.appendleft(i)

print(timeit('''for i in range(num):
                    d = my_list3[i]''', "from __main__ import my_list3, num", number=1000))  # 0.030206200000000294
print(timeit('''for i in range(num):
                    d = my_deque3[i]''', "from __main__ import my_deque3, num", number=1000))  # 0.043863200000000546
# Скорость примерно одинаковая