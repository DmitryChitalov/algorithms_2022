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
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


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



def main():
    revers_1(number_ent)
    revers_2(number_ent)
    revers_3(number_ent)
    revers_4(number_ent)

number_ent = 1234567890987654321234123412341234123457398537
number_str = str(number_ent)
print(len(number_str))

print(
    timeit(
        "revers_1(number_ent)",
        setup="from __main__ import revers_1, number_ent", number=10000))

print(
    timeit(
        "revers_2(number_ent)",
        setup="from __main__ import revers_2, number_ent", number=10000))

print(
    timeit(
        "revers_3(number_ent)",
        setup="from __main__ import revers_3, number_ent", number=10000))

print(
    timeit(
        "revers_4(number_ent)",
        setup="from __main__ import revers_4, number_ent", number=10000))

run('main()')

'''
Наиболее быстрая функция является разворот СТРОКИ через срезы. O(b-a)
На втором месте функция с join и встроенной сортировкой, встроенные функции работают быстрее
 При маленьком количестве элементов цикл WHILE на третьем месте пока число не будет равно 0,
 остаток от целочисленного деления на 10 записывается в новую переменную,
  а исчисляемое сокращается на один порядок. O(n)
При большом количестве элементов
 на втором месте ЦИКЛ FOR... IN... со сложностью  будет предпочтительнее. O(n)
Последнее место по производительности это РЕКУРСИВНАЯ функция
с экспонинциальной сложностью сложность O(2**n)

Вычисления производились для числа длиной 46 цифр
Профилирование функций не показывают замеров времени, видимо выполняются почти мгновенно и нужно более загрузить 
процессор.

revers_1 = 0.210682800039649
revers_2 = 0.17576330015435815
revers_3 = 0.010079200379550457
revers_4 = 0.02581339981406927
'''

