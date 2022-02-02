"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""


import timeit


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
    return reversed(f'{enter_num}')


if __name__ == '__main__':
    # revers(123456)
    # revers_2(123456)
    # revers_3(123456)
    # revers_4(123456)

    t = timeit.Timer(lambda: revers(123456))
    print(t.repeat(3))
    t = timeit.Timer(lambda: revers_2(123456))
    print(t.repeat(3))
    t = timeit.Timer(lambda: revers_3(123456))
    print(t.repeat(3))
    t = timeit.Timer(lambda: revers_4(123456))
    print(t.repeat(3))

# import модуля перенес вверх кода (в предыдущем варианте ДЗ был после инструкции if __name__ == '__main__)

# вместо мемоизации операций в функции в рекурсией в качестве четвертого варианта предложен новый
# улучшить время немного получилось, результаты:
# [1.0943018999999998, 1.0884261000000002, 1.0844249000000001]
# [0.7374728999999998, 0.7403700999999998, 0.7360201999999996]
# [0.25527250000000024, 0.25854210000000055, 0.25389700000000026]
# [0.19834829999999926, 0.19635340000000046, 0.19616170000000022]
