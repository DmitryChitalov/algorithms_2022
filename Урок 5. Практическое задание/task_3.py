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


my_list = [i for i in range(1, 101)]
my_deque = deque(my_list)

"""
Первая часть.
Кроме 'append', операции в деке выполняются медленнее чем в списке.
append(list)
0.003806999997323146
pop(list)
0.0037100999979884364
extend(list)
0.006031099997926503
append(deque)
0.00355919999856269
pop(deque)
0.003950899998017121
extend(deque)
0.013307699999131728
__________________________________________________________________
"""


def my_append_1(my_list):
    for i in range(101, 201):
        my_list.append(i)


def my_pop_1(my_list):
    for i in range(101, 201):
        my_list.pop()


def my_extend_1(my_list):
    for i in range(101, 201):
        my_list.extend([i])


def deque_append_1(my_deque):
    for i in range(101, 201):
        my_deque.append(i)


def deque_pop_1(my_deque):
    for i in range(101, 201):
        my_deque.pop()


def deque_extend_1(my_deque):
    for i in range(101, 201):
        my_deque.extend([i])


print(timeit("my_append_1(my_list)", globals=globals(), number=1000))
print(timeit("my_pop_1(my_list)", globals=globals(), number=1000))
print(timeit("my_extend_1(my_list)", globals=globals(), number=1000))
print(timeit("deque_append_1(my_deque)", globals=globals(), number=1000))
print(timeit("deque_pop_1(my_deque)", globals=globals(), number=1000))
print(timeit("deque_extend_1(my_deque)", globals=globals(), number=1000))


"""
Вторая часть.
Операции дека выполняются в разы быстрее чем в списке.
Операции списка
0.3929520000019693
0.17240090000268538
1.5817197000033048
Операции дека
0.00351790000058827
0.00337270000090939
0.008672399999340996
__________________________________________________________________
"""


def my_append_2(my_list):
    for i in range(50):
        my_list.insert(0, i)


def my_pop_2(my_list):
    for i in range(len(my_list)):
        my_list.pop(0)


def my_extend_2(my_list):
    for i in range(101, 201):
        my_list.insert(0, [i])


def deque_append_2(my_deque):
    for i in range(101, 201):
        my_deque.appendleft(i)


def deque_pop_2(my_deque):
    for i in range(101, 201):
        my_deque.popleft()


def deque_extend_2(my_deque):
    for i in range(101, 201):
        my_deque.extendleft([i])


print(timeit("my_append_2(my_list)", globals=globals(), number=1000))
print(timeit("my_pop_2(my_list)", globals=globals(), number=1000))
print(timeit("my_extend_2(my_list)", globals=globals(), number=1000))
print(timeit("deque_append_2(my_deque)", globals=globals(), number=1000))
print(timeit("deque_pop_2(my_deque)", globals=globals(), number=1000))
print(timeit("deque_extend_2(my_deque)", globals=globals(), number=1000))


"""
Третья часть.
Получение элемента из списка незначительно быстрее.

__________________________________________________________________
"""



def my_def_1(my_list):
    for i in range(50):
        my_list[i] = i


def my_def_2(my_deque):
    for i in range(50):
        my_deque[i] = i


print(timeit("my_def_1(my_list)", globals=globals(), number=1000))
print(timeit("my_def_2(my_deque)", globals=globals(), number=1000))