"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from random import randint
from timeit import timeit


def time_search(f):
    def wrapper(*args):
        f_time = timeit(f'{f(*args)}', number=100)
        return f_time
    return wrapper


@time_search
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


@time_search
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


@time_search
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(n, i=0, get_start=0):
    while n % 10 == 0 and get_start == 0:
        n = n // 10
        i += 1
    if n // 10 == 0:
        return str(n)

    element = str(n % 10)
    get_start = 1
    return element + revers_4(n // 10, i, get_start)


res = 'revers_4(number)'

number = randint(10000000000000000000000000, 100000000000000000000000000)
print(number)
print(revers(number))
print(revers_2(number))
print(revers_3(number))
print(timeit(res, globals=globals(), number=100))
# Для number = 93173729473891208498992028 следующие результаты:
# revers 9.9.00000000001594e-07
# revers_2 9.00000000001594e-07
# revers_3 9.00000000001594e-07
# revers_4 0.0011767999999999987
# Вывод: скорости выполнения первых трех функций практически равны, а последняя сильно отстаёт от них.
# Рекурсия проигрывает других решениям в данном случае