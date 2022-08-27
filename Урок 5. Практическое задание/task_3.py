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


# Сравниваю операции append, pop, extend
my_list = []
my_deque = deque()
for_extend = [1, 2, 3]


print('append_func(my_list)', timeit("""
for i in range(100):
    my_list.append(1)""", globals=globals()))

print('pop_func(my_list)', timeit("""
for i in range(100):
    my_list.pop()""", globals=globals()))

print('extend_func(my_list)', timeit("""
for i in range(100):
    my_list.extend(for_extend)""", globals=globals()))
my_list.clear()

print('append_func(my_deque)', timeit("""
for i in range(100):
    my_deque.append(1)""", globals=globals()))

print('pop_func(my_deque)', timeit("""
for i in range(100):
    my_deque.pop()""", globals=globals()))

print('extend_func(my_deque)', timeit("""
for i in range(100):
    my_deque.extend(for_extend)""", globals=globals()))
my_deque.clear()

"""
Результаты:
        append_func(my_list) 37.0279414
            pop_func(my_list) 20.107726400000004
                extend_func(my_list) 87.7690196
        append_func(my_deque) 11.819256599999989
            pop_func(my_deque) 9.834385200000014
                extend_func(my_deque) 24.896275099999997
Вывод:
        Вставка данных в конец и pop с конца в деке осуществляется быстрее,
        чем в списке.
"""

# Сравниваю appendleft, popleft, extendleft

print('appendleft - list = ', timeit("""
for i in range(100):
    my_list.insert(0, 1)""", globals=globals(), number=2000))

print('popleft - list = ', timeit("""
for i in range(100):
    my_list.pop(0)""", globals=globals(), number=2000))

print('extendleft - list = ', timeit("""
for i in for_extend[::-1]:
    my_list.insert(0, i)""", globals=globals(), number=10000))
my_list.clear()

print('appendleft - deque = ', timeit("""
for i in range(100):
    my_deque.appendleft(1)""", globals=globals(), number=2000))

print('popleft - deque = ', timeit("""
for i in range(100):
    my_deque.popleft()""", globals=globals(), number=2000))

print('extendleft - deque = ', timeit("""
for i in range(100):
    my_deque.extendleft(for_extend)""", globals=globals(), number=10000))
my_deque.clear()

"""
Результаты:
        appendleft - list =  41.152481599999994
            popleft - list =  11.216579199999998
                extendleft - list =  0.7733928000000034
        appendleft - deque =  0.04241929999999883
            popleft - deque =  0.03181289999999848
                extendleft - deque =  0.338146100000003
Вывод:
        Добавление в начало и pop с начала списка в деке
        осуществляется гораздно быстрее, чем в списке.
"""


# Сравниваю скорость получения элемента
for i in range(201):
    my_list.append(i)
    my_deque.append(i)

print('Получение элемента - list = ', timeit("""
for i in range(200):
    a = my_list[i]""", globals=globals()))

print('Получение элемента - deque = ', timeit("""
for i in range(200):
    a = my_deque[i]""", globals=globals()))

"""
Результаты:
        Получение элемента - list =  30.9816783
        Получение элемента - deque =  28.2499809
Вывод: 
        Получение элемента по идексу осуществляется
        с одинаковыми временными результатами.
"""