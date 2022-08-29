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

"""
1 пункт
Обычное добавление в список и дек
0.48587444399981905
0.48121112100034225
Обычное удаление последнего элемента в списке и деке
0.4150575199996638
0.3974622460000319
Обычное расширение списка и дека
0.08285231899981227
0.09022849599999972

Итог: обычные методы работают +- одинаково в списке и в деке

2 пункт

append left
39.161681729000065
0.00035417899971434963
pop left
30.120948860000226
0.00032577799993305234
extend left
37.98122809300003
0.0009549370001877833

Итог: обработка с левой стороны в деке намного быстрее, чем в списке

3 пункт, поиск элемента

искала разные элементы, получить элемент по индексу из списка быстрее

0.032826693000060914
0.07214827600000717
0.03316376900011164
0.0723532939996403
0.033228707000034774
0.07231778799996391
"""

from collections import deque
from timeit import timeit
from random import randint

print('1 пункт')

# append
print('Обычное добавление в список и дек')

lst_lst = [i for i in range(1000)]
deq_deq = deque(i for i in range(1000))


def append_lst(lst):
    for i in range(1000):
        lst.append(i)
    return lst


def append_deq(deq):
    for i in range(1000):
        deq.append(i)
    return deq


print(timeit('append_lst(lst_lst)', globals=globals(), number=10000))
print(timeit('append_deq(deq_deq)', globals=globals(), number=10000))

# 2) pop
print('Обычное удаление последнего элемента в списке и деке')


def pop_lst(lst):
    for i in range(1000):
        lst.pop()
    return lst


def pop_deq(deq):
    for i in range(1000):
        deq.pop()
    return deq


print(timeit('pop_lst(lst_lst)', globals=globals(), number=10000))
print(timeit('pop_deq(deq_deq)', globals=globals(), number=10000))

# 3) extend
print('Обычное расширение списка и дека')


def extend_lst(lst):
    for i in range(100):
        lst.extend([1, 2, 3, 4, 5])
    return lst


def extend_deq(deq):
    for i in range(100):
        deq.extend([1, 2, 3, 4, 5])
    return deq


print(timeit('extend_lst(lst_lst)', globals=globals(), number=10000))
print(timeit('extend_deq(deq_deq)', globals=globals(), number=10000))

print('2 пункт')
# вставка слева
print('append left')


def app_left_lst(lst):
    for i in range(100):
        lst.insert(0, i)
    return lst


def app_left_deq(deq):
    for i in range(100):
        deq.appendleft(i)
    return deq


print(timeit('app_left_lst(lst_lst)', globals=globals(), number=100))
print(timeit('app_left_deq(deq_deq)', globals=globals(), number=100))

print('pop left')


# pop слева


def pop_left_lst(lst):
    for i in range(100):
        lst.pop(i)
    return lst


def pop_left_deq(deq):
    for i in range(100):
        deq.popleft()
    return deq


print(timeit('pop_left_lst(lst_lst)', globals=globals(), number=100))
print(timeit('pop_left_deq(deq_deq)', globals=globals(), number=100))

# расширение слева

print('extend left')


def ex_le_lst(lst):
    for i in range(100):
        lst.insert(0, [1, 2, 3, 4, 5])
    return lst


def ex_le_deq(deq):
    for i in range(100):
        deq.extendleft([1, 2, 3, 4, 5])
    return deq


print(timeit('ex_le_lst(lst_lst)', globals=globals(), number=100))
print(timeit('ex_le_deq(deq_deq)', globals=globals(), number=100))
print('3 пункт, поиск элемента')

# добываем элемент из списка случайных чисел


# new_lst = list(randint(0, 1000) for i in range(100))
# new_deq = deque(randint(0, 1000) for j in range(100))

new_lst = [i for i in range(10000)]
new_deq = deque(i for i in range(10000))


def find_el_lst(lst, el):
    for i in range(len(lst)):
        lst[i] = el
    return i


def find_el_deque(deq, el):
    for i in range(len(deq)):
        deq[i] = el
    return i


# погоняем на дальность поиска от начала
print(timeit('find_el_lst(new_lst, 100)', globals=globals(), number=100))
print(timeit('find_el_lst(new_deq, 100)', globals=globals(), number=100))
print(timeit('find_el_lst(new_lst, 1000)', globals=globals(), number=100))
print(timeit('find_el_lst(new_deq, 1000)', globals=globals(), number=100))
print(timeit('find_el_lst(new_lst, 10000)', globals=globals(), number=100))
print(timeit('find_el_lst(new_deq, 10000)', globals=globals(), number=100))
