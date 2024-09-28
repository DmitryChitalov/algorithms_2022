"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from random import randint
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
    x = [str(a) for a in str(enter_num)]
    x.reverse()
    return ''.join(x)


cur_num = randint(1000000, 10000000)
print(timeit('revers(cur_num)', globals=globals()))
print(timeit('revers_2(cur_num)', globals=globals()))
print(timeit('revers_3(cur_num)', globals=globals()))
print(timeit('revers_4(cur_num)', globals=globals()))


"""
revers - 2.6041202000000003
revers_2 - 1.5860314999999998
revers_3 - 0.4402432000000003
revers_4 - 1.8873066000000005
Функция с использованием среза более эффективнее. Другие функции используют цикл и рекурсию, где присутствуют
математические операции, которые существенно снижают время выполнения кода.
"""
