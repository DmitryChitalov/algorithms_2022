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
    return ''.join(reversed(str(enter_num)))


numb = 123
print(timeit('revers(numb)', 'from __main__ import revers, numb', number=10000))  # 0.024278400000000006
print(timeit('revers_2(numb)', 'from __main__ import revers_2, numb', number=10000))  # 0.017658800000000002
print(timeit('revers_3(numb)', 'from __main__ import revers_3, numb', number=10000))  # 0.008143999999999998
print(timeit('revers_4(numb)', 'from __main__ import revers_4, numb', number=10000))  # 0.01381220000000001
# Эффективнее всего срез
