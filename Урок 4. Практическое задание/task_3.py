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
    return ''.join(reversed(str(enter_num)))


enter_num = 1234567890

print(
    'Число наоборот на рекурсиях: ',
    timeit(
        f'revers_1({enter_num})',
        globals=globals()))

print(
    'Число наоборот на циклах: ',
    timeit(
        f'revers_2({enter_num})',
        globals=globals()))

print(
    'Число наоборот на срезах: ',
    timeit(
        f'revers_3({enter_num})',
        globals=globals()))

print(
    'Число наоборот через реверс: ',
    timeit(
        f'revers_4({enter_num})',
        globals=globals()))

run("revers_1(enter_num)")
run("revers_2(enter_num)")
run("revers_3(enter_num)")
run("revers_4(enter_num)")

"""
Применено 3 вида реализации задачи ( рекурсия, цикл, срез, реверс).
Согласно полученным результатам видно что срез наиболее быстрый в плане выполнения
задачи. Рекурсия и цикл имеют арифмитические действия поэтому они проигрывают
в скорости по сравнению со срезом в котором отсутствуют арифмитические действия.
Следовательно в подобных задачах оптимально использовать срез.

Число наоборот на рекурсиях:  3.272293691
Число наоборот на циклах:  2.1066223089999996
Число наоборот на срезах:  0.41483651099999985
Число наоборот через реверс:  0.7546048089999999
"""