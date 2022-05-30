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
from timeit import repeat, default_timer


def time_test(operations, stmt_list, stmt_deque, setup_list, setup_deque, repeats, numbers):
    for i in range(len(stmt_list)):
        res_list = repeat(stmt_list[i], setup_list[i], default_timer, repeats, numbers, globals=globals())
        res_deque = repeat(stmt_deque[i], setup_deque[i], default_timer, repeats, numbers, globals=globals())
        print(f'----------- Операция: {operations[i]} -----------')
        print(f'>Время  {"min":>8} {"mean":>8} {"max":>8}')
        print(f'Список: {min(res_list):>8.2f} {sum(res_list) / repeats:>8.2f} {max(res_list):>8.2f}')
        print(f'Дек:    {min(res_deque):>8.2f} {sum(res_deque) / repeats:>8.2f} {max(res_deque):>8.2f}')



"""
1) Операции: append, pop, extend
для списка и дека в среднем имеют практически одинаковое время выполнения 
"""

length = 1000  # длина массива
repeats = 100  # число замеров
numbers = 1000  # число запусков

operations = ['append', 'pop', 'extend']

setup_list = [
    f'obj=[]\nelems=range({length})',
    f'elems=range({length})\nobj=list(elems)*{numbers}',
    f'obj=[]\nelems=range({length})'
    ]

setup_deque = [
    f'obj=deque()\nelems=range({length})',
    f'elems=range({length})\nobj=deque(list(elems)*{numbers})',
    f'obj=deque()\nelems=range({length})'
    ]

stmt = [
    'for i in elems:\n\tobj.append(i)',
    'for i in elems:\n\tobj.pop()',
    'for i in elems:\n\tobj.extend([i])'
    ]


time_test(operations, stmt, stmt, setup_list, setup_deque, repeats, numbers)



"""
2) Операции: appendleft, popleft, extendleft
для дека выполняются гораздо быстрее, чем для списка
"""

length = 30  # длина массива
repeats = 100  # число замеров
numbers = 1000  # число запусков

operations = ['appendleft', 'popleft', 'extendleft']

setup_list = [
    f'obj=[]\nelems=range({length})',
    f'elems=range({length})\nobj=list(elems)*{numbers}',
    f'obj=[]\nelems=range({length})'
    ]

setup_deque = [
    f'obj=deque()\nelems=range({length})',
    f'elems=range({length})\nobj=deque(list(elems)*{numbers})',
    f'obj=deque()\nelems=range({length})'
    ]

stmt_list = [
    'for i in elems:\n\tobj.insert(i, 0)',
    'for i in elems:\n\tobj.pop(0)',
    'for i in elems:\n\tobj = [i] + obj'
    ]

stmt_deque = [
    'for i in elems:\n\tobj.appendleft(i)',
    'for i in elems:\n\tobj.popleft()',
    'for i in elems:\n\tobj.extendleft([i])'
    ]


time_test(operations, stmt_list, stmt_deque, setup_list, setup_deque, repeats, numbers)



"""
3) Операции: получение первого/последнего элемента
для списка и дека в среднем имеют практически одинаковое время выполнения
Операция: получение произвольного элемента по индексу
для списка будет работать гораздо быстрее, чем для дека, т.к. в случае списка
достаточно обратиться к нужному элементу по индексу, а для дека
необходимо будет подбираться к нужному элементу с той или другой стороны
путем удаления ненужных элементов
"""

length = 1000  # длина массива
repeats = 100  # число замеров
numbers = 1000  # число запусков

operations = ['получение первого элемента', 'получение последнего элемента']

setup_list = [
    f'elems=range({length})\nobj=list(elems)'
    ] * 2


setup_deque = [
    f'elems=range({length})\nobj=deque(list(elems))'
    ] * 2

stmt = [
    'for i in elems:\n\tobj[0]',
    'for i in elems:\n\tobj[-1]'
    ]


time_test(operations, stmt, stmt, setup_list, setup_deque, repeats, numbers)