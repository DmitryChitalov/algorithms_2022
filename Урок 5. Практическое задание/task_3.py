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
from timeit import timeit as tt

n = 100
obj = list(range(2))
lst = list(range(n))
deq = deque(range(n))


# 1
def ls_append(lst):
    for i in range(n):
        lst.append(i)
    return lst


def deque_append(deq):
    for i in range(n):
        deq.append(i)
    return deq


def ls_pop(lst):
    for i in range(n):
        lst.pop()
    return lst


def deque_pop(deq):
    for i in range(n):
        deq.pop()
    return deq


def ls_extend(lst):
    for i in range(n):
        lst.extend(obj)
    return lst


def deque_extend(deq):
    for i in range(n):
        deq.extend(obj)
    return deq


# 2
def ls_popleft(lst):
    for i in range(len(lst)):
        lst.pop(0)
    return lst


def deque_popleft(deq):
    for i in range(n):
        deq.popleft()
    return deq


def ls_appendleft(lst):
    for i in range(n):
        lst.insert(0, i)
    return lst


def deque_appendleft(deq):
    for i in range(n):
        deq.appendleft(i)
    return deq


def ls_extendleft(lst):
    for i in range(n):
        lst.insert(0, obj)
    return lst


def deque_extendleft(deq):
    for i in range(n):
        deq.extendleft(obj)
    return deq


# 3
def ls_item(lst):
    for i in range(n):
        lst[i] = i
    return lst


def deque_item(deq):
    for i in range(n):
        deq[i] = i
    return deq


if __name__ == '__main__':
    print('1', end='\n' + '-' * 25 + '\n')
    print("ls_append()", tt("ls_append(lst.copy())", globals=globals()))
    print("deque_append()", tt("deque_append(deq.copy())", globals=globals()))
    print("ls_pop()", tt("ls_pop(lst.copy())", globals=globals()))
    print("deque_pop()", tt("deque_pop(deq.copy())", globals=globals()))
    print("ls_extend()", tt("ls_extend(lst.copy())", globals=globals()))
    print("deque_extend()", tt("deque_extend(deq.copy())", globals=globals()))
    print("""
    Операции append, pop, extend у списка и дека имеют одинаковую суть, но разную скорость выполнения:
    - append - у списка быстрее, но разница невелика.
    - pop - быстрей у дека, причём значительно
    - extend - у списка быстрей почти в 1,5 раза
    """)
    print('2', end='\n' + '-' * 25 + '\n')
    print("ls_appendleft()", tt("ls_appendleft(lst.copy())", globals=globals()))
    print("deque_appendleft()", tt("deque_appendleft(deq.copy())", globals=globals()))
    print("ls_popleft()", tt("ls_popleft(lst.copy())", globals=globals()))
    print("deque_popleft()", tt("deque_popleft(deq.copy())", globals=globals()))
    print("ls_extendleft()", tt("ls_extendleft(lst.copy())", globals=globals()))
    print("deque_extendleft()", tt("deque_extendleft(deq.copy())", globals=globals()))
    print("""
    Аналогичные операции в начале коллекции быстрее выполняет дек. Для чего в принципе он и был создан. 
    """)
    print('3', end='\n' + '-' * 25 + '\n')
    print("ls_item()", tt("ls_item(lst.copy())", globals=globals()))
    print("deque_item()", tt("deque_item(deq.copy())", globals=globals()))
    print("""
    С доступом к элементу коллекции лучше справляется список.
    Вывод:
    Если важней вставка или удаление элемента с любого конца коллекции, но не получение элемента,то лучше подойдёт дек. 
    В случае частого обращения к элементам коллекции, но редкого удаления или добавления данных, лучше список
    """)
