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
from random import randint

def revers(enter_num, revers_num=0):
    """
    Разворачивает число математически, путём деления на 10 с отделением целой части и остатка. Далее прибавляет к
    переменной результата остаток и умножает на 10 чтобы перенести разряд цифр на 1 выше. Далее посылает целую часть и
    результат в себя же. Можно добавить меморизатор. 3-я по скорости
    :param enter_num:
    :param revers_num:
    :return:
    """
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


"""
    Разворачивает число математически, путём деления на 10 с отделением целой части и остатка. Далее прибавляет к 
    переменной результата остаток и умножает на 10 чтобы перенести разряд цифр на 1 выше. Аналогична первой функции, но 
    происходит в цикле и не может быть эффективно меморизирована. 2-я по скорости, эффективнее первой так как не рекурсивна
    :param enter_num: 
    :param revers_num: 
    :return: 
    """
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    """
    Функция разворачивает число путём перевода его в строковый тип и создания слайса строки в обратном направлении. Не
    выполняет математических действий, а создаёт новую строку с другим порядком символов, для большей правильности
    измерения нужно добавить приведение к int
    :param enter_num:
    :return:
    """
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def revers_m(enter_num, revers_num=0):
    """
    Аналогична revers но с меморизатором. Неэффективна на используемых диапазонах чисел
    :param enter_num:
    :param revers_num:
    :return:
    """
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)




num_100 = randint(100000, 999999)
num_1000 = randint(1000000, 9999999)
num_10000 = randint(1000000000000, 9999999999999)

print('функция revers')
print(
    timeit(
        "revers(num_100)",
        setup='from __main__ import revers, num_100',
        number=10000))
print(
    timeit(
        "revers(num_1000)",
        setup='from __main__ import revers, num_1000',
        number=10000))
print(
    timeit(
        "revers(num_10000)",
        setup='from __main__ import revers, num_10000',
        number=10000))


print('функция revers_2')
print(
    timeit(
        "revers_2(num_100)",
        setup='from __main__ import revers_2, num_100',
        number=10000))
print(
    timeit(
        "revers_2(num_1000)",
        setup='from __main__ import revers_2, num_1000',
        number=10000))
print(
    timeit(
        "revers_2(num_10000)",
        setup='from __main__ import revers_2, num_10000',
        number=10000))


print('функция revers_3')
print(
    timeit(
        "int(revers_3(num_100))",
        setup='from __main__ import revers_3, num_100',
        number=10000))
print(
    timeit(
        "int(revers_3(num_1000))",
        setup='from __main__ import revers_3, num_1000',
        number=10000))
print(
    timeit(
        "int(revers_3(num_10000))",
        setup='from __main__ import revers_3, num_10000',
        number=10000))


rm = lambda : revers_m(randint(10000, 99999))
r1 = lambda : revers(randint(10000, 99999))
r2 = lambda : revers_2(randint(10000, 99999))
r3 = lambda : revers_3(randint(10000, 99999))


print('\n промежуток (10000, 99999)')
print('функция revers_m')
print(
    timeit(rm,
        number=10000))
print('функция revers')
print(
    timeit(r1,
        number=10000))
print('функция revers_2')
print(
    timeit(r2,
        number=10000))
print('функция revers_3')
print(
    timeit(r3,
        number=10000))



rm = lambda : revers_m(randint(100000, 999999))
r1 = lambda : revers(randint(100000, 999999))
r2 = lambda : revers_2(randint(100000, 999999))
r3 = lambda : revers_3(randint(100000, 999999))


print('\n промежуток (100000, 999999)')
print('функция revers_m')
print(
    timeit(rm,
        number=10000))
print('функция revers')
print(
    timeit(r1,
        number=10000))
print('функция revers_2')
print(
    timeit(r2,
        number=10000))
print('функция revers_3')
print(
    timeit(r3,
        number=10000))


rm = lambda : revers_m(randint(1000000000000, 9999999999999))
r1 = lambda : revers(randint(1000000000000, 9999999999999))
r2 = lambda : revers_2(randint(1000000000000, 9999999999999))
r3 = lambda : revers_3(randint(1000000000000, 9999999999999))


print('\n промежуток (1000000000000, 9999999999999)')
print('функция revers_m')
print(
    timeit(rm,
        number=10000))
print('функция revers')
print(
    timeit(r1,
        number=10000))
print('функция revers_2')
print(
    timeit(r2,
        number=10000))
print('функция revers_3')
print(
    timeit(r3,
        number=10000))