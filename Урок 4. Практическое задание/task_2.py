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
    return f'{str(number % 10)}{recursive_reverse(number // 10)}' if number != 0 else ''


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

# print(num_100, recursive_reverse(num_100))
print('Не оптимизированная функция recursive_reverse')
print(timeit("recursive_reverse(num_100)", setup='from __main__ import recursive_reverse, num_100', number=1))
print(timeit("recursive_reverse(num_1000)", setup='from __main__ import recursive_reverse, num_1000', number=1))
print(timeit("recursive_reverse(num_10000)", setup='from __main__ import recursive_reverse, num_10000', number=1))

num_101 = randint(10000, 1000000)
num_1001 = randint(1000000, 10000000)
num_10001 = randint(100000000, 10000000000000)


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            # print(cache[args])
            return cache[args]

        else:
            cache[args] = f(*args)
            # print(cache[args])
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}' if number != 0 else ''


# print(num_101, recursive_reverse_mem(num_101))
print('Оптимизированная функция recursive_reverse_mem')
print(timeit('recursive_reverse_mem(num_101)', setup='from __main__ import recursive_reverse_mem, num_101', number=1))
print(timeit('recursive_reverse_mem(num_1001)', setup='from __main__ import recursive_reverse_mem, num_1001', number=1))
print(timeit('recursive_reverse_mem(num_10001)', setup='from __main__ import recursive_reverse_mem, num_10001', number=1))

'''возможно числа кэшируются и второй раз не вычисляются (нет)(не совсем)'''
'''возможно мемоизируются итерации timeit. 
Да, фукнция _mem выполняется только 1 раз, далее значение берется из cache[args].
Функции выполняются одинаково по времени.'''
