"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import timeit
from random import randint


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    enter_num = str(enter_num)
    result = ''
    for s in enter_num:
        result = s + result
    return result


def revers_5(enter_num):
    return ''.join(reversed(str(enter_num)))


my_num = randint(10000, 1000000)
print(my_num)

print(revers(my_num), timeit('revers(my_num)', globals=globals(), number=10000))
print(revers_2(my_num), timeit('revers_2(my_num)', globals=globals(), number=10000))
print(revers_3(my_num), timeit('revers_3(my_num)', globals=globals(), number=10000))
print(revers_4(my_num), timeit('revers_4(my_num)', globals=globals(), number=10000))
print(revers_5(my_num), timeit('revers_5(my_num)', globals=globals(), number=10000))

"""
Самый эффективный вариант - слайсинг (revers_3), потому что это встроенный механизм языка и он максимально оптимизирован
для таких задач.
"""
