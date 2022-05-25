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
from cProfile import run


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
            print(cache[args])
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

my_num = 123456789012345678901
print(recursive_reverse_mem(my_num))
run('recursive_reverse(num_10000)')
run('recursive_reverse_mem(num_10000)')


''''
Мне кажеться, что мемоизация в данном случие не несет абсолютно никакого смысла. Фундаментально, мнемоизация позволяет
избежать ненужные ПОВТОРЯЮЩИЕСЯ вычисления (ну, или дублирующиеся аргументы), сохраняя первычный результат в кеше, 
и вместо вычисления  n-раз одного и того же, позволяет выкгружать вычесленный результат из кеша. Слегка модифицировав 
приведенный в задании код, можно удостовериться, что в кеш сохраняеться "лесенка" (смотреть консольный вывод)  из 
уникальных неповторяющихся чисел. Т.е. сома идея мемоизации здесь работать не может! Теперь про выйгрышь в скорости: 
он достигаеться за счет того, что декоратор мемоизации вызываеться однократно, а без декоратора, идет куча вызовов, 
что видно  из статистики cProfile. Сами операции, проходят быстро, а вот на дополнительный вызов функции время лишнее 
и затрацивается (ну, по крайней мере я вижу для себя это так). 
'''

