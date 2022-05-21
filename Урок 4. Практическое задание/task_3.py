"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from random import randint
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
    return ''.join([i for i in str(enter_num)[::-1]])


def revers_5(enter_num):
    return ''.join(list(reversed(list(str(enter_num)))))


if __name__ == '__main__':
    num_100 = randint(10000, 1000000)

    print(timeit('revers(num_100)', 'from __main__ import revers, num_100', number=10000))
    print(timeit('revers_2(num_100)', 'from __main__ import revers_2, num_100', number=10000))
    print(timeit('revers_3(num_100)', 'from __main__ import revers_3, num_100', number=10000))
    print(timeit('revers_4(num_100)', 'from __main__ import revers_4, num_100', number=10000))
    print(timeit('revers_5(num_100)', 'from __main__ import revers_5, num_100', number=10000))

"""
0.020741399             - 4 место - рекурсия
0.012692201             - 3 место - цикл while + арифметика
0.004178497999999989    - 1 место - вариант с обратным прочтением строки (::-1)
0.010106192             - 2 место - list comprehension с обратным перебором списка
0.010470545999999997    - 2 место - функция reversed() для списка
"""
