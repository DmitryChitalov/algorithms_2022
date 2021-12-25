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

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


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
    revers_num = str()
    for i in reversed(enter_num):
        revers_num = revers_num + i
    return revers_num

print(revers_1(123456789), timeit('revers_1(123456789)', globals=globals()))
print(revers_2(123456789), timeit('revers_2(123456789)', globals=globals()))
print(revers_3(123456789), timeit('revers_3(123456789)', globals=globals()))
print(revers_4(123456789), timeit('revers_4(123456789)', globals=globals()))

# Замеры: 1 - 1.243 сек, самая долгая функция, так как используется рекурсия, а следовательно и самая высокая сложность,
# 2 - 0.806 сек, 3 - 0.190 сек, самая быстрая функция, так как делается срез, а значит меньше синтаксического
# анализа, 4 - 0.525 сек
