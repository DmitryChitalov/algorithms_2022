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

from random import randint
from collections import deque
from timeit import timeit


def list_append(from_list: list, to_list: list):
    return [to_list.append(el) for el in from_list]


def deque_append(from_list: list, to_deque: deque):
    return [to_deque.append(el) for el in from_list]


def list_extend(base: list, extension: list):
    return base.extend(extension)


def deque_extend(base: deque, extension: list):
    return base.extend(extension)


def list_pop(user_list: list, quantity: int):
    for _ in range(quantity):
        user_list.pop(len(user_list) - 1)
    return user_list


def deque_pop(user_deque: deque, quantity: int):
    for _ in range(quantity):
        user_deque.pop()
    return user_deque


def list_appendleft(from_list: list, to_list: list):
    to_list.reverse()
    [to_list.append(el) for el in from_list]
    to_list.reverse()


def deque_appendleft(from_list: list, to_deque: deque):
    return [to_deque.appendleft(el) for el in from_list]


def list_popleft(from_list: list, quantity: int):
    return [from_list.pop(0) for _ in range(quantity)]


def deque_popleft(from_deque: deque, quantity: int):
    return [from_deque.popleft() for _ in range(quantity)]


def list_extendleft(from_list: list, to_list: list):
    to_list.reverse()
    [to_list.append(el) for el in from_list]
    to_list.reverse()


def deque_extendleft(from_list: list,  to_deque: deque):
    return to_deque.extendleft(from_list)


def list_get(from_list: list):
    for i in range(len(from_list)):
        return from_list[i]


def deque_get(from_deque: deque):
    for i in range(len(from_deque)):
        return from_deque[i]


print('\nВведите число от 1 до 200 для работы программы: ', end='')
number = int(input())
main_list = [randint(1, number) for _ in range(number)]
print(f'Создан список main_list из {number} случайных целых чисел от 1 до {number}.\n')
base_list = []
base_deque = deque()
extension_deque = deque()

# 1. list_append vs. deque_append
time_1 = timeit(stmt='list_append(main_list, base_list)',
                setup='from __main__ import list_append',
                number=number,
                globals=globals())
time_2 = timeit(stmt='deque_append(main_list, base_deque)',
                setup='from __main__ import deque_append',
                number=number,
                globals=globals())
print(f'1. {number} элемент(ов) из списка main_list {number} раз(а) добавлены (по одному) в список base_list.\n'
      f'   {number} элемент(ов) из списка main_list {number} раз(а) добавлены (по одному) в дэк base_deque.\n'
      f'   Функция list_append: {time_1:.7f} сек, функция deque_append: {time_2:.7f} сек, '
      f'преимущество deque по скорости {time_1 / time_2:.1f} раз(а).\n')

extension_list = [randint(1, number) for _ in range(number)]

# 2. list_extend vs. deque_extend
time_1 = timeit(stmt='list_extend(base_list, extension_list)',
                setup='from __main__ import list_extend',
                number=number,
                globals=globals())
time_2 = timeit(stmt='deque_extend(base_deque, extension_list)',
                setup='from __main__ import deque_extend',
                number=number,
                globals=globals())
print(f'2. Сгенерирован случайный список extension_list длиной {len(extension_list)} элемента(ов).\n'
      f'   В список base_list {number} раз(а) добавлены (по одному) элементы из списка extension_list'
      f'с помощью метода list.extend.\n'
      f'   В дэк base_deque {number} раз(а) добавлены (по одному) элементы из списка extension_list'
      f' с помощью метода deque.extend.\n'
      f'   Функция list_extend: {time_1:.7f} сек, функция deque_extend: {time_2:.7f} сек, '
      f'преимущество deque по скорости {time_1 / time_2:.1f} раз(а).\n')

to_pop = int((len(base_list) / (2 * number)))

# 3. list_pop vs. deque_pop
time_1 = timeit(stmt='list_pop(base_list, to_pop)',
                setup='from __main__ import list_pop',
                number=number,
                globals=globals())
