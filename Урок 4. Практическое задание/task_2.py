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


def num_100():
    return randint(10000, 1000000)

def num_1000():
    return randint(1000000, 10000000)


def num_10000():
    return randint(100000000, 10000000000000)


count=10000
print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100())",
        setup='from __main__ import recursive_reverse, num_100',
        number=count))
print(
    timeit(
        "recursive_reverse(num_1000())",
        setup='from __main__ import recursive_reverse, num_1000',
        number=count))
print(
    timeit(
        "recursive_reverse(num_10000())",
        setup='from __main__ import recursive_reverse, num_10000',
        number=count))


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
        'recursive_reverse_mem(num_100())',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=count))
print(
    timeit(
        'recursive_reverse_mem(num_1000())',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=count))
print(
    timeit(
        'recursive_reverse_mem(num_10000())',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=count))

"""с
На первый взгляд, когда запускаешь программу, мемоизация дает приличный выигрыш.
Логика подсказывает, что не должна: мемоизация будет работать, если встречаются одинаковые данные. 
В процессе переворота одного числа мемоизация не раотает: одинаковые подстроки там не встречаются,
они по крайней мере по длине разные.
После некоторого количества размышлений до меня дошло. Тест так устроен, что программа переворачивает 
много раз одно и то же число.
Тогда, конечно, мемоизация работает.
А вот если изменить код так, чтобы переворачивались разные числа (и я так код изменила),
то выигрыш за счет мемоизации обернется проигрышем по времени (небольшим), и я даже боюсь сказать,
какого размера кэшем.

...А еще программа неправильно работает.
Она лишний ноль в конце добавляет. Вот, смотрите:
"""
print(recursive_reverse(135))
