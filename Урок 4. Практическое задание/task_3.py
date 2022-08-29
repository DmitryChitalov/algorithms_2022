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


def revers_4(numb):
    reversed_4 = 0
    while numb > 0:
        re = numb % 10
        reversed_4 = reversed_4 * 10 + re
        numb //= 10
    return reversed_4


print(timeit('revers(1230000000000000)', globals=globals(), number=100))
print(timeit('revers_2(1230000000000000)', globals=globals(), number=100))
print(timeit('revers_3(1230000000000000)', globals=globals(), number=100))
print(timeit('revers_4(1230000000000000)', globals=globals(), number=100))
print(revers_4(123456))
print(revers_4(123456))

'''Первое при больших числах имеет большее время исполнение, это свзано с рекурсивным
вызовом, третий получается самым удачным, так как имеет линейную сложность и количество итераций
прямо зависит от длинны числа, во втором случае придется выполнять дополнительные математические 
действия в завимисти от длинны, что тоже не хорошо влияет на скорость исполнения,
четвертый вариант так же является сложным из за математических операций'''