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
import time


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
    return str(enter_num)[::-1]


res_revers, res_revers_2, res_revers_3, res_revers_4, n = [], [], [], [], 0
while n < 10:
    res_revers.append(timeit.timeit(stmt='revers(1234567890)', setup='from __main__ import revers', number=1000))
    time.sleep(1)
    res_revers_2.append(timeit.timeit(stmt='revers_2(1234567890)', setup='from __main__ import revers_2', number=1000))
    time.sleep(1)
    res_revers_3.append(timeit.timeit(stmt='revers_3(1234567890)', setup='from __main__ import revers_3', number=1000))
    time.sleep(1)
    res_revers_4.append(timeit.timeit(stmt='revers_4(1234567890)', setup='from __main__ import revers_4', number=1000))
    time.sleep(1)
    n += 1

print(sum(res_revers) / len(res_revers), sum(res_revers_2) / len(res_revers_2), sum(res_revers_3) / len(res_revers_3),
      sum(res_revers_4) / len(res_revers_4), sep='\n')

'''
Результаты замеров:
0.009240419953130186
0.0077767200069502
0.0013581699691712855
0.0012164199491962791
Функция revers_4 наиболее эффективна.
'''
