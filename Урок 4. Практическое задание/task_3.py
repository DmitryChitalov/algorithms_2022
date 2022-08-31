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


print('Рекурсия: ', timeit('revers(123456789, revers_num=0)', globals=globals(), number=1000))


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print('Цикл:', timeit('revers_2(123456789, revers_num=0)', globals=globals(), number=1000))


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print('Срез: ', timeit('revers_3(123456789)', globals=globals(), number=1000))


def revers_4(enter_num):
    a = str(enter_num)
    return ''.join(reversed(a))


print('Реверс: ', timeit('revers_4(123456789)', globals=globals(), number=1000))

''' Срез выполняется быстрее, так как не имеет арифметических действий '''
