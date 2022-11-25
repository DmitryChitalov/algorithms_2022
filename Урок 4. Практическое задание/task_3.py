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
    if enter_num < 10:
        return enter_num
    return str(enter_num % 10) + str(revers_4(enter_num // 10))


def revers_5(enter_num):
    num_list = list(str(enter_num))
    num_list.reverse()
    return ''.join(num_list)


if __name__ == '__main__':
    num = 315628546
    print(revers(num))
    print(revers_2(num))
    print(revers_3(num))
    print(revers_4(num))
    print(revers_5(num))

    print(timeit('revers(num)', setup='from __main__ import revers, num', number=1000))
    print(timeit('revers_2(num)', setup='from __main__ import revers_2, num', number=1000))
    print(timeit('revers_3(num)', setup='from __main__ import revers_3, num', number=1000))
    print(timeit('revers_4(num)', setup='from __main__ import revers_4, num', number=1000))
    print(timeit('revers_5(num)', setup='from __main__ import revers_5, num', number=1000))
"""
Первая функция возвращает None
Вторая функция добавляет .0 в конце
Функция revers_3 отрабатывает быстрее всех, на втором месте revers_5 - т.к. в них нет циклов и рекурсий
"""