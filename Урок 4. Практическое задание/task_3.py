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
        return int(revers_num)
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
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return int(revers_num)


def revers_4(enter_num):
    return int(''.join(list(reversed(str(enter_num)))))


def revers_5(enter_num):
    new_str = ''
    for i in str(enter_num):
        new_str = i + new_str
    return int(new_str)


number = 6557841546546032
print(timeit(
        'revers(number)',
        setup='from __main__ import revers, number',
        number=10000))
print(timeit(
        'revers_2(number)',
        setup='from __main__ import revers_2, number',
        number=10000))
print(timeit(
        'revers_3(number)',
        setup='from __main__ import revers_3, number',
        number=10000))

print(timeit(
        'revers_4(number)',
        setup='from __main__ import revers_4, number',
        number=10000))

print(timeit(
        'revers_5(number)',
        setup='from __main__ import revers_5, number',
        number=10000))

# 0.04434999998193234
# 0.031493899994529784
# 0.004790000035427511
# 0.008531400002539158
# 0.015772700018715113
# чтобы было по-честному - все результаты привел к int
# Первая реализация - это рекурсия с вычислением остатка от деления, она самая долгая, потому что рекурсия
# Вторая - та же, арифметика, но через цикл. чуть быстрее, но тоже долга.
# Третья - использование встроенного класса slice - самое оптимальное.
# Четвертая - использование встроенной функции reversed() тоже быстрое,
#   но чуть медленней из-за большого количества преобразования типов.
# Пятая - конкатенация в цикле. Самый быстрый из способов, в которых нет встроенных функций.
