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


num = 123


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


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
    x = str(enter_num)
    y = ''
    for i in range(1, len(x)+1):
        y += x[-i]
    return int(y)


print(timeit(f'revers({num})', globals=globals()))
print(timeit(f'revers_2({num})', globals=globals()))
print(timeit(f'revers_3({num})', globals=globals()))
print(timeit(f'revers_4({num})', globals=globals()))

run("revers(num)")
run("revers_2(num)")
run("revers_3(num)")
run("revers_4(num)")

# Эффективнее всего срез, так он имеет меньшую сложность