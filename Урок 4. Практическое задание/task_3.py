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
        return revers_num
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
    #enter_num = str(enter_num)
    revers_num = str(enter_num)[::-1]
    return revers_num

def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))

print('время для рекурсивного метода с делением на десять')
print(
    timeit(
        'revers(9876543210)',
        globals = globals(),
        number=1000000))
print('*'*30)
print('время для метода с циклом с делением на 10')
print(
    timeit(
        'revers_2(9876543210)',
        globals = globals(),
        number=1000000))
print('*'*30)
print('время для метода с присвоением среза')
print(
    timeit(
        'revers_3(9876543210)',
        globals = globals(),
        number=1000000))
print('*'*30)
print('время для метода с использовнием встроенной функции reversed')
print(
    timeit(
        'revers_4(9876543210)',
        globals = globals(),
        number=1000000))
"""
время для рекурсивного метода с делением на десять
2.872303660000398
******************************
время для метода с циклом с делением на 10
1.9000550260007003
******************************
время для метода с присвоением среза
0.342629841001326
******************************
время для метода с использовнием встроенной функции reversed
0.8606314469998324

Самый затратный метод - рекурсивный

Самый быстрый - присвоение среза

"""