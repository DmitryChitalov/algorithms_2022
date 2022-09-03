"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
import random
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
    res = []
    str_num = str(enter_num)
    for i in str_num:
        res.append(i)
    return sorted(res, reverse=True)


num = random.randint(1000, 10000)

print(timeit.timeit('revers(num)', globals=globals()))
print(timeit.timeit('revers_2(num)', globals=globals()))
print(timeit.timeit('revers_3(num)', globals=globals()))
print(timeit.timeit('revers_4(num)', globals=globals()))

"""
revers(num) - самый затратный, так как там используется рекурсия, которая медленней обычного цикла в revers_2(num)
revers_3(num) - самый быстрый способ, так как используется только преобразование к строке и вывод сортированной строки
revers_4(num) - мой вариант решения проблемы. Выполняется на уровне revers_2(num), так как в обоих функциях используется цикл

"""
