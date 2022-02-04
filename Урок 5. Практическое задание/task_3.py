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

print(timeit("""my_list.append(1)""",  setup="from __main__ import my_list", number=1000000))
# 0.05843129999999999
print(timeit("""my_deque.append(1)""",  setup="from __main__ import my_deque", number=1000000))
# 0.05735709999999999
# Заполнение дека и списка методом append идет практически одинаково по времени

print(timeit("my_list.extend([1, 2, 3])",  setup="from __main__ import my_list, my_deque, cnt_iter", number=1000000))
# 0.12902239999999998
print(timeit("my_deque.extend([1, 2, 3])",  setup="from __main__ import my_list, my_deque, cnt_iter", number=1000000))
# 0.12229080000000003
# Расширение дека и расширение списка выполняется практически с одинаковой скоростью

print(timeit("""for i in range(len(my_list)):
    my_list.pop()""",  setup="from __main__ import my_list, my_deque, cnt_iter", number=10000))
# 0.17796080000000003
print(timeit("""for i in range(len(my_deque)):
    my_deque.pop()""",  setup="from __main__ import my_list, my_deque, cnt_iter", number=10000))
# 0.17123449999999996
# Удаление методом pop проходит практически с одинаковой скоростью

my_list4 = [1, 2, 3]
my_deque4 = deque([1, 2, 3])

print(timeit("""my_list4[1]""",  setup="from __main__ import my_list4, my_deque4, cnt_iter", number=10000000))
# 0.2052939
print(timeit("my_deque4[1]",  setup="from __main__ import my_list4, my_deque4, cnt_iter", number=10000000))
# 0.20858879999999996
# Взятие произвольного элемента из списка и дека занимает примерно одинаковое время.

my_list2 = []
my_deque2 = deque()

print(timeit("""for i in range(cnt_iter):
    my_list2.insert(0, i)""",  setup="from __main__ import my_list2, my_deque2, cnt_iter", number=100))
# 2.0402786
print(timeit("""for i in range(cnt_iter):
    my_deque2.appendleft(i)""",  setup="from __main__ import my_list2, my_deque2, cnt_iter", number=100))
# 0.00516709999999998
# Заполнение дека методом appendleft идет значительно быстрее, чем заполнение списка аналогом insert в нулевой индекс

my_list3 = []
my_deque3 = deque()

print(timeit("""my_list3.reverse()
my_list3.extend([1, 2, 3])
my_list3.reverse()""",  setup="from __main__ import my_list3, my_deque3, cnt_iter", number=1000))
# 0.0011797000000000023
print(timeit("my_deque3.extendleft([1, 2, 3])",  setup="from __main__ import my_list3, my_deque3, cnt_iter", number=1000))
# 0.00011960000000000442
# Расширение дека методом extentedleft идет на порядок быстрее, чем имитация расширения списка


print(timeit("""for i in range(len(my_list2)):
    my_list2.pop(0)""",  setup="from __main__ import my_list2, my_deque2, cnt_iter", number=1000))
# 4.5713382
print(timeit("""for i in range(len(my_deque2)):
    my_deque2.popleft()""",  setup="from __main__ import my_list2, my_deque2, cnt_iter", number=1000))
# 0.009001299999999546
# Удаление из дека методом popleft происходит значительно быстрее, чем удаление из списка по нулевому индексу


