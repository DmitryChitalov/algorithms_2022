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

from cProfile import run
from random import randint
from timeit import timeit


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
    if not cache:
        print("cache", cache)  # {} - пустое напечаталось 1 раз в начале вывода работы программы.

    # print("cache", cache)  # Далее на печать выводилось заполненное.

    def decorate(*args):

        if args in cache:
            # print("cache[args]", cache[args])  # При смене числа всегда пустой.
            # print("cache", cache)  # добавлялись новые значения при смене чисел, подаваемых на вход.
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


def main():
    recursive_reverse(
        12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890)


run('main()')


def main_1():
    recursive_reverse_mem(
        12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890)


run('main_1()')

# В данном случае мемоизация нужна для сокращения времени исполнения алгоритма
# при его повторении для одного числа.
# Выросло общее количество кода.
# Помимо этого выросло количество вызовов функций и кумулятивное время за счет вызова декоратора.
# Мемоизация сохраняет предыдущие вычисления, при повторе вычислений
# - возвращает значение, чтобы второй раз не считать.
# По идее, при делении числа все время на 10, одинаковых результатов быть не может.
# Целая чсть всегда разная. Извлекать из кеша будет нечего, если нет повторений вызовов функции.
# Во втором случае время сокращается при применении мемоизации за счет извлеченияя из памяти
# значения при повторении вызова функции для того же числа.
# randint() срабатывает 1 раз при смене числа. Далее повторы идут с тем же числом.
# Кеш не чистится. Он создается один раз на запуск всего кода.
# Имеет смысл делать замер для одного запуска на новом числе.
# В этом случае время возрастает практически в полтора раза.

print("Сравнение для одного запуска преобразования нового числа.")
print("Вызов recursive_reverse:")
print(
    timeit(
        "recursive_reverse(754213486789182461975432846)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=1))
print("Вызов recursive_reverse_mem:")
print(
    timeit(
        'recursive_reverse_mem(754213486789182461975432846)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=1))
