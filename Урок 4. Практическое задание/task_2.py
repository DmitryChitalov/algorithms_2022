"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение мемоизацией
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!

П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    # А это так планировалось, что мы получаем лишний ноль на конце в обеих функциях (77601 -> 106770)?
    if number == 0:
        return str(number % 10)
    # if number < 10:
    #     return str(number)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    # if number < 10:
    #     return str(number)
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))


'''
Результаты получились следующие:

Не оптимизированная функция recursive_reverse
0.02380366299985326
0.02683471499949519
0.04841034999844851
Оптимизированная функция recursive_reverse_mem
0.0020576010010699974
0.0020630430008168332
0.0022513959993375465

На первый взгляд оптимизированная отрабатывает лучше, но по описанию задания, кажется, что ответ "Нужна мемоизация" неправильный.

В целом чем меньше вариантов входных аргументов и больше вызовов, тем более нужна мемоизация. То есть если на вход мы можем получить одно из 100 чисел, а вызовов больше 100, то очевидно, что мемоизация пригодится.

Но сами по себе функции выводят результат только для одного числа (много вызовов засчет замеров) и в таком случае мемоизация не особо нужна

'''
