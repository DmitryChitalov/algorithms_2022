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
        return str(number % 10)  # работает не совсем корректно, в конце добавляется ноль
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)


print('Не оптимизированная функция recursive_reverse')
print(timeit("recursive_reverse(num_100)", setup='from __main__ import recursive_reverse, num_100', number=10000))
print(timeit("recursive_reverse(num_1000)", setup='from __main__ import recursive_reverse, num_1000', number=10000))
print(timeit("recursive_reverse(num_10000)", setup='from __main__ import recursive_reverse, num_10000', number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            print(cache)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(timeit('recursive_reverse_mem(num_100)', setup='from __main__ import recursive_reverse_mem, num_100',
             number=1))
print(timeit('recursive_reverse_mem(num_1000)', setup='from __main__ import recursive_reverse_mem, num_1000',
             number=10000))
print(timeit('recursive_reverse_mem(num_10000)', setup='from __main__ import recursive_reverse_mem, num_10000',
             number=10000))

"""
На первый взгляд может сложиться мнение, что мемоизация позволила оптимизировать код, однако это  
приведет  к ошибке второго рода.
Это связано с реализованным кодом recursive_reverse_mem, который не позволяет воспользоваться преимуществом 
заполнения словаря (cash) данными, полученными на предыдущей операции, т.к. последующее значение больше на единицу.
Получается словарь заполняется, но никак не участвует в ускорении процесса.
Рассмотрим пример:
пусть num_100 = 12345, тогда при вызове recursive_reverse_mem срабатывает декоратор и получаем следующий результат:
rec_rev_mem(12345) -> rec_rev_mem(1234) -> rec_rev_mem(123) -> rec_rev_mem(12) -> rec_rev_mem(1) -> rec_rev_mem(0).
Далее происходит реверс рекурсии (поучения значений из кэша): rec_rev_mem(0) -> ...-> rec_rev_mem(12345).
В cache записываются данные в виде: {(0,): '', (1,): '1', (12,): '21', (123,): '321', (1234,): '4321', 
(12345,): '54321', (123456,): '654321', (1234567,): '7654321'}. 
Получить можно, дописав в def memoize(f):
...
cache[args] = f(*args)
print(cache)
"""