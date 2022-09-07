"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from random import randrange
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


def number_revers(n):
    return f"{str(n % 10)}{number_revers(n // 10)}" if n // 10 > 0 else str(n % 10)


number = randrange(100000000000, 1000000000000)
print("Функция revers")
print(f"{timeit.timeit('revers(number)', globals=globals(), number=1000):.5f}")
print("Функция revers_2")
print(f"{timeit.timeit('revers_2(number)', globals=globals(), number=1000):.5f}")
print("Функция revers-3")
print(f"{timeit.timeit('revers_3(number)', globals=globals(), number=1000):.5f}")
print("Функция number_revers")
print(f"{timeit.timeit('number_revers(number)', globals=globals(), number=1000):.5f}")

"""
Быстрее всего работает функция revers-3, так как без циклов, с встроенной возможностью делать срезы.
Медленнее всего - рекурсия, конечно, потому что сама себя вызывает.
"""
