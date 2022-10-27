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


"""
В задание с GH в начале есть опечатка в коде: 
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}' - эта часть возвращает лишний ноль
    
Вообще работает значительно быстрее второй вариант, если число огромное, то будет намного быстрее.
Результат выполнения для number=100000000, считал только для n_10000:
Не оптимизированная функция recursive_reverse
1.5265981
1.7239976000000001
335.1687313
Оптимизированная функция recursive_reverse_mem
0.12951809999998432
0.1279696999999942
13.88889690000002

Если выполнять функцию не большое число раз, смысла не имеет хранить результат, проигрывая немного в скорости, мы сильно выигрываем по памяти.
"""


from timeit import timeit
from random import randint


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
        number=1000000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=1000000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=1000000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            print(f'1{cache[args]}')
            return cache[args]
        else:
            cache[args] = f(*args)
            print(f'2{cache[args]}')
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
        number=1000000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=1000000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=1000000))
