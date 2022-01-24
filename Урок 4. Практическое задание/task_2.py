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

# ==============================================================================
# === Ответ ====================================================================
# ==============================================================================
# При вызове мемоизации и первом вызове функции реверса числа 
# мы запоминаем реверс для КАЖДОГО отрезка числа
# Например для числа 123456 в кеше будут следующие числа:
# 1) cash['123456'] = '654321'
# 2) cash['23456'] = '65432'
# 3) cash['3456'] = '6543'
# 4) cash['456'] = '654'
# 5) cash['56'] = '65'
# 6) cash['6'] = '6'
# При первом вызове функции мемоизация наоборот увеличивает время выполения, 
# так как необходимо время на сохрание промежуточных результатов.
#
# Однако если у нас попадаются входные данные, у которых хвостовая часть числа
# (например после вышеуказанного числа мы ввели число 999123456) 
# или же всё число равно существующему ключу кэша (число 123456), тогда будет 
# ускорение работы, так как нет необходимости переворачивать число, 
# а достаточно взять результат из кэша. 
# Однако если у нас практически все числа случайные и 
# запросов не очень много, тогда не смысла в мемоизации, так как шанс что 
# попадется одинаковая хвостовая часть не большой
# В ниже указанный замерах число использовалось одно на все проходы, поэтому реально 
# реверс выполнялся только для первохо прохода, а в последующих вызовах 
# результат брался из кэша, поэтому мы видим такие малые цифры реверса при мемоизации
# ==============================================================================

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


def reverse(number: int) -> str:
    def recursion_reverse(number):
        if number < 10:
            return [number]

        number, remain = divmod(number, 10)
        return [remain] + recursion_reverse(number)
    
    result_list = recursion_reverse(number)
    result_list_str = [str(num) for num in result_list]
    return ''.join(result_list_str)

