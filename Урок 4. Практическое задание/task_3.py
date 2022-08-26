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
    return ''.join([num for num in str(enter_num)][::-1])


number = 5674567890976545678998765890
print(revers(number))
print(revers_2(number))
print(revers_3(number))
print(revers_4(number))

"""Судя по выводу результатов работы функций. Первая и вторая не выполняют поставленную задачу."""

print(timeit("revers(number)", globals=globals(), number=100000))
print(timeit("revers_2(number)", globals=globals(), number=100000))
print(timeit("revers_3(number)", globals=globals(), number=100000))
print(timeit("revers_4(number)", globals=globals(), number=100000))

"""Самый быстрый способ заключается в использовании срезов revers_3"""