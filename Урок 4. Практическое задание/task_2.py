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


# Очевидно что меморизированная функция выполняется за меньшее количество времени, так как декоратор хранит в себе
# выполненные варианты параметров функции с результатом. Однако, замеры выполняются 10000 раз с одним и тем же числом.
# Для чистоты эксперимента число должно генерироваться случайно каждый раз
# Рекурсивная функция на каждом уровне отделяет последнюю цифру и ставит её в конец и передаёт в следующий уровень
# строку без последнего числа
# Меморизация здесь тем эффективнее чем больше повторяющихся последовательностей во вводных данных. Так как диапазон
# генерации случайных чисел ограничен, то количество последовательностей очень ограничено и меморизация работает
# эффективно. При более широком диапазоне или меньшем количестве обращений к функции меморизация будет менее эффективна
# Также при больших числах количество уникальных последовательностей будет больше
# Количество уникальных чисел в диапазоне от n1 до n2 равно n2 - n1. Меморизация для диапазона 100000000, 10000000000000
# может хранить в памяти до 9999900000000 комбинаций
#
#Новые замеры:

a1 = lambda : recursive_reverse(randint(10000, 1000000))
a2 = lambda : recursive_reverse(randint(1000000, 10000000))
a3 = lambda : recursive_reverse(randint(100000000, 10000000000000))

b1 = lambda : recursive_reverse_mem(randint(10000, 1000000))
b2 = lambda : recursive_reverse_mem(randint(1000000, 10000000))
b3 = lambda : recursive_reverse_mem(randint(100000000, 10000000000000))

print('\nПравильные замеры')
print('функция recursive_reverse')
print(
    timeit(a1, number=10000))
print(
    timeit(a2, number=10000))
print(
    timeit(a3, number=10000))
print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(b1, number=10000))
print(
    timeit(b2, number=10000))
print(
    timeit(b3, number=10000))

# Согласно случайным замерам меморизация неэффективна, слишком мало повторяющихся последовательностей. На самом
# маленьком промежутке иногда работает немного быстрее, но это не стоит затрат памяти.