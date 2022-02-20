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
import time

num = [i for i in range(10000)]
dq = deque(i for i in range(10000))

# декоратор для замеров времени
def time_measurement(func):
    def wrapper(arg1):
        start_time = time.time()
        c = func(arg1)
        print(f'{func.__name__} : {(time.time() - start_time)} seconds')
        return c
    return wrapper

# проверим скорость выполнения операции append

@time_measurement
def test_append(a):
    for i in range(10000):
        a.append(i)
    return a

test_append(num)  # test_append : 0.0024352073669433594 seconds
test_append(dq)   # test_append : 0.0028977394104003906 seconds
# По замерам не заметна особая разнница по времени выполнения, хотя и тут deque немного быстрее
# при append не надо пересчитывать индексы, т.к. берем последний индекс

# проверим скорость выполнения операции pop

@time_measurement
def test_pop(a):
    for i in range(len(a)):
        a.pop()
    return a

test_pop(num)  # test_pop : 0.0038907527923583984 seconds
test_pop(dq)   # test_pop : 0.0020339488983154297 seconds
# Так же нет грандиозной разницы по времени, т.к. опять обращаемся к последнему индексы
# не надо пересчитывать индексы

# проверим скорость выполнения операции extend

ext = [i for i in range(10)]

@time_measurement
def test_extend(a):
    for i in range(10000):
        a.extend(ext)
    return a

test_extend(num)  # test_extend : 0.004200935363769531 seconds
test_extend(dq)   # test_extend : 0.006617307662963867 seconds
# Так же нет грандиозной разницы по времени, но deque как обычно быстрее

# сравним appendleft и insert в начало списка

@time_measurement
def num_insert(a):
    for i in range(100000):
        a.insert(0, i)
    return a

@time_measurement
def dq_appendleft(a):
    for i in range(100000):
        a.appendleft(i)
    return a

num_insert(num)    # num_insert : 6.465112924575806 seconds
dq_appendleft(dq)  # dq_appendleft : 0.020966053009033203 seconds
# Тут видно, что deque много выигрывает по времени, документация не врет)

# сравним popleft и pop из начала списка

@time_measurement
def test1_pop(a):
    for i in range(len(a)):
        a.pop(0)
    return a

@time_measurement
def dq_popleft(a):
    for i in range(len(a)):
        a.popleft()
    return a

test1_pop(num)  # test1_pop : 0.26752495765686035 seconds
dq_popleft(dq)  # dq_popleft : 0.0015919208526611328 seconds
# Тут видно, что deque много выигрывает по времени, документация не врет)

# сравним extendleft и insert для начала списка

@time_measurement
def num1_insert(a):
    for i in range(10000):
        a.insert(0, ext)
    return a

@time_measurement
def dq_extendleft(a):
    for i in range(10000):
        a.extendleft(ext)
    return a

num1_insert(num)  # num1_insert : 0.20671486854553223 seconds
dq_extendleft(dq) # dq_extendleft : 0.007027864456176758 seconds
# Тут видно, что deque много выигрывает по времени, документация не врет)

# получим элемент по индексу и сравним время выполнения

@time_measurement
def get_by_index(a):
    for i in range(10000):
        c = a[995]

get_by_index(num)  # get_by_index : 0.0009779930114746094 seconds
get_by_index(dq)   # get_by_index : 0.0033118724822998047 seconds
# Тут видно, что deque много проигрывант по времени, документация не врет)

# в целом наши замеры подтвердили информацию из документации




