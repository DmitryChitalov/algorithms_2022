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
from collections import deque
from random import randint

lst = []
deq = deque()
# 1)########################
print('операции append, pop, extend')
for i in range(1, 1000):
    lst.append(i)

lst_app = """
for i in range(1, 1000):
    lst.append(i)"""

print(timeit(lst_app, globals=globals(), number=1000), 'lst_app')

for i in range(1, 1000):
    deq.append(i)


deq_app = """
for i in range(1, 1000):
    deq.append(i)"""

print(timeit(deq_app, globals=globals(), number=1000), 'deq_app')

while lst:
    lst.pop()

lst_pop = """
while lst:
    lst.pop()"""
print(timeit(lst_pop, globals=globals(), number=100000), 'lst_pop')

while deq:
    deq.pop()

deq_pop = """
while deq:
    deq.pop()"""

print(timeit(deq_pop, globals=globals(), number=100000), 'deq_pop')

lst.extend([n for n in range(1, 1000)])
print(timeit("""lst.extend([n for n in range(1, 1000)])""", globals=globals(), number=1000), 'lst_extend')
deq.extend([n for n in range(1, 1000)])
print(timeit("""deq.extend([n for n in range(1, 1000)])""", globals=globals(), number=1000), 'deq_extend')

# 2)##########################
print('операции appendleft, popleft, extendleft дека и соответствующих им операций списка')
for i in range(1, 1000):
    lst.insert(0, i)

lst_insert = """
for i in range(1, 1000):
    lst.insert(0, i)"""

print(timeit(lst_insert, globals=globals(), number=3), 'lst_insert')

for i in range(1, 1000):
    deq.appendleft(i)

deq_appleft = """
for i in range(1, 1000):
    deq.appendleft(i)"""

print(timeit(deq_appleft, globals=globals(), number=3), 'deq_appleft')

lst = [n for n in range(1, 1000)]

while lst:
    lst.pop(0)

lst_pop_0 = """
while lst:
    lst.pop(0)"""

print(timeit(lst_pop_0, globals=globals(), number=10000), 'lst_pop_0')

deq = deque(n for n in range(1, 1000))

while deq:
    deq.popleft()

deq_popleft = """
while deq:
    deq.popleft()"""

print(timeit(deq_popleft, globals=globals(), number=10000), 'deq_popleft')

lst = [n for n in range(1, 100000)]
lst[0:0] = [n for n in range(1, 1000)]
print(timeit("""lst[0:0] = [n for n in range(1, 1000)]""", globals=globals(), number=1000), 'lst_extendleft')

deq = deque(n for n in range(1, 100000))
deq.extendleft([n for n in range(1, 1000)])
print(timeit("""deq.extend([n for n in range(1, 1000)])""", globals=globals(), number=1000), 'deq_extendleft')

# 3)####################
print('операции получения элемента списка и дека')

lst = [n for n in range(1, 1000)]
deq = deque(n for n in range(1, 1000))
for i in range(1, 1000):
    n = lst[randint(0, 998)]

lst_get = """
for i in range(1, 1000):
    n = lst[randint(0, 998)]"""

print(timeit(lst_get, globals=globals(), number=1000), 'lst_get')

for i in range(1, 1000):
    n = deque[randint(0, 998)]

deq_get = """
for i in range(1, 1000):
    n = deque[randint(0, 998)]"""

print(timeit(deq_get, globals=globals(), number=1000), 'deq_get')


# операции append, pop, extend:
# 0.06023230007849634 lst_app -- меняется длина списка
# 0.045390300219878554 deq_app -- добавление в очередь быстрее, соответствует документации
# 0.0018557000439614058 lst_pop -- доступ просто по индексу
# 0.0019164001569151878 deq_pop -- вытащить элемент из очереди медленнее, несоответствует документации
# 0.040671300143003464 lst_extend -- вычисляется длина списка, и индексы
# 0.03151090000756085 deq_extend -- расширение очереди быстрее чем списка
#################################
# операции appendleft, popleft, extendleft дека и соответствующих им операций списка:
# 1.1780683000106364 lst_insert -- вычисляется длина списка, и индексы
# 0.0001308000646531582 deq_appleft  -- добавление слева быстрее в очереди, соответствует документации
# 0.00016300007700920105 lst_pop_0   -- вытаскивание элемента из начала списка быстрее чем из очереди
# 0.00018289987929165363 deq_popleft -- не ясно почему
# 0.211295299930498 lst_extendleft -- вычисляется длина списка, и индексы
# 0.031259399838745594 deq_extendleft -- расширение слева также быстрее у deque
#######################################
# операции получения элемента списка и дека:
# 0.5564425000920892 lst_get -- доступ к элементу списка быстрее чем очереди, что соответствует документации
# 0.6501677001360804 deq_get

# Вывод: списки настроены на работу с индексами, а очереди на потоки данных
# добавление быстрее в deque, доступ к элементу быстрее в list



