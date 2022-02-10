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
    enter_num = str(enter_num)
    return "".join(reversed(enter_num))


n = 123
print(revers(n))
print(revers_2(n))
print(revers_3(n))
print(revers_4(n))

print(timeit(f'revers(n)', globals=globals(), number=1000))
print(timeit(f'revers_2(n)', globals=globals(), number=1000))
print(timeit(f'revers_3(n)', globals=globals(), number=1000))
print(timeit(f'revers_4(n)', globals=globals(), number=1000))

# 0.000632800001767464
# 0.0004543000031844713
# 0.00023430000146618113
# 0.0004056999969179742

# Срез — самый быстрый способ