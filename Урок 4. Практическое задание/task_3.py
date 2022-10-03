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
        return revers_num
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
    res = []
    for i in str(enter_num):
        res.insert(0, i)
    return ''.join(res)


num = 1000

print(f"revers(num): {timeit('revers(num)', globals=globals())}")
print(f"revers_2(num)': {timeit('revers_2(num)', globals=globals())}")
print(f"revers_3(num): {timeit('revers_3(num)', globals=globals())}")
print(f"my_revers(num){timeit('my_revers(num)', globals=globals())}")

#
# print(revers(num))
# print(revers_2(num))
# print(revers_3(num))
# print(my_revers(num))


# первые две реализации нельзя считать сопоставимыми с остальными, потому что они не работают.
# среди оставшихся insert и срезов, срезы показывают скорость в трираза выше.
# так вот они эффективно написаны эти срезы по своему замыслу и реализации.

