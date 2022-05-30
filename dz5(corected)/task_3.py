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
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

'''
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
'''
lst_deque = deque()
lst_1 = []


def append_num(lst):
    for i in range(1000):
        lst.append(i)
    return lst


# print('------------------------------------------------')
# print(f"Замер append() у дека: {timeit('append_num(lst_deque)', globals=globals(), number=1)}")
# print('------------------------------------------------')
# print(f"Замер append() у списка: {timeit('append_num(lst_1)', globals=globals(), number=1000)}")
'''
Замеры скорости показали, что функция append() работает c одинаковой скоростью всписке и деке.
'''


def pop_num(lst):
    for i in range(999):
        lst.pop()
    return lst


lst_2 = [i for i in range(1000)]
deque_2 = deque([i for i in range(1000)])

# print('------------------------------------------------')
# print(f"Замер pop() списка: {timeit('pop_num(lst_2)', globals=globals(), number=1)}")
# print('------------------------------------------------')
# print(f"Замер pop() дека: {timeit('pop_num(deque_2)', globals=globals(), number=1)}")
'''
Замеры времени функции pop() показали, время на удаление элементов в списке, такое же как в деке.
pop() в деке и списке равен по скорости
'''


def extend_num(lst):
    num = [i for i in range(1000)]
    lst.extend(num)
    return lst


print('------------------------------------------------')
print(f"Замер extend() в списке: {timeit('extend_num(lst_1)', globals=globals(), number=1000)}")
print(f"Замер extend() в деке: {timeit('extend_num(lst_deque)', globals=globals(), number=1000)}")
'''
Замеры времени extend показали, что функция extend() работает c одинаковой скорость в списке и деке.
'''

'''
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
'''
lst_3 = []
deque_3 = deque()


def insert_num(lst):
    for i in range(1000):
        lst.insert(0, i)
    return lst


def appendleft_num(lst):
    for i in range(1000):
        lst.appendleft(i)
    return lst


print('------------------------------------------------')
print(f"Замер insert(0) списка: {timeit('insert_num(lst_3)', globals=globals(), number=100)}")
print(f"Замер appendleft() дека: {timeit('appendleft_num(deque_3)', globals=globals(), number=100)}")
'''
Замеры appendleft() дека и insert() списка показали, что дек работает значительно быстрее.
Список работает медленее потому что, при вставке в начало списка, сем следующим элементам нужно изменить индекс,
на это уходит много времени.
'''


def popleft_lst(lst):
    for i in range(990):
        lst.pop(0)
    return lst


def popleft_deque(dq):
    for i in range(990):
        dq.popleft()
    return dq


print('------------------------------------------------')
print(f"Замер popleft() в деке: {timeit('popleft_deque(deque_2)', globals=globals(), number=1)}")
print(f"Замер pop(0) в списке: {timeit('popleft_lst(lst_2)', globals=globals(), number=1)}")
print('------------------------------------------------')

'''
Замеры popleft() дека и pop(0) списка показали что удаление элемента из начала списка быстрее выполняется у дека, 
так как при удалении первого улемента в списке, всем следующим присвайвается новый индекс, а это занимает ресурсы.
'''


def extendleft_dq(dq):
    num = [i for i in range(1000)]
    dq.extendleft(num)
    return dq


print(f"Замер extendleft() в деке: {timeit('extendleft_dq(lst_deque)', globals=globals(), number=1000)}")
'''
Замеры extendleft() показали что добавление в начало дека происходит значительно быстрее, 
чем добавление в начало списка при помощи функции insert(я уже замерял выше)
Дело все в тех же индексах списка, при добавлении элемента в начало списка, индексы всех следующих элементов меняются.
'''

'''
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
'''


def lst_receiving(lst):
    n = 0
    for i in lst:
        if n < 10:
            n += 1
            return i
        else:
            break


def dq_receiving(dq):
    n = 0
    for i in dq:
        if n < 10:
            n += 1
            return i
        else:
            break


print('------------------------------------------------')
print(f"Замер получения 10 элементов из дека: {timeit('dq_receiving(deque_2)', globals=globals(), number=100)}")
print(f"Замер получения 10 элементов списка: {timeit('lst_receiving(lst_2)', globals=globals(), number=100)}")

'''
Замеры получения 10 элементов из списка и дека, показывают, что из списка получить элементы получается быстрее, 
у дека получение 10 элементов через цикл занимает больше времени, а вот если вытаскивать по однму элементу, 
тогда дек будет работать быстрее.
'''
