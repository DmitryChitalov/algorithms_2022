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


def reverse_4(num):
    return f'{str(num)[::-1]}'


def revers_5(num):
    rev_num = ' '
    for i in range(len(str(num)) - 1, -1, -1):
        rev_num = rev_num + str(num)[i]
    return rev_num


def revers_6(num):
    return ''.join(reversed(str(num)))

number = 1233445454656
print(revers(number))
print(revers_2(number))
print(revers_3(number))
print(reverse_4(number))
print(revers_5(number))
print(revers_6(number))
print(timeit("revers(number)", number=100000, globals=globals()))  # 0.457196318
print(timeit("revers_2(number)", number=100000, globals=globals()))  # 0.48074139699999996
print(timeit("revers_3(number)", number=100000, globals=globals()))  # 0.06091120100000014
print(timeit("reverse_4(number)", number=100000, globals=globals()))  # 0.09956170499999994
print(timeit("revers_5(number)", number=100000, globals=globals()))  # 0.4739992380000002
print(timeit("revers_6(number)", number=100000, globals=globals()))  # 0.09554313699999994
# Срез и реверс работают быстрее всего.
