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

cnt_iter = 1000

my_list = []
my_deque = deque()
# a)
# append
print(timeit("""for i in range(cnt_iter):
    my_list.append(i)""", "from __main__ import my_list, cnt_iter", number=1000))  # 0.1677388
print(timeit("""for i in range(cnt_iter):
    my_deque.append(i)""", "from __main__ import my_deque, cnt_iter", number=1000))  # 0.19292229999999994
# Скорость примерно одинаковая
# extend
print(timeit("my_list.extend(my_list)", "from __main__ import my_list", number=1))  # 0.017037100000000027
print(timeit("my_deque.extend(my_deque)", "from __main__ import my_deque", number=1))  # 0.04435180000000005
# Расширение дека медленнее
# pop
print(timeit("""for i in range(len(my_list)):
    my_list.pop()""", "from __main__ import my_list", number=1000))  # 0.19793510000000003
print(timeit("""for i in range(len(my_deque)):
    my_deque.pop()""", "from __main__ import my_deque", number=1000))  # 0.21991109999999991
# Скорость примерно одинаковая

# b)
my_list2 = []
my_deque2 = deque()
# appendleft
print(timeit("""for i in range(cnt_iter):
    my_list2.insert(0, i)""", "from __main__ import my_list2, cnt_iter", number=100))  # 2.0402786
print(timeit("""for i in range(cnt_iter):
    my_deque2.appendleft(i)""", "from __main__ import my_deque2, cnt_iter", number=100))  # 0.00516709999999998
# Скорость заполнения дека выше
# extendleft
print(timeit("""my_list2.reverse()
my_list_copy = my_list2.copy()
my_list2.extend(my_list_copy)
my_list2.reverse()""", "from __main__ import my_list2", number=1))  # 0.0011926999999998245
print(timeit("my_deque2.extendleft(my_deque2)", "from __main__ import my_deque2", number=1))  # 0.0017460000000002474
# расширение дека медленнее
# popleft
print(timeit("""for i in range(len(my_list2)):
    my_list2.pop(0)""", "from __main__ import my_list2", number=1000))  # 4.5713382
print(timeit("""for i in range(len(my_deque2)):
    my_deque2.popleft()""", "from __main__ import my_deque2", number=1000))  # 0.009001299999999546
# Скорость удаления элементов из дека выше

# c)
my_list3 = []
my_deque3 = deque()
for i in range(cnt_iter):
    my_list3.append(i)
for i in range(cnt_iter):
    my_deque3.appendleft(i)

print(timeit('''for i in range(cnt_iter):
    el = my_list3[i]''', "from __main__ import my_list3, cnt_iter", number=1000))  # 0.03243270000000109
print(timeit('''for i in range(cnt_iter):
    el = my_deque3[i]''', "from __main__ import my_deque3, cnt_iter", number=1000))  # 0.10745640000000023
# Скорость взятия элемента из дека ниже