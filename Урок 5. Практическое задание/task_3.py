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

def list_extendleft(lst1,lst2):
    lst2.reverse()
    for el in lst2:
        lst1.insert(0,el)

#1)
if __name__ == '__main__':

    lst = []
    deq = deque()
    test_str = 'test'
    print("Пункт 1: ")
    print(f' append list: {timeit("lst.append(1)", globals=globals())}')
    print(f' append deque: {timeit("deq.append(1)", globals=globals())}')
    print('********************************************************')
    print(f' pop list: {timeit("lst.pop()", globals=globals())}')
    print(f' pop deque: {timeit("deq.pop()", globals=globals())}')
    print('********************************************************')
    print(f' extend list: {timeit("lst.extend(test_str)", globals=globals())}')
    print(f' extend deque: {timeit("deq.extend(test_str)", globals=globals())}')
"""
    По результатам замеров по операциям append,pop,extend  - deque немного быстрее чем list
    самая большая разница на операции extend
    по данным операциям разница не значительная можно использовать оба объекта
"""

#2)
print("Пункт 2 ")

print(f' insert[0] list: {timeit("lst.insert(0,1)",number=1000, globals=globals())}')
print(f' appendleft deque: {timeit("deq.appendleft(1)",number=1000, globals=globals())}')
print('********************************************************')
print(f' pop(0) list: {timeit("lst.pop(0)",number=1000, globals=globals())}')
print(f' popleft deque: {timeit("deq.popleft()",number=1000, globals=globals())}')
print('********************************************************')
print(f' extend list: {timeit("list_extendleft(lst,list(test_str))",number=1000, globals=globals())}')
print(f' extendleft deque: {timeit("deq.extend(test_str)",number=1000, globals=globals())}')

"""
    По результатам замеров по операциям  appendleft,pop,extend  - deque гораздо быстрее в 10000 раз
    если необходимо вставлять и получать в начало списка надо использовать deque
"""

#3)
print("Пункт 3 ")

lst = [i for i in range(1000)]

print(f' получение по индексу list: {timeit("lst[501]",number=1000, globals=globals())}')
print(f' получение по индексу deque: {timeit("deq[501]",number=1000, globals=globals())}')

"""
    По результатам замеров по операци получения по индексу список примерно в 2 раза быстрее
    
    Общий вывод: deque имеет смысл использовать когда мы в основном работаем на получение и удаление элементов
    с обоих сторон списка или только с головы. В остальных случаях нет преимуществ со списком_
"""
