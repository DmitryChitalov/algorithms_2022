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

num = 12365

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
    num_list = list(str(enter_num))
    num_list.reverse()
    return ''.join(num_list)


print(timeit.timeit('revers(num)', globals=globals(), number=1000))
print(timeit.timeit('revers_2(num)', globals=globals(), number=1000))
print(timeit.timeit('revers_3(num)', globals=globals(), number=1000))
print(timeit.timeit('revers_4(num)', globals=globals(), number=1000))

# Самый эффективный вариант решения - revers_3, т.к. времени на выполнение этой функции нужно меньше всего.
