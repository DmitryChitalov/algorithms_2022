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
from cProfile import run


def recursive_reverse(number):
    recursive_reverse.cnt += 1
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
recursive_reverse.cnt = 0

print(num_100, num_1000, num_10000)
recursive_reverse(123456789)
count_not_opt = recursive_reverse.cnt

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
    recursive_reverse_mem.cnt += 1
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


recursive_reverse_mem.cnt = 0

recursive_reverse_mem(123456789)
count_opt = recursive_reverse_mem.cnt

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

run('recursive_reverse(num_10000)')
run('recursive_reverse_mem(num_10000)')

print(f'Количество операций recursive_reverse 123456789 {count_not_opt}')
print(f'Количество операций recursive_reverse_mem для числа 123456789 {count_opt}')

'''
как можно видеть из результатов профилирования , при мемоизации в отчет модуля timeit и cProfileпопадает только 
последнее выполнение фунции и значение берется из кэша, поэтому отображатеся такое быстрое время. Если мы введем 
счетчики выполения функций для числа 123456789 , то каждая функция будет вызвана по 10 раз, т.е. количество операций 
одинаково. Из этого делаем , что для данной задачи мемоизация не нужна.
'''
