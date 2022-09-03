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


def revers_4(enter_num):
    enter_num = str(enter_num)
    emp_list = []
    for x in enter_num:
        emp_list.insert(0, x)
    res_str = ''.join(emp_list)
    return res_str


print(timeit("revers(200000)", number=1000000, globals=globals()))
print(timeit("revers_2(200000)", number=1000000, globals=globals()))
print(timeit("revers_3(200000)", number=1000000, globals=globals()))
print(timeit("revers_4(200000)", number=1000000, globals=globals()))

"""
АНАЛИТИКА
Третий вариант (revers_3) является наиболее эффективным, т.к. состоит из наименьшего количества встроенных
(и имеющих низкую сложность) функций Python.

Результат:
3.3274356000000003
2.1113321999999997
0.7227752000000001
1.8926511000000001
"""
