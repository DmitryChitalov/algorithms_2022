"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from random import randint
from timeit import timeit

num_rnd = randint(10000, 1000000)


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


revers_4 = str(num_rnd)[::-1]

print(
    timeit(
        "revers(num_rnd)",
        globals=globals(),
        number=1000
    )
)
print(
    timeit(
        "revers_2(num_rnd)",
        globals=globals(),
        number=1000
    )
)
print(
    timeit(
        "revers_3(num_rnd)",
        globals=globals(),
        number=1000
    )
)

# Замер присвоения
print(
    timeit(
        "str(num_rnd)[::-1]",
        globals=globals(),
        number=1000
    )
)

"""
Вывод:
Работа со срезами горазда быстрее чем математические операции, так-же вызов функции тратит время 
даже если revers_3 удалить все и оставить только return str(enter_num[::-1]), будет выполняться дольше 
чем обычное присвоение str(num_rnd)[::-1]
"""
