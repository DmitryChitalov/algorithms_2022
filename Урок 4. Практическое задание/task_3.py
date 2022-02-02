"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
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


def revers_4(enter_num):
    return int("".join(reversed(str(enter_num))))


def revers_5(enter_num):
    revers_num = 0
    while enter_num > 0:
        enter_num, r = divmod(enter_num, 10)
        revers_num = revers_num * 10 + r
    return revers_num


n = 1234567

print('Время рекурсии: ', timeit('revers(n)', number=1000, globals=globals()))
print('Время цикла: ', timeit('revers_2(n)', number=1000, globals=globals()))
print('Время среза: ', timeit('revers_3(n)', number=1000, globals=globals()))
print('Время метода списка reversed: ', timeit('revers_4(n)', number=1000, globals=globals()))
print('Время функции divmod: ', timeit('revers_5(n)', number=10000, globals=globals()))


# Самый быстрый вариант - срез. Возможно потому что срез не выполняет вычисления
# а посто берет элементы по индексам в обратном порядке
