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
        return ''
        '''
        здесь была допущена ошибка в алгоритме, 
        так как функция возврещая перевёрнутое число и в конце добавляла лишний ноль,
        '''
        # return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


const_num = 756747456
num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print(num_100, recursive_reverse(num_100))


print(
    timeit(
        "recursive_reverse(const_num)",
        setup='from __main__ import recursive_reverse, const_num',
        number=10000))


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
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


'''
Мемоизация для этой функции ускоряет её работу только в том случае,
если эта функция будет вызвана несколько раз с одним и тем же аргументом, 
поэтому при использовании функции timeit время мемоизированной функции будет меньше,
так как с каждым новым запуском функция будет брать готовое значения их кэша.
Поэтому мемоизация для этой функции не нужна
'''
# print(const_num, recursive_reverse_mem(const_num))
#
# print(const_num, recursive_reverse_mem(const_num))

print(
    timeit(
        'recursive_reverse_mem(const_num)',
        setup='from __main__ import recursive_reverse_mem, const_num',
        number=10000))

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
