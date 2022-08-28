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
    revers_num = "".join(reversed(str(enter_num)))
    return revers_num


n = 780054300


r1 = """
revers(n)
"""

r2 = """
revers_2(n)
"""

r3 = """
revers_3(n)
"""


r4 = """
revers_4(n)
"""



print(timeit(r1, globals=globals(), number=10000))
print(timeit(r2, globals=globals(), number=10000))
print(timeit(r3, globals=globals(), number=10000))
print(timeit(r4, globals=globals(), number=10000))

# Среднее время выполнения revers: 0.016 сек -- наименее эфективная, очевидно из-за рекурсии
# Среднее время выполнения revers_2: 0.010 сек  -- средняя по эфективности, работает по принципу revers, но без рекурсии.Цикл while оказался эфективней
# Среднее время выполнения revers_3: 0.0022 сек -- эфективная, перезапись строки в обратном порядке оказалась эфективней чем while
# Среднее время выполнения revers_4: 0.0047 сек -- средняя по эфективности, функция reversed потребляет больше всего ресурсов

