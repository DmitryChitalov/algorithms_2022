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

"""
ВЫВОДЫ:
тестировалось на версии пайтон 3.10
В первом и втором пункте дек оказался быстрее в каждом тесте, подробности в таблице. 
В третьем медленее, полагаю из-за более сложной организации дека.
 
Получается документация верна.
"""

from collections import deque
from timeit import timeit
from prettytable import PrettyTable
from random import randint


def add_result_row(operation, code_list, code_dq, result_table):
    print(f'{operation}.....')

    l_time = round(timeit(code_list, number=number, globals=globals()), 6)
    d_time = round(timeit(code_dq, number=number, globals=globals()), 6)

    percent = round(100 * (l_time - d_time) / l_time if l_time > d_time else 100 * (d_time - l_time) / d_time)
    result = f'Быстрее {"список" if l_time < d_time else "дек"}'

    result_table.add_row([f'{operation}', l_time, d_time, length, number, result, percent])
    # result_table.add_row(['', '', '', '', '', '', ''])


lst = list()
dq = deque()
tmp_list = list(range(100))
tmp_dq = deque(range(100))

result_table = PrettyTable()
result_table.field_names = ['Операция (список/дек)', 'Список', 'Дек', 'Элементы', 'Замеры', 'Результат', '%']
result_table.align['Операция (список/дек)'] = "l"
result_table.align['Результат'] = "l"

print('Вычисление.....')

result_table.add_row(['Пункт 1)', '-', '-', '-', '-', '-', '-'])

length = 1000
number = 1000
add_result_row('append',
               '''for i in range(length):
                      lst.append(i)
               ''',
               '''for i in range(length):
                      dq.append(i)
               ''', result_table)

add_result_row('pop',
               '''for i in range(length):
                      lst.pop()
               ''',
               '''for i in range(length):
                      dq.pop()
               ''', result_table)

add_result_row('extend',
               '''for i in range(1000):
                      lst.extend(tmp_list)
               ''',
               '''for i in range(1000):
                      dq.extend(tmp_dq)
               ''', result_table)

result_table.add_row(['Пункт 2)', '-', '-', '-', '-', '-', '-'])
length = 100
number = 1000
lst = list()
dq = deque()

add_result_row('appendleft',
               '''for i in range(length):
                      lst.insert(0, i)
               ''',
               '''for i in range(length):
                      dq.appendleft(i)
               ''', result_table)

add_result_row('popleft',
               '''for i in range(length):
                      lst.pop(0)
               ''',
               '''for i in range(length):
                      dq.popleft()
               ''', result_table)

number = 10

add_result_row('extendleft',
               '''for i in range(length):
                      for j in range(len(tmp_list)):
                          lst.insert(0, j)
               ''',
               '''for i in range(length):
                      dq.extendleft(tmp_dq)
               ''', result_table)

result_table.add_row(['Пункт 3)', '-', '-', '-', '-', '-', '-'])
length = 1000
number = 1000

add_result_row('get random',
               '''for i in range(length):
                      _ = lst[randint(0, len(lst) - 1)]
               ''',
               '''for i in range(length):
                      _ = dq[randint(0, len(dq) - 1)]
               ''', result_table)

print(result_table)
