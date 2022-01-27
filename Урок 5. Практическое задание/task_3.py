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

'''
Exercise #1
'''
print('-'*50, 1, '-'*50)

test_deque = deque()


def fill_in_the_deque():
    for i in range(10000):
        test_deque.append(i)


test_list = []


def fill_in_the_list():
    for i in range(10000):
        test_list.append(i)


print('Заполнение очреди - ', timeit('fill_in_the_deque()', globals=globals(), number=1000),
      '\nЗаполнение списка - ', timeit('fill_in_the_list()', globals=globals(), number=1000))


def pop_deque():
    for i in range(1, 10000, 2):
        test_deque.pop()


def pop_list():
    for i in range(1, 10000, 2):
        test_list.pop()


print('pop в deque - ', timeit('pop_deque()', globals=globals(), number=1000),
      '\npop в list - ', timeit('pop_list()', globals=globals(), number=1000))

# extended_list = [i for i in range(1000)]


def extend_deque():
    for i in range(100):
        test_deque.extend({1, 2, 3})


def extend_list():
    for i in range(100):
        test_list.extend({1, 2, 3})


print('Присоединение к очереди - ', timeit('extend_deque()', globals=globals(), number=1000),
      '\nПрисоединение к списку - ', timeit('extend_list()', globals=globals(), number=1000))

'''
Команды append, pop и extend в списке и очереди занимает примерно одно и тоже время
'''

'''
Exercise #2
appendleft, popleft, extendleft
'''
print('-'*50, 2, '-'*50)

test_list = []
test_deque = deque()


def appendleft_deque():
    for i in range(1000):
        test_deque.appendleft(i)


def appendleft_list():
    for i in range(1000):
        test_list.insert(0, i)


print('appendleft в deque - ', timeit('appendleft_deque()', globals=globals(), number=100),
      '\nappendleft в list - ', timeit('appendleft_list()', globals=globals(), number=100))


def popleft_deque():
    for i in range(1, 1000, 2):
        test_deque.popleft()


def popleft_list():
    for i in range(1, 1000, 2):
        test_list.pop(0)


print('popleftdeque в deque - ', timeit('popleft_deque()', globals=globals(), number=100),
      '\npopleftlist в list - ', timeit('popleft_list()', globals=globals(), number=100))


def extendleft_deque():
    for i in range(100):
        test_deque.extendleft([1, 2, 3])


def extendleft_list():
    for i in range(100):
        test_list.insert(0, [1,2,3])


print('extendleftdeque в deque - ', timeit('extendleft_deque()', globals=globals(), number=100),
      '\nextendleftlist в list - ', timeit('extendleft_list()', globals=globals(), number=100))

'''
appendleft, popleft, extendleft во много раз быстрее работают с очередями, чем со списком 
'''

'''
Exercise #3
'''
print('-'*50, 3, '-'*50)


def get_elem_deque():
    for i in range(10000):
        test_deque[i] = i


def get_elem_list():
    for i in range(10000):
        test_list[i] = i


print('Получение элемента в deque - ', timeit('get_elem_deque()', globals=globals(), number=100),
      '\nПолучение элемента в list - ', timeit('get_elem_list()', globals=globals(), number=100))
'''
Получение элементов в deque происходит медленнее чем в list
'''