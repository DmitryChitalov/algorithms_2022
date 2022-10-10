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
    return ''.join(reversed(str(enter_num)))


def revers_5(enter_num):
    return str(enter_num)[::-1]

num = 123456789

print('Замер для рекурсии: ', timeit("revers(num)", globals=globals()))    # 2.2990523999997095
print('Замер для цикла: ', timeit("revers_2(num)", globals=globals()))  # 1.5600940000003902
print('Замер для среза: ', timeit("revers_3(num)", globals=globals()))  # 0.31075910000072327
print('Замер для встроенного метода: ', timeit("revers_4(num)", globals=globals()))  # 0.6823621999992611
print('Замер для среза оптимиз.: ', timeit("revers_5(num)", globals=globals()))  # 0.29324280000037106

"""
Самая быстрая реализация через срез, которая выполняется всего в несколько действий
Далее идет встроенный метод, который оптимизирован 
В цикле производится многократное вычисление и потому время достаточно большое
Рекурсия является элегантным решением, но проигрывает по времени даже циклу из-за работы со стеком
"""
