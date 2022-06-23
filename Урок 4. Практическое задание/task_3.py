from timeit import timeit
"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


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


def revers_4(num):
    return ''.join(reversed(list(str(num))))


print(revers_4(32018))
print(timeit(stmt='revers(32018)', number=1000, globals=globals()))
print(timeit(stmt='revers_2(32018)', number=1000, globals=globals()))
print(timeit(stmt='revers_3(32018)', number=1000, globals=globals()))
print(timeit(stmt='revers_4(32018)', number=1000, globals=globals()))

"""
результаты:
revers   0.0017858000355772674
revers_2 0.0012313000042922795
revers_3 0.00043710001045838
revers_4 0.0009418000117875636

Вывод: 
Согласно замерам, самую высокую скорость выполнения имеет revers_3
поскольку используются минимальное количество операций, только строковый срез
"""