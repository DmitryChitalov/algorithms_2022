"""
Задание 2.
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(100, 1000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
print('Отметка число', num_100)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_1000)",
#         setup='from __main__ import recursive_reverse, num_1000',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_10000)",
#         setup='from __main__ import recursive_reverse, num_10000',
#         number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            print('отметка словарь', cache, ' текущий аргумент', args,
                  'значение', cache[args]) # оутпут ниже
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


# func(586) -> "6"func(58) -> func(58) -> "8"func(5) -> func(5)
#                    |                      |             |
#                   685                     85            5
# оутпут со словаря
# отметка словарь {(0,): ''} аргумент (0,) значение
# отметка словарь {(0,): '', (6,): '6'} аргумент (6,) значение 6
# отметка словарь {(0,): '', (6,): '6', (67,): '76'} аргумент (67,) значение 76
# отметка словарь {(0,): '', (6,): '6', (67,): '76', (673,): '376'}
# аргумент (673,) значение 376
# для дальнейших чисел комбинации тоже заносятся в словарь
# при выполнении фукнции числа заносятся в словарь, откуда при 10000 кратном исполнении
# значения и черпаются, ускоряя работу
# При этом большого смысла в нем нет, т к комбинации чисел могут быть различные,
# хотя попасть в случайную комбинацию конечно можно



print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_1000)',
#         setup='from __main__ import recursive_reverse_mem, num_1000',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_10000)',
#         setup='from __main__ import recursive_reverse_mem, num_10000',
#         number=10000))
