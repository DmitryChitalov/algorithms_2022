"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
import random
from timeit import timeit


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


# мой вариант решения
def revers_4(ent_num):
    return ''.join(reversed(str(ent_num)))


value = random.randint(100, 10000)
print(revers_4(value))
print(timeit('revers(value)', globals=globals(), number=1000))
print(timeit('revers_2(value)', globals=globals(), number=1000))
print(timeit('revers_3(value)', globals=globals(), number=1000))
print(timeit('revers_4(value)', globals=globals(), number=1000))

"""
Вывод:
0.018205100088380277
0.0006040999433025718
0.0002929000183939934
0.0006666000699624419
быстрее оказался метод revers_3, так как срез является встроенным инструментом, поэтому он быстрее
"""