from timeit import timeit
from timeit import repeat, default_timer
from random import randint

"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


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

setup = "num='12345013142346747890606898477366567368687969895625364878785985980676573673767773'"
statements = [
    'num = str(num)',
    """r_num = num[::-1]"""]

for st in statements:
    print(repeat(st, setup, default_timer, 3, 100000))


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


def revers_5(enter_num):
    s1 = ''
    for c in str(enter_num):
        s1 = c + s1
    return s1


print(timeit("revers",
             globals=globals(),
        number=10000))

print(timeit("revers_2",
             globals=globals(),
        number=10000))

print(timeit("revers_3",
             globals=globals(),
        number=10000))

print(timeit("revers_4",
             globals=globals(),
        number=10000))

print(timeit("revers_5",
             globals=globals(),
        number=10000))

num = randint(10000000000000000, 1000000000000000000000000000)

print('Собственные замеры:')
print(f'C применением рекурсии : {timeit("revers(num)", globals=globals(), number=10000)}')

print(f'Цикл loop  for: {timeit("revers_2(num)", globals=globals(), number=10000)}')
print(f'Взятие среза: {timeit("revers_3(num)", globals=globals(), number=10000)}')

print(f'Функция reversed к строке: {timeit("revers_4(num)", globals=globals(), number=10000)}')

print(f'С использованием конкатенации к строке: {timeit("revers_5(num)", globals=globals(), number=10000)}')


"""Cамым быстрым способ является способ переворачивания числа с использованием среза строки (в десятки раз быстрее).
Также этот способ является достаточно лаконичным (может быть написан в одну строку), однако менее читаемым,
 чем функция reversed к строке."""