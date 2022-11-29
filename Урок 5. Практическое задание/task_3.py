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
import collections
import timeit


# initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn', 'eleventh', 'twelveth']
# list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark', 'Sebastian Vettel']
#
# experimental_list = initial_list[:]
# experimental_deque = collections.deque(initial_list)


def appending_list():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in list_for_experiments:
        experimental_list.append(i)
    return


def appending_deque():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in list_for_experiments:
        experimental_deque.append(i)
    return

def popping_list():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in range(len(experimental_list)):
       element = experimental_list.pop()
    return

def popping_deque():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in range(len(experimental_deque)):
        element = experimental_deque.pop()
    return

def extending_list():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in range(len(list_for_experiments)):
        experimental_list.extend(list_for_experiments)
    return

def extending_deque():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in range(len(list_for_experiments)):
        experimental_deque.extend(list_for_experiments)
    return

def appending_left_list():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in list_for_experiments:
        experimental_list.insert(0, i)
    return

def appending_left_deque():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in list_for_experiments:
        experimental_deque.appendleft(i)
    return

def pop_left_list():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in range(len(experimental_list)-1):
        experimental_list.pop(0)
    return

def pop_left_deque():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in range(len(experimental_deque)-1):
        experimental_deque.popleft()
    return

def extending_left_list():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    list_for_copy = list_for_experiments.copy()
    for i in range(len(list_for_experiments)-1):
        list_for_experiments.extend(list_for_copy)
    list_for_experiments.extend(experimental_list)
    return

def extending_left_deque():
    initial_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tentn',
                    'eleventh', 'twelveth']
    list_for_experiments = ['Aytron Senna', 'Lewis Hamilton', 'Michael Schumacher', 'Stirling Moss', 'Jim Clark',
                            'Sebastian Vettel']

    experimental_list = initial_list[:]
    experimental_deque = collections.deque(initial_list)

    for i in range(len(list_for_experiments)):
        experimental_deque.extendleft(list_for_experiments)
    return


appending_list_test = timeit.timeit('appending_list()', 'from __main__ import appending_list')
appending_deque_test = timeit.timeit('appending_deque()', 'from __main__ import appending_deque')
popping_list_test = timeit.timeit('popping_list()', 'from __main__ import popping_list')
popping_deque_test = timeit.timeit('popping_deque()', 'from __main__ import popping_deque')
extending_list_test = timeit.timeit('extending_list()', 'from __main__ import extending_list')
extending_deque_test = timeit.timeit('extending_deque()', 'from __main__ import extending_deque')
appending_left_list_test = timeit.timeit('appending_left_list()', 'from __main__ import appending_left_list')
appending_left_deque_test = timeit.timeit('appending_left_deque()', 'from __main__ import appending_left_deque')
pop_left_list_test = timeit.timeit('pop_left_list()', 'from __main__ import pop_left_list')
pop_left_deque_test = timeit.timeit('pop_left_deque()', 'from __main__ import pop_left_deque')
extending_left_list_test = timeit.timeit('extending_left_list()', 'from __main__ import extending_left_list')
extending_left_deque_test = timeit.timeit('extending_left_deque()', 'from __main__ import extending_left_deque')

# добавление в конец немного быстрее у обычного списка
print(appending_list_test)  # 2.2564998000161722
print(appending_deque_test)  # 2.169522299984237

# удаление последнего элемента значительно быстрее у дека
print(popping_list_test)  # 3.5622552999993786
print(popping_deque_test)  # 2.9207107000111137

# добавление другого списка в конец быстрее у обычного списка
print(extending_list_test)  # 2.7807010999822523
print(extending_deque_test)  # 3.329635700007202

# добавление слева быстрее у дека
print(appending_left_list_test)  # 2.7869986000005156
print(appending_left_deque_test)  # 2.162802999984706

# удаление слева быстрее у дека
print(pop_left_list_test)  # 3.83917350001866
print(pop_left_deque_test)  # 2.8596676000161096

# включение другого списка слева быстрее у обычного списка, или я что-то не так сделал -_-
print(extending_left_list_test)  # 3.345781700016232
print(extending_left_deque_test)  # 3.618577799992636

