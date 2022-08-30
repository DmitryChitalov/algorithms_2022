"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""

from timeit import timeit
from random import randint

test_num = randint(10000, 1000000)


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


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
    return ''.join(reversed(enter_num))


print(timeit("revers(test_num)", globals=globals(), number=10000))

print(timeit("revers_2(test_num)", globals=globals(), number=10000))

print(timeit("revers_3(test_num)", globals=globals(), number=10000))

print(timeit("revers_4(test_num)", globals=globals(), number=10000))

# третий способ быстрее, так как его сложность O(1), у других же алгоритмож сложность O(n)
