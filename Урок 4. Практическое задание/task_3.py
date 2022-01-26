"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from timeit import default_timer, timeit


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
    enter_num1 = list(map(str, str(enter_num)))
    enter_num1.reverse()
    fn = ''.join(enter_num1)
    return fn


print(revers(123))
print(timeit('revers(123)', setup='from __main__ import revers', number=100))
print(revers_2(123))
print(timeit('revers_2(123)', setup='from __main__ import revers_2', number=100))
print(revers_3(123))
print(timeit('revers_3(123)', setup='from __main__ import revers_3', number=100))
print(revers_4(123))
print(timeit('revers_4(123)', setup='from __main__ import revers_4', number=100))
#Самая быстрая получается 3, т.к. встроенные функции самыем оптимизированные
