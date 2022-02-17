"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
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
    enter_num = list(str(enter_num))
    for i in range(len(enter_num) // 2):
        enter_num[i], enter_num[-(i+1)] = enter_num[-(i+1)], enter_num[i]
    return enter_num


def revers_5(enter_num):
    enter_num = list(str(enter_num))
    return enter_num.reverse()

num = 101
print(f"revers() {timeit('revers(num ** num)', globals=globals(), number=10000)}")
print(f"revers_2() {timeit('revers_2(num ** num)', globals=globals(), number=10000)}")
print(f"revers_3() {timeit('revers_3(num ** num)', globals=globals(), number=10000)}")
print(f"revers_4() {timeit('revers_4(num ** num)', globals=globals(), number=10000)}")
print(f"revers_5() {timeit('revers_5(num ** num)', globals=globals(), number=10000)}")

"""
revers() 0.7710948
revers_2() 0.5276983999999999
revers_3() 0.02203569999999999
revers_4() 0.1545529000000001
revers_5() 0.0316748

Функциям revers и revers_2 требуется в двое больше шагов/итераций по сравнению с фукнцией revers_4.
Также наличие арифметических операций оказывает влияние на время выполнения.
Функции revers_3 и revers_5 используют встроенные операции

"""