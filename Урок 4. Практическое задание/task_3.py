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


def revers_4(enter_num):
    reversed_list = []
    for i in reversed(str(enter_num)):
        reversed_list.append(i)
    return ''.join(reversed_list)


nums = 1233576457567
print(timeit("revers(nums)", setup="from __main__ import revers, nums", number=1000))
print(timeit("revers_2(nums)", setup="from __main__ import revers_2, nums", number=1000))
print(timeit("revers_3(nums)", setup="from __main__ import revers_3, nums", number=1000))
print(timeit("revers_4(nums)", setup="from __main__ import revers_4, nums", number=1000))


"""
1)Самый долгий т.к. использована рекурсия, сложность O(2^N)
0.004431499999999998
2)Через цикл, быстрее предыдущего, сложность O(N)
0.003291200000000008
3)С помощью среза получается самым эффективным, судя по времени исполнения, сложность O(N)
0.0010329000000000033
4)С использованием встроенной функции reverse() и джойном, хоть и дольше среза, но тоже имеет место быть сложность O(N)
0.002906999999999993
"""