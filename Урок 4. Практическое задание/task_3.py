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
    reverse_num = ''.join(reversed(list(enter_num)))
    return reverse_num


nums = 1230593423455556
print(timeit("revers(nums)", globals=globals(), number=1000))
print(timeit("revers_2(nums)", globals=globals(), number=1000))
print(timeit("revers_3(nums)", globals=globals(), number=1000))
print(timeit("revers_4(nums)", globals=globals(), number=1000))

"""
f_1 - 0.003102500000000001
f_2 - 0.002057499999999997
f-3 - 0.0003148999999999999
f_4 - 0.0008299999999999974

Функция 3 работает быстрее, т.к в ней используются встроенные функции.
Функция 4 работает чуть медленне, в ней используется встроенная функция reversed, 
но она работает дольше чем 3-я функция, возможно, потому что в ней используется преобразование в список и обратно
"""
