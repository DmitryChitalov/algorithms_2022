from timeit import *
"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit.

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


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
    if enter_num == 0:
        return str(enter_num % 10)[0:-1]
    return f'{str(enter_num % 10)}{revers_4(enter_num // 10)}'


num = 123456
print("1 - ", revers(num))
print("2 - ", revers_2(num))
print("3 - ", revers_3(num))
print("4 - ", revers_4(num))
print("________")

print("1 - ", timeit("revers(num)", setup='from __main__ import revers, num', number=10000))
print("2 - ", timeit("revers_2(num)", setup='from __main__ import revers_2, num', number=10000))
print("3 - ", timeit("revers_3(num)", setup='from __main__ import revers_3, num', number=10000))
print("4 - ", timeit("revers_4(num)", setup='from __main__ import revers_4, num', number=10000))

"""3-тья функция самая быстрая, потому что в ней нет рекурсии, все исполняется 1 раз"""