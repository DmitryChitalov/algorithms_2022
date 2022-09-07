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
    val = enter_num % 10
    return revers(enter_num // 10, revers_num * 10 + val)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        val = enter_num % 10
        revers_num = revers_num * 10 + val
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


num = 456123
print(revers(num))
print(revers_2(num))
print(revers_3(num))
print(revers_4(num))
print(f"время функции revers(num): {timeit('revers(num)', globals=globals())}")
print(f"время функции revers_2(num): {timeit('revers_2(num)', globals=globals())}")
print(f"время функции revers_3(num): {timeit('revers_3(num)', globals=globals())}")
print(f"время функции revers_4(num): {timeit('revers_4(num)', globals=globals())}")

"""
время функции revers(num): 2.5433293000096455
время функции revers_2(num): 1.8602766999974847
время функции revers_3(num): 0.6965715999831446
время функции revers_4(num): 1.0167995000374503

эффективнее всего реализация реверса через срез"""