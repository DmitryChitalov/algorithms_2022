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


def my_revers(enter_num):
    pass


n = 4011505

# print(revers(n))
print(f"Замер revers >>> "
      f"{timeit('revers(n)', globals=globals(), number=500000)}")
# print(revers_2(n))
print(f"Замер revers_2 >>> "
      f"{timeit('revers_2(n)', globals=globals(), number=500000)}")
# print(revers_3(n))
print(f"Замер revers_3 >>> "
      f"{timeit('revers_3(n)', globals=globals(), number=500000)}")
