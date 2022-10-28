"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

"""
Первый реверс самый долгий: создаем кучу переменных, записываем, и все это в рекурсии.
Во втором случае чуть быстрее, потому что не нужно накапливать в памяти, а потом возвращать и складывать кучу данных,
все делается в одной переменной, которая перезаписывается во время прохождения цикла.
Третий способ самый быстрый, использование среза еще и "in place", не создавая новый.
Мой способ - середина между ними, список создается, потом в нем переворачивается, не создавая новый, а потом собирается в одну переменную.
"""

from random import randint
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
    list_num = list(enter_num)
    list_num.reverse()
    revers_num = ''.join(list_num)
    return revers_num


num = randint(10000000, 10000000000)
print(num)

print(timeit("revers(num)", "from __main__ import revers, num", number=100000))
print(timeit("revers_2(num)", "from __main__ import revers_2, num", number=100000))
print(timeit("revers_3(num)", "from __main__ import revers_3, num", number=100000))
print(timeit("revers_4(num)", "from __main__ import revers_4, num", number=100000))
