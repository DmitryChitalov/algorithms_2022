"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

import timeit


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


def revers_4(enter_num, reverse_num=''):
    if enter_num == 0:
        return str(reverse_num)
    else:
        a_digit = enter_num % 10
        enter_num //= 10
        reverse_num = reverse_num + str(a_digit)
        return revers_4(enter_num, reverse_num)


a_num = 987654
print('Время выполнения функции revers (1000000 раз): ',
      timeit.timeit('revers(a_num)', 'from __main__ import revers, a_num'))
print('Время выполнения функции revers_2 (1000000 раз): ',
      timeit.timeit('revers_2(a_num)', 'from __main__ import revers_2, a_num'))
print('Время выполнения функции revers_3 (1000000 раз): ',
      timeit.timeit('revers_3(a_num)', 'from __main__ import revers_3, a_num'))
print('Время выполнения функции revers_4 (1000000 раз): ',
      timeit.timeit('revers_4(a_num)', 'from __main__ import revers_4, a_num'))


# Время выполнения функции revers (1000000 раз):  4.345343799999682
# Время выполнения функции revers_2 (1000000 раз):  3.0494667000020854
# Время выполнения функции revers_3 (1000000 раз):  0.6507244000094943
# Время выполнения функции revers_4 (1000000 раз):  4.676864999986719
#
# Третья реализация эффективнее остальных, т.к. ее сложность минимальна.
# В алгоритмах 1 и 4 применяется рекурсия, что значительно повышает сложность
# и увеличивает время выполнения функций. Алгоритм 2 выполняется несколько
# быстрее вариантов с рекурсией, но содержит цикл, также существенно
# замедляющий скорость решения.
