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
        return str(number % 10)  # здесь появляется лишний 0 в конце
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

##############################################################################
"""
Ответ: Нет, в данном случае мемоизация не нужна
Объяснение: В данном случае рекурсия является последовательной (не как в
примере с последовательностью Фибоначчи, когда на каждом шаге рекурсивная
функция вызывалась внутри себя дважды, за счет чего образовывалось дерево
вычислений значений функции от различных аргументов, и по мере прохождения
по веткам этого дерева с помощью мемоизации удавалось кэшировать значения
фукнции для различных аргументов и использовать их при сворачивании последующих
веток) и на каждом последущем шаге функция рекурсивно вызывает себя с аргументом,
отличным от предыдущих вызовов (как минимум они отличаются по количеству цифр в
составе числа-аргумента). Поэтому нет смысла кэшировать значения функции для
различных аргументов, программе все равно не доведется ими воспользоваться
при сворачивании рекурсии.

Пример: 12345

Последовательность вызовов рекурсии:
rec_f(12345) -> rec_f(1234) -> rec_f(123) -> rec_f(12) -> rec_f(1) -> rec_f(0)

Последовательность сворачивания рекурсии (она же последовательность
кешируемых значений):
rec_f(12345) <- rec_f(1234) <- rec_f(123) <- rec_f(12) <- rec_f(1) <- rec_f(0)

Ниже представлен пример к объяснению.
"""

# Мемоизация с добавленной функцией print
def memoize_print(f):
    cache = {}

    def decorate(args):

        if args in cache:
            pass
        else:
            cache[args] = f(args)
        print(cache)
        return cache[args]

    return decorate

@memoize_print
def rec_f(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{rec_f(number // 10)}'

# Пример
num_test = 12345
print('-------------------------')
print(num_test)
print(rec_f(num_test))