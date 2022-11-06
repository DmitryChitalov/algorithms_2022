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
        return revers_num  # допущена ошибка в примере
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)  # допущена ошибка в примере


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
    revers_num = []
    for i in str(enter_num):
        revers_num.insert(0, i)
    return ''.join(revers_num)


my_nums = 123

print('Ф-ция №1 -', timeit('revers(my_nums)', globals=globals(), number=1000))
print('Ф-ция №2 -', timeit('revers_2(my_nums)', globals=globals(), number=1000))
print('Ф-ция №3 -', timeit('revers_3(my_nums)', globals=globals(), number=1000))
print('Ф-ция №4 -', timeit('revers_4(my_nums)', globals=globals(), number=1000))

'''
Ф-ция 3 работает быстрее, т.к в ней срезом копируется вся строка в обратном порядке,
это наименьшая сложность (O(n)) из вышеперечисленных ф-ций.
'''
