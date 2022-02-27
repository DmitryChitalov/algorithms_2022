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


def time_test(operations, stmt_list, stmt_deque, setup_list, setup_deque):
    for i in range(len(stmt_list)):
        print(f'Дек.: {operations[i]} за '
              f'{min(repeat(stmt_deque[i], setup_deque[i], default_timer, 5, 1000, globals=globals())):.4f}')
        print(f'Список: {operations[i]} за '
              f'{min(repeat(stmt_list[i], setup_list[i], default_timer, 5, 1000, globals=globals())):.4f}')
    print('--------------------')

"""
a)
Операции: append, pop, extend
имеют один и тот же порядок малости для списка и дека 
"""

length = 30  # длина массива
# numbers = 1000  # число запусков

operations = ['append', 'pop', 'extend']

setup_list = [
    f'obj=[]\nelems=range({length})',
    f'elems=range({length})\nobj=list(elems)*1000',
    f'obj=[]\nelems=range({length})'
    ]

setup_deque = [
    f'obj=deque()\nelems=range({length})',
    f'elems=range({length})\nobj=deque(list(elems)*1000)',
    f'obj=deque()\nelems=range({length})'
    ]

stmt = [
    'for i in elems:\n\tobj.append(i)',
    'for i in elems:\n\tobj.pop()',
    'for i in elems:\n\tobj.extend([i])'
    ]


time_test(operations, stmt, stmt, setup_list, setup_deque)


"""
b)
Операции: appendleft, popleft, extendleft
для дека выполняются быстрее, чем для списка, на порядок/два.
list есть динамический массив, который отлично подходит для быстрого произвольного доступа,
но требует периодического изменения размера при добавлении или удалении элементов. 
Список перераспределяет свое пространство хранения, так что не каждый push или pop требует изменения размера, 
обеспечивая производительность O(1). 
Но нужно быть осторожным при вставке и удалении элементов только справа (append и pop), 
иначе произойдёт снижение производительности до O(n). Что наблюдается в данном примере.
collection.deque является двусвязным списком, который оптимизирован для добавления и удаления 
с любой стороны и обеспечивает одинаковую производительность O(1) для этих операций. 
Производительность не только стабильна, но и сам класс deque проще, 
поскольку не нужно беспокоиться о добавлении или удалении элементов с «неправильного конца». 
"""

operations = ['appendleft', 'popleft', 'extendleft']

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

time_test(operations, stmt_list, stmt_deque, setup_list, setup_deque)


"""
c)
Операции: получение первого/последнего элемента
для списка и дека имеют практически одинаковое время выполнения
"""

operations = ['получение первого элемента', 'получение последнего элемента']

setup_list = [
    f'elems=range(1000)\nobj=list(elems)'
    ] * 2


setup_deque = [
    f'elems=range(1000)\nobj=deque(list(elems))'
    ] * 2

stmt = [
    'for i in elems:\n\tobj[0]',
    'for i in elems:\n\tobj[-1]'
    ]

time_test(operations, stmt, stmt, setup_list, setup_deque)
