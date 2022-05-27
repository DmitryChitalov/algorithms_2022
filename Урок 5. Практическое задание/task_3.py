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

lst_list = []
lst_deque = deque([])


def diff_time(func_1, func_2):
    """
    Функция определения разности скорости выполнения в процентах.
    """
    if func_1 > func_2:
        return f'deque быстрее list на {100 - (100 * func_2 / func_1)} процентов(а)'
    elif func_1 < func_2:
        return f'deque медленнее list на {(100 * func_2 / func_1) - 100} процентов(а)'
    else:
        return f'deque и list равны по времени'


# 1)
# Сравнение операций append, pop, extend


def func_append(test_list):
    """Функция заполняет список от 0 до 100"""
    for i in range(10001):
        test_list.append(i)
    return test_list


time_list_append = timeit(f'func_append(lst_list)', globals=globals(), number=1)
time_deque_append = timeit(f'func_append(lst_deque)', globals=globals(), number=1)
print(f'\nappend для list и deque'
      f'\nlist.append: {time_list_append} сек. --- deque.append: {time_deque_append} сек.\n'
      f'{diff_time(time_list_append, time_deque_append)}')


def func_pop(test_list):
    """Функция удаляет последние 100 элементов из списка"""
    for _ in range(1000):
        test_list.pop()
    return test_list


time_list_pop = timeit(f'func_pop(lst_list)', globals=globals(), number=1)
time_deque_pop = timeit(f'func_pop(lst_deque)', globals=globals(), number=1)
print(f'\npop для list и deque'
      f'\nlist.pop: {time_list_pop} сек. --- deque.pop: {time_deque_pop} сек.\n'
      f'{diff_time(time_list_pop, time_deque_pop)}')


def func_extend(test_list):
    """Добавление списка extension_list к принимаемому функцией списку"""
    extension_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    test_list.extend(extension_list)
    return test_list


time_list_extend = timeit(f'func_extend(lst_list)', globals=globals(), number=1)
time_deque_extend = timeit(f'func_extend(lst_deque)', globals=globals(), number=1)
print(f'\nextend для list и deque'
      f'\nlist.extend: {time_list_extend} сек. --- deque.extend: {time_deque_extend} сек.\n'
      f'{diff_time(time_list_extend, time_deque_extend)}')


######################################################################################################################
# Замеры чаще всегда показывают, что deque при использовании append быстрее чем list.
# При использовании pop, extend замеры показываю время то больше чем list то меньше.
######################################################################################################################


# 2)
# Сравнение операций appendleft, popleft, extendleft


def func_insert(test_list):
    """Добавление элементов слева от списка list"""
    for el in (['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']):
        test_list.insert(0, el)
    return test_list


def func_appendleft(test_list):
    """Добавление элементов слева от списка deque"""
    for el in (['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']):
        test_list.appendleft(el)
    return test_list


time_insert = timeit(f'func_insert(lst_list)', globals=globals(), number=1)
time_appendleft = timeit(f'func_appendleft(lst_deque)', globals=globals(), number=1)
print(f'\nlist.insert: {time_insert} сек. --- deque.appendleft: {time_appendleft} сек.\n'
      f'{diff_time(time_insert, time_appendleft)}')


def func_pop_first(test_list):
    """Удаление элемента слева от списка list"""
    for _ in range(100):
        test_list.pop(0)
    return test_list


def func_popleft(test_list):
    """Удаление элементов слева от списка deque"""
    for _ in range(100):
        test_list.popleft()
    return test_list


time_pop_first = timeit(f'func_pop_first(lst_list)', globals=globals(), number=1)
time_popleft = timeit(f'func_popleft(lst_deque)', globals=globals(), number=1)
print(f'\nlist.pop: {time_pop_first} сек. --- deque.popleft: {time_popleft} сек.\n'
      f'{diff_time(time_pop_first, time_popleft)}')


def func_insert_left(test_list):
    """Добавление списка слева от списка list"""
    for el in (['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']):
        test_list.insert(0, el)
    return test_list


# Если правильно понял, то для 'extendleft' аналогом в списке будет через цикл добавить элементы.

def func_extendleft(test_list):
    """Добавление списка слева от списка deque"""
    test_list.extendleft(
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
    return test_list


time_insert_left = timeit(f'func_insert_left(lst_list)', globals=globals(), number=1)
time_extendleft = timeit(f'func_extendleft(lst_deque)', globals=globals(), number=1)
print(f'\nlist.insert: {time_insert_left} сек. --- deque.extendleft: {time_extendleft} сек.\n'
      f'{diff_time(time_insert_left, time_extendleft)}')


######################################################################################################################
# Замеры показывают, что deque при использовании appendleft, popleft, extendleft по сравнению с
# list с соответствующими командами быстрее.
# Так же заметил, что если списки list и deque не большие, скорость может быть больше как у deque так и у list.
######################################################################################################################

# 3)
# Сравнение получения элемента из списка и дека


def getting_element(test_list):
    for el in range(0, len(test_list), 3):
        n_lst = test_list[el]
    return n_lst


time_getting_el_list = timeit(f'getting_element(lst_list)', globals=globals(), number=1)
time_getting_el_deque = timeit(f'getting_element(lst_deque)', globals=globals(), number=1)
print(f'\nlist: {time_getting_el_list} сек. --- deque: {time_getting_el_deque} сек.\n'
      f'{diff_time(time_getting_el_list, time_getting_el_deque)}')

######################################################################################################################
# Замеры показывают, что получение элемента из deque медленнее чем из list.
######################################################################################################################
