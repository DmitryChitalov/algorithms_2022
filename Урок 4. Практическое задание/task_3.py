"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
import random
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
    lst = list(str(enter_num))
    lst.reverse()
    return "".join(lst)


if __name__ == '__main__':
    enter_num = random.randint(100000, 1000000)

    print("revers:", timeit("revers(enter_num)", globals=globals(), number=10000))
    print("revers_2:", timeit("revers_2(enter_num)", globals=globals(), number=10000))
    print("revers_3:", timeit("revers_3(enter_num)", globals=globals(), number=10000))
    print("revers_4:", timeit("revers_4(enter_num)", globals=globals(), number=10000))

    """
    Самая эффективная реализация со взятием среза строки, т.к. она использует встроенные методы python.
    """