time_2 = timeit(stmt='deque_pop(base_deque, to_pop)',
                setup='from __main__ import deque_pop',
                number=number,
                globals=globals())
print(f'3. {to_pop} элемента(ов) {number} раз удалены из списка base_list с помощью list.pop.\n'
      f'   {to_pop} элемента(ов) {number} раз удалены из дэка base_deque с помощью deque.pop.\n'
      f'   Функция list_pop: {time_1:.7f} сек, функция deque_pop: {time_2:.7f} сек, '
      f'преимущество deque по скорости {time_1 / time_2:.1f} раз(а).\n')

# 4. list_appendleft vs. deque_appenleft
time_1 = timeit(stmt='list_appendleft(extension_list, base_list)',
                setup='from __main__ import list_appendleft',
                number=number,
                globals=globals())
time_2 = timeit(stmt='deque_appendleft(extension_list, base_deque)',
                setup='from __main__ import deque_appendleft',
                number=number,
                globals=globals())
print(f'4. Элементы из extension_list длиной {number} элемента(ов) добавлены (по одному) слева в лист base_list.\n'
      f'   Элементы из extension_list длиной {number} элемента(ов) добавлены (по одному) слева в дэк base_deque.\n'
      f'   Функция list_appendleft: {time_1:.7f} сек, функция deque_appendleft: {time_2:.7f} сек, '
      f'преимущество deque по скорости {time_1 / time_2:.1f} раз(а).\n')

# 5. list_popleft vs. deque_popleft
time_1 = timeit(stmt='list_popleft(base_list, to_pop)',
                setup='from __main__ import list_popleft',
                number=number,
                globals=globals())
time_2 = timeit(stmt='deque_popleft(base_deque, to_pop)',
                setup='from __main__ import deque_popleft',
                number=number,
                globals=globals())
print(f'5. {to_pop} элемента(ов) {number} раз удалены слева из списка base_list.\n'
      f'   {to_pop} элемента(ов) {number} раз удалены слева из дэка base_deque.\n'
      f'   Функция list_popleft: {time_1:.7f} сек, функция deque_appendleft: {time_2:.7f} сек, '
      f'преимущество deque по скорости {time_1 / time_2:.1f} раз(а).\n')

# 6. list_extendleft vs. deque_extendleft
time_1 = timeit(stmt='list_extendleft(extension_list, base_list)',
                setup='from __main__ import list_extendleft',
                number=number,
                globals=globals())
time_2 = timeit(stmt='deque_extendleft(extension_list, base_deque)',
                setup='from __main__ import deque_extendleft',
                number=number,
                globals=globals())
print(f'6. Список extension_list длиной {len(extension_list)} элемента(ов) {number} раз(а) добавлен слева '
      f'в список base_list (функциональный аналог deque.extendleft).\n'
      f'   Список extension_list длиной {len(extension_list)} элемента(ов) {number} раз(а) добавлен слева '
      f'в дэк base_deque c помощью deque_extendleft.\n'
      f'   Функция list_extendleft: {time_1:.7f} сек, функция deque_extendleft: {time_2:.7f} сек, '
      f'преимущество deque по скорости {time_1 / time_2:.1f} раз(а).\n')


# 7. list_get vs. deque_get
time_1 = timeit(stmt='list_get(base_list)',
                setup='from __main__ import list_get',
                number=number,
                globals=globals())
time_2 = timeit(stmt='deque_get(base_deque)',
                setup='from __main__ import deque_get',
                number=number,
                globals=globals())

print(f'7. Получение {len(base_list)} элементов из списка base_list {number} раз(а).\n'
      f'   Получение {len(base_deque)} элементов из дэка base_deque {number} раз(а).\n'
      f'   Функция list_get: {time_1:.7f} сек, функция deque_get: {time_2:.7f} сек, '
      f'преимущество list по скорости {time_2 / time_1:.1f} раз(а).\n')

print('ВЫВОД. Получение элемента по индексу для списка работает быстрее.'
      ' В остальных случаях быстрее deque. Особенно там, где нужно что-то добавить или удалить слева.')
