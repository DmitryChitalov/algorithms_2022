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

cnt_iter = 1000

my_list = []
my_deque = deque()

print(timeit("""for i in range(cnt_iter):
    my_list.append(i)""",  setup="from __main__ import my_list, my_deque, cnt_iter", number=100))
# 0.007764800000000002
print(timeit("""for i in range(cnt_iter):
    my_deque.append(i)""",  setup="from __main__ import my_list, my_deque, cnt_iter", number=100))
# 0.004939300000000001
# Заполнение дека методом append идет быстрее, чем списка

print(timeit("my_list.extend(my_list)",  setup="from __main__ import my_list, my_deque, cnt_iter", number=1))
# 0.0005582999999999977
print(timeit("my_deque.extend(my_deque)",  setup="from __main__ import my_list, my_deque, cnt_iter", number=1))
# 0.0021122999999999975
# Расширение дека на порядок медленнее расширения списка

print(timeit("""for i in range(len(my_list)):
    my_list.pop()""",  setup="from __main__ import my_list, my_deque, cnt_iter", number=1000))
# 0.0114484899999999997
print(timeit("""for i in range(len(my_deque)):
    my_deque.pop()""",  setup="from __main__ import my_list, my_deque, cnt_iter", number=1000))
# 0.011424200000000007
# Удаление методом pop проходит практически с одинаковой скоростью, на больших объемах дек немного быстрее

my_list2 = []
my_deque2 = deque()

print(timeit("""for i in range(cnt_iter):
    my_list2.insert(0, i)""",  setup="from __main__ import my_list2, my_deque2, cnt_iter", number=100))
# 2.0402786
print(timeit("""for i in range(cnt_iter):
    my_deque2.appendleft(i)""",  setup="from __main__ import my_list2, my_deque2, cnt_iter", number=100))
# 0.00516709999999998
# Заполнение дека методом appendleft идет значительно быстрее, чем заполнение списка аналогом insert в нулевой индекс

print(timeit("""my_list2.reverse()
my_list_copy = my_list2.copy()
my_list2.extend(my_list_copy)
my_list2.reverse()""",  setup="from __main__ import my_list2, my_deque2, cnt_iter", number=1))
# 0.0011926999999998245
print(timeit("my_deque2.extendleft(my_deque2)",  setup="from __main__ import my_list2, my_deque2, cnt_iter", number=1))
# 0.0017460000000002474
# Расширение дека методом extentedleft идет несколько медленне, чем имитация расширения списка

print(timeit("""for i in range(len(my_list2)):
    my_list2.pop(0)""",  setup="from __main__ import my_list2, my_deque2, cnt_iter", number=1000))
# 4.5713382
print(timeit("""for i in range(len(my_deque2)):
    my_deque2.popleft()""",  setup="from __main__ import my_list2, my_deque2, cnt_iter", number=1000))
# 0.009001299999999546
# Удаление из дека методом popleft происходит значительно быстрее, чем удаление из списка по нулевому индексу


