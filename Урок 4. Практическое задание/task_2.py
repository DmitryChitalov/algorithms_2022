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
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    f'{num_100} -> {recursive_reverse(num_100)}\n{num_1000} -> {recursive_reverse(num_1000)}\n{num_10000} -> {recursive_reverse(num_10000)}')
print(
    timeit(
        "recursive_reverse(randint(10000, 1000000))",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000,
        globals=globals()))
print(
    timeit(
        "recursive_reverse(randint(1000000, 10000000))",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000,
        globals=globals()))
print(
    timeit(
        "recursive_reverse(randint(100000000, 10000000000000))",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000,
        globals=globals()))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            #print(f'Функция с такими аргументами {args} уже выхывалась б результат ее выполнения -  {cache[args]} ')
            return cache[args]
        else:
            cache[args] = f(*args)
           # print(f'Аргументы {args} и результат выполнения - {cache[args]} добавлены в кеш.')
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('--------------------------------')
print('Оптимизированная функция recursive_reverse_mem')
print(
    f'{num_100} -> {recursive_reverse_mem(num_100)}\n{num_1000} -> {recursive_reverse_mem(num_1000)}\n{num_10000} -> {recursive_reverse_mem(num_10000)}')
print(
    timeit(
        'recursive_reverse_mem(randint(10000, 1000000))',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000,
        globals=globals()))
print(
    timeit(
        'recursive_reverse_mem(randint(1000000, 10000000))',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000,
        globals=globals()))
print(
    timeit(
        'recursive_reverse_mem(randint(100000000, 10000000000000))',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000,
        globals=globals()))

# начнем с того что не оптимизированная она работает неправильно - а именно добавляет лишний 0 в конце. Исправил
# удалением строки return str(number % 10)

# Мемоизация по сути не используется, тк значения занесенные в кэш при
# вычислении самой функции не используются. А При повторном запуске функции выдается сохраненный в кэше результат
# выполнения функции с этим же самым аргументом.
# Для чистоты эксперимента сделал, что бы проверка на время выполнения
# каждый раз велась с рандомным аргументом.
# (при этом вывод оставил одинаковым, что бы видно было что функции работают правильно)
# В результате время выполнения "оптимизированной " функции примерно равно
# времени выполнения не оптимизированной
