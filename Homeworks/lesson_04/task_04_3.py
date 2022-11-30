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


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
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
    revers_num = ''.join(reversed(enter_num))
    return revers_num


if __name__ == '__main__':
    number = 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
    print(timeit("revers(number)", globals=globals(), number=10000))
    print(timeit("revers_2(number)", globals=globals(), number=10000))
    print(timeit("revers_3(number)", globals=globals(), number=10000))
    print(timeit("revers_4(number)", globals=globals(), number=10000))

# Эффективнее всего функция revers_3, т.к. времени на её выполнение нужно меньше всего.
