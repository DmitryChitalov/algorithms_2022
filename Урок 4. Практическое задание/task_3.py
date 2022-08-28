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


def my_reverse(enter_num):
    temp_list = list(str(enter_num))
    temp_list.reverse()
    return ''.join(temp_list)


number = 23450

print(revers(number))
print(revers_2(number))
print(revers_3(number))
print(my_reverse(number))

print(timeit('revers(number)', globals=globals(), number=10000))
print(timeit('revers_2(number)', globals=globals(), number=10000))
print(timeit('revers_3(number)', globals=globals(), number=10000))
print(timeit('my_reverse(number)', globals=globals(), number=10000))

"""
Вывод: самая эффективная реализация - revers_3,
так как в ней меньше преобразований, 
в частности, не используются арифметические действия в отличии от двух первых реализаций,
и нет дополнительного преобразования списка, как в четвертой.
"""