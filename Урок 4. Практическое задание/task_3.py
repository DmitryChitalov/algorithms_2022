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
---Что сделал и выводы---
Эффективная реализация в плане временных затрат, функция - revers_3. 
Так как срезы работают быстрее чем остальные представленные решения.

Функция revers_4 (Свой вариант решения) немного медленнее чем revers_3. Но имеет лучшую читабельность кода.
"""
from timeit import timeit  # Импорт timeit
from random import randint

rand_num = randint(10000, 1000000)


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


def revers_4(enter_num):  # Свой вариант решения
    return ''.join(reversed(str(enter_num)))


print('Время выполнения функции revers')
print(
    timeit(
        "revers(rand_num)",
        setup='from __main__ import revers, rand_num',
        number=10000))

print('Время выполнения функции revers_2')
print(
    timeit(
        "revers_2(rand_num)",
        setup='from __main__ import revers_2, rand_num',
        number=10000))

print('Время выполнения функции revers_3')
print(
    timeit(
        "revers_3(rand_num)",
        setup='from __main__ import revers_3, rand_num',
        number=10000))

print('Время выполнения функции revers_4')
print(
    timeit(
        "revers_4(rand_num)",
        setup='from __main__ import revers_4, rand_num',
        number=10000))
