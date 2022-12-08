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


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


num_user = 56491
print(revers_1.__name__, timeit("revers_1(num_user, revers_num=0)", globals=globals(), number=100000))


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print(revers_2.__name__, timeit("revers_2(num_user, revers_num=0)", globals=globals(), number=100000))


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(revers_3.__name__, timeit("revers_3(num_user)", globals=globals(), number=100000))


def revers_4(enter_num):
    list_num = list(str(enter_num))
    list_num.reverse()
    revers_num = "".join(list_num)
    return revers_num


print(revers_4.__name__, timeit("revers_4(num_user)", globals=globals(), number=100000))

'''revers_1
0.24936175404582173
revers_2
0.16684464900754392
revers_3
0.0498265769565478
revers_4
0.08016066101845354'''
'''Функция revers_3 имеет быструю скорость, потому что имеет сложность - O(1)'''
