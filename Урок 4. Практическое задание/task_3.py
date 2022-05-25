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


def revers_4(number, num_str=''):
    if number == 0:
        return num_str
    else:
        part_num = number % 10
        num_str += '{}'.format(part_num)
        number = number // 10
        return revers_4(number=number, num_str=num_str)


print(timeit("revers(7412)", setup="from __main__ import revers", number=1000))
print(timeit("revers_2(7412)", setup="from __main__ import revers_2", number=1000))
print(timeit("revers_3(7412)", setup="from __main__ import revers_3", number=1000))
print(timeit("revers_4(7412)", setup="from __main__ import revers_4", number=1000))

"""
Результат:

0.0006236350000108359
0.0003958830000101443
0.0001885970000330417
0.0010624899999811532

Самая эффективная функция - revers_3
"""

