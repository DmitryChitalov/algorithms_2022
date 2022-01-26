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
from random import randint


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
    revers_num = ''
    for i in range(len(str(enter_num)) - 1, -1, -1):
        revers_num = revers_num + str(enter_num)[i]
    return int(revers_num)


num_1000 = randint(1000000, 10000000)

print(
    f'{num_1000} -> {revers(num_1000)}\n{num_1000} -> {revers_2(num_1000)}\n{num_1000} -> {revers_3(num_1000)}\n{num_1000} -> {revers_4(num_1000)}\n')
print("revers", timeit("revers(randint(1000000, 10000000))", number=2000, globals=globals()), "seconds")
print("revers_2", timeit("revers_2(randint(1000000, 10000000))", number=2000, globals=globals()), "seconds")
print("revers_3", timeit("revers_3(randint(1000000, 10000000))", number=2000, globals=globals()), "seconds")
print("revers_4", timeit("revers_3(randint(1000000, 10000000))", number=2000, globals=globals()), "seconds")

# Первая не работает , вторая работает неверно, логично что третье самое эффективное , тк оно одинственное выполняет поставленную задачу :)
# По скорости третья самая быстрая, тк операция среза выполняется быстрее чем циклы и тем более чем рекурсия
# 5031434 -> None
# 5031434 -> 4341305.0
# 5031434 -> 4341305
# 5031434 -> 4341305

# По скорости третья самая быстрая, тк операция среза выполняется быстрее чем циклы с математическими выражениями и тем более, чем рекурсия.
# Мой вариант с проходом строки в обратном порядке работает примерно с той же скоростью, что и срез.
# revers 0.015004999999999998 seconds
# revers_2 0.009981900000000002 seconds
# revers_3 0.005346500000000004 seconds
# revers_4 0.005440399999999998 seconds
