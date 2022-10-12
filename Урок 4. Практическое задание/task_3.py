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
    revers_num = ''
    for index in range(1, len(str(enter_num)) + 1):
        revers_num += str(enter_num)[-index]
    return revers_num


def revers_5(enter_num):
    reverse_num = list(str(enter_num))
    reverse_num.reverse()
    return ''.join(reverse_num)


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print(f'1.revers with num_100: {timeit("revers(num_100)", globals=globals(), number=100000)} sec;')
print(f'1.revers with num_1000: {timeit("revers(num_1000)", globals=globals(), number=100000)} sec;')
print(f'1.revers with num_10000: {timeit("revers(num_10000)", globals=globals(), number=100000)} sec;')

print(f'\n2.revers_2 with num_100: {timeit("revers_2(num_100)", globals=globals(), number=100000)} sec;')
print(f'2.revers_2 with num_1000: {timeit("revers_2(num_1000)", globals=globals(), number=100000)} sec;')
print(f'2.revers_2 with num_10000: {timeit("revers_2(num_10000)", globals=globals(), number=100000)} sec;')

print(f'\n3.revers_3 with num_100: {timeit("revers_3(num_100)", globals=globals(), number=100000)} sec;')
print(f'3.revers_3 with num_1000: {timeit("revers_3(num_1000)", globals=globals(), number=100000)} sec;')
print(f'3.revers_3 with num_10000: {timeit("revers_3(num_10000)", globals=globals(), number=100000)} sec;')

print(f'\n4.revers_4 with num_100: {timeit("revers_4(num_100)", globals=globals(), number=100000)} sec;')
print(f'4.revers_4 with num_1000: {timeit("revers_4(num_1000)", globals=globals(), number=100000)} sec;')
print(f'4.revers_4 with num_10000: {timeit("revers_4(num_10000)", globals=globals(), number=100000)} sec;')

print(f'\n5.revers_5 with num_100: {timeit("revers_5(num_100)", globals=globals(), number=100000)} sec;')
print(f'5.revers_5 with num_1000: {timeit("revers_5(num_1000)", globals=globals(), number=100000)} sec;')
print(f'5.revers_5 with num_1000: {timeit("revers_5(num_10000)", globals=globals(), number=100000)} sec;')

"""
Ввиду использования встроенных методов строки, самой быстрой является функция reverse_3
"""
