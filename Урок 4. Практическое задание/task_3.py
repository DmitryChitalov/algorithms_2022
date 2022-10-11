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

def my_revers(enter_num):
    a = ''
    while enter_num != 0:
        a += str(enter_num % 10)
        enter_num //= 10
    return a

def my_revers2(enter_num):
    a = []
    while enter_num != 0:
        a.append(str(enter_num%10))
        enter_num //= 10
    return ''.join(a)

n = 12345432234
print(timeit('revers(n)', globals=globals(), number=1000))
print(timeit('revers_2(n)', globals=globals(), number=1000))
print(timeit('revers_3(n)', globals=globals(), number=1000))
print(timeit('my_revers(n)', globals=globals(), number=1000))
print(timeit('my_revers2(n)', globals=globals(), number=1000))

"""
Быстрее всего работает третий вариант, так как там всего 2 действия сложность константная
"""