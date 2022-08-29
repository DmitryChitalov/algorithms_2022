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

# -------------------------Рекурсия до 'оптимизации'--------------------------

def recursive_reverse(number):
    if number == 0:
        return ''
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

# ------------------------Рекурсия после 'оптимизации'------------------------
@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
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

"""
Не оптимизированная функция recursive_reverse
0.30187026899999997
0.351715053
0.5999413180000001

Оптимизированная функция recursive_reverse_mem
0.061801192000000116
0.062389217
0.06353870299999986

На первый взгля оптимизация помогла. Но так ли это?
"""

"""
976566 - исходное число

При первом вызове из number наполняем кэш.

9
79
679
5679
65679
665679

При втором и остальных
берем готовое перевернутое число уже из кэша

665679
665679

Поэтому такие цифры. Мемоизаци пригодится, если после наполнения кэша,
потребуются новые вызовы функции. 

Для однократного вызова ф-ции она не нужна (в отличие с задачей Фибоначчи)
Но если в рамках кода нам придется делать много вызовов. Тогда она может
помочь, если будут встречаться повторы чисел
"""