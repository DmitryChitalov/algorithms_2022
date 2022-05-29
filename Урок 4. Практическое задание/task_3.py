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
from random import randint


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
    temp_list = [el for el in str(enter_num)]
    return ''.join(list(reversed(temp_list)))


if __name__ == '__main__':
    number = randint(100000000000000, 10000000000000000000000000000000)
    print(timeit('revers(number)', number=10000, globals=globals()))
    print(timeit('revers_2(number)', number=10000, globals=globals()))
    print(timeit('revers_3(number)', number=10000, globals=globals()))
    print(timeit('revers_4(number)', number=10000, globals=globals()))

"""
Самой быстрой функцией будет функция с обратным срезом(revers_3) т.к. в ней нет цикла и нет рекурсии
"""
