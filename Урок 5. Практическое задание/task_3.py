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
from random import randint

main_li = [i for i in range(100)]
li = main_li.copy()
de = deque(li.copy())
test_li = [randint(1,99) for _ in range(5)]


def li_append():
    for i in test_li:
        li.append(i)

def de_append():
    for i in test_li:
        de.append(i)

def li_pop():
    for _ in range(100):
        li.pop()

def de_pop():
    for _ in range(100):
        de.pop()

def li_extend():
    li.extend(test_li)

def de_extend():
    de.extend(test_li)

# l_app = timeit(li_append,globals = globals(), number=10000)
# d_app = timeit(de_append,globals = globals(), number=10000)
# l_pop = timeit(li_pop,globals = globals(), number=1)
# d_pop = timeit(de_pop,globals = globals(), number=1)
# l_extend = timeit(li_extend,globals = globals(), number=10000)
# d_extend = timeit(de_extend,globals = globals(), number=10000)
# print(l_pop, d_pop, 'test')
# print(f'сравнение списка с деком насколько % дек быстрее списка:\n при расширении {d_app*100/l_app} \n \
# при вырезании {d_pop*100/l_pop},\n при обьеденении {d_extend*100/l_extend}')
'''
сравнение deque со списком насколько % дек быстрее списка:
 при добавлении 84.1635816718657 
 при вырезании 90.10068381491539,
 при обьеденении 165.1381857370785

Выводы при append и pop быстрее у дека(<100%) а extend быстрее у списка (>100%)

'''
# 2 
def de_appendleft():
    for i in test_li:
        de.appendleft(i)

def li_appendleft():
    for i in test_li:
        li.insert(0,i)

def de_popleft():
    for _ in test_li:
        de.popleft()

def li_popleft():
    for _ in test_li:
        li.pop(0)

def de_extendleft():
    de.extendleft(test_li)

def li_extendleft():
    new_li = []
    new_li.extend(test_li)
    new_li.extend(li)


d_appendleft = timeit(de_appendleft,globals = globals(), number=1000)
l_appendleft = timeit(li_appendleft,globals = globals(), number=1000)
d_popleft = timeit(de_popleft,globals = globals(), number=1)
l_popleft = timeit(li_popleft,globals = globals(), number=1)
d_extendleft = timeit(de_extendleft,globals = globals(), number=1000)
l_extendleft = timeit(li_extendleft,globals = globals(), number=1000)
print(l_appendleft,d_appendleft)
print(f'сравнение списка с деком насколько % дек быстрее списка:\n при appendleft {d_appendleft*100/l_appendleft}\n \
при popleft {d_popleft*100/l_popleft}\n \
при extendleft {d_extendleft*100/l_extendleft}')

'''
сравнение списка с деком насколько % дек быстрее списка:
 при appendleft 5.037506524249985
 при popleft 30.807461696721415
 при extendleft 1.7679838084417203
 
 выводы все значения <100%: при данных операциях дек гораздо быстрее списка
 '''

# 3 получение элемента из списка и дека

def li_pop_i():
    for i in test_li:
        li[i]

def de_pop_i():
    for i in test_li:
        de[i]

d_pop_i = timeit(de_pop_i, globals = globals(), number=1)
l_pop_i = timeit(li_pop_i, globals = globals(), number=1)
print(f'получение элемента из списка проходит за {l_pop_i}\n\
получение элемента из дека проходит за {d_pop_i}\n\
{d_pop_i*100/l_pop_i} > 100 % ')


'''
получение элемента из списка проходит за 1.059999704011716e-06
получение элемента из дека проходит за 1.4300003385869786e-06
134.90572998982395 > 100 % 
Выводы из списка по индексу элемент получить гораздо быстрее
'''