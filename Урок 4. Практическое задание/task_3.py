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
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    enter_lst = list(str(enter_num))
    revers_num = int(''.join(list(reversed(enter_lst))))
    return revers_num


num = 7249901
print(revers_1(num))
print(revers_2(num))
print(revers_3(num))
print(revers_4(num))

print(timeit("revers_1(num)", globals=globals(), number=10000))
print(timeit("revers_2(num)", globals=globals(), number=10000))
print(timeit("revers_3(num)", globals=globals(), number=10000))
print(timeit("revers_4(num)", globals=globals(), number=10000))

# revers_1 1099427
# revers_2 1099427
# revers_3 1099427
# revers_4 1099427

# revers_1 0.012189499975647777
# revers_2 0.007357400027103722
# revers_3 0.0019660000107251108
# revers_4 0.00671599997440353

'''
Срез в revers_3 работает быстрее всего,
потому что сложность срезов в O-нотации равна O(1)
У остальных же O(n) 
'''