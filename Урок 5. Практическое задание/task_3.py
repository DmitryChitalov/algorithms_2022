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
lst = [randint(0, 100000) for _ in range(100000)]
dqe = deque(lst)

def list_extend_left(to_lst, from_lst):
    for _ in range(len(from_lst)):
        to_lst.insert(0, from_lst.pop())
    return None

print('append')
print(timeit("lst.append(1)", globals=globals(), number=1000000)) #Время выполнения 0.08418579799999998
print(timeit("dqe.append(1)", globals=globals(), number=1000000)) #Время выполнения 0.08410543100000001 практически одинаково
print('*' * 50 + '\n')
print('pop')
print(timeit("lst.pop()", globals=globals(), number=1000000)) #Время выполнения 0.077913069
print(timeit("dqe.pop()", globals=globals(), number=1000000)) #Время выполнения 0.07540786699999996 практически одинаково
print('*' * 50 + '\n')
print('extend')
print(timeit("lst.extend([2, 3, 4, 5, 6, 7, 8, 9])", globals=globals(), number=1000000)) #Время выполнения 0.21260749700000003
print(timeit("dqe.extend([2, 3, 4, 5, 6, 7, 8, 9])", globals=globals(), number=1000000)) #Время выполнения 0.282618775 практически одинаково
print('*' * 50 + '\n')
print('appendleft')
print(timeit("lst.insert(0, 3)", globals=globals(), number=1000)) #Время выполнения 6.861881671
print(timeit("dqe.appendleft(3)", globals=globals(), number=1000)) #Время выполнения 9.351599999973814e-05 dramatic difference!
print('*' * 50 + '\n')
print('popleft')
print(timeit("lst.pop(0)", globals=globals(), number=1000)) #Время выполнения 6.798438076
print(timeit("dqe.popleft()", globals=globals(), number=1000)) #Время выполнения 9.935900000002107e-05 dramatic difference!
print('*' * 50 + '\n')
print('extendleft')
print(timeit("list_extend_left(lst, [2, 3, 4, 5, 6, 7, 8, 9])", globals=globals(), number=1000)) #Время выполнения 56.115290347000006 !!!!
print(timeit("dqe.extendleft([2, 3, 4, 5, 6, 7, 8, 9])", globals=globals(), number=1000)) #Время выполнения 0.0002955730000024914

# Итог: специфические для deque функции, такие как appendleft, popleft, extendleft, работают гораздо быстрее для deque, чем аналогичные функции для list


