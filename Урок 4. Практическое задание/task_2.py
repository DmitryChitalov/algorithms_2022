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
    if number == 0:
        return str(number % 10)
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
результаты изначальных замеров:
Не оптимизированная функция recursive_reverse
0.04337789997225627
0.03302979998989031
0.0707346000126563
Оптимизированная функция recursive_reverse_mem
0.002084899984765798
0.0022438999731093645
0.0022360000293701887

А теперь поговорим о том, имеет ли смысл оптимизация.
С одной стороны ,конечно, имеет, ведь казалось бы функция выполняется быстрее,
но с другой... Поговорим подробнее.
Оптимизация функции в представленном примере заключается в том, что мы 
сохраняем результаты в кеш и при повторном вызове получаем более высокую 
скорость работы за счет кеша, но при первичном вызове мы получим одинаковые 
результаты как при использовании оптимизации, так и без нее. Вызвано такое 
поведение тем, что в обоих вариантах значение будет вычисляться с нуля.
Исходя из этой логики, оптимизация будет нужна только в том случае, если в 
задачи программы будет входить постоянное использование подобных вычислений.
Вывод:
Решение применять мемоизацию или нет, зависит от того, какие задачи решает 
программа.
"""
