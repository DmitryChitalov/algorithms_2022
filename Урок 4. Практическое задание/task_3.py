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
        return int(revers_num)                          # исправил ошибку в рекурсивной функции
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)            # исправил ошибку в рекурсивной функции

#print(revers(10525106142151052))

def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return "".join(reversed(str(enter_num)))


for func in (revers, revers_2, revers_3, revers_4):
    num = 10525106142151
    print(f"{func.__name__} takes: {timeit('func(num)', globals=globals())} s", )
    #print("Result: ", func(num))

""" 
На мой взгляд revers_3 реализована лучше всего, это лаконичность и скорость выполнения без лишний рекурсий и циклов
"""