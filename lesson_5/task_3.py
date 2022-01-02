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

lst = list()
example = 'geekbrains'

for x in example:
    lst.append(x)
print(lst)

dqe = deque(example)
print(dqe)


def append_left(x):
    dqe.appendleft(x)
    return dqe


# 1) сравнить операции append, pop, extend списка и дека и сделать выводы что и где быстрее
print('Сравнение операции append')
print(timeit('lst.append("s")', globals=globals()))
print(timeit('dqe.append("s")', globals=globals()))

print('\nСравнение операции pop')
print(timeit('lst.pop()', globals=globals()))
print(timeit('dqe.pop()', globals=globals()))

print('\nСравнение операции extend')
print(timeit('lst.extend("geekbrains")', globals=globals()))
print(timeit('dqe.extend("geekbrains")', globals=globals()))
'''Операции append, pop и extend у дека быстрее, чем у списка.'''

# 2) сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка
print('\n\nСравнение операций insert и appendleft')
print(timeit('lst.insert(0, "G")', globals=globals(), number=1000))
print(timeit('append_left("G")', globals=globals(), number=1000))

print('\nСравние операций pop(index) и popleft')
print(timeit('lst.pop(0)', globals=globals(), number=1000))
print(timeit('dqe.popleft()', globals=globals(), number=1000))

print('\nСравнение операций объединения списков и extendleft')
print(timeit('["g", "e", "e", "k"] + lst', globals=globals(), number=100))
print(timeit('dqe.extendleft(["g", "e", "e", "k"])', globals=globals(), number=100))
'''Операции appendleft, popleft, extendleft у дека быстрее, чем соответствующие операции у списка.'''

# 3) сравнить операции получения элемента списка и дека
print('\n\nСравнение операции получения элемента списка и дека')
print(timeit('lst[0]', globals=globals()))
print(timeit('dqe[0]', globals=globals()))
'''Операция получения элемента списка быстрее, чем операция получения элемента дека.'''
