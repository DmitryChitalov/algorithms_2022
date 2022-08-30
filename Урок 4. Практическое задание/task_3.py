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


def revers_4(n, b=0):
    if n != 0:
        b = b * 10 + n % 10
        n //= 10
        return revers_4(n, b)
    return b


print(timeit("revers(4623524)", number=1000000, globals=globals()))
print(timeit("revers_2(4623524)", number=1000000, globals=globals()))
print(timeit("revers_3(4623524)", number=1000000, globals=globals()))
print(timeit("revers_4(4623524)", number=1000000, globals=globals()))
"""Первый и третий вариант наименее эффективные, т.к. используют "тяжелую" рекурсию,
второй вариант - средней эффективности, т.к. содержит один цикл с простыми арифметическими действиями,
третий вариант - наиболее эффективный, т.к. содержит всего два действия  с О(n)"""