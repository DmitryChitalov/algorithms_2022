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

enter_num = randint(10000, 100000)
print('Исходное число:', enter_num)
SETUP = 'from __main__ import revers, revers_2, revers_3, revers_4, revers_5, enter_num'
NUMBER = 100_000


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


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
    return str(enter_num)[::-1]


def revers_5(enter_num, revers_num=0):
    while enter_num:
        revers_num = revers_num * 10 + enter_num % 10
        enter_num //= 10
    return revers_num


print(timeit('revers(enter_num)', setup=SETUP, number=NUMBER))
print(timeit('revers_2(enter_num)', setup=SETUP, number=NUMBER))
print(timeit('revers_3(enter_num)', setup=SETUP, number=NUMBER))
print(timeit('revers_4(enter_num)', setup=SETUP, number=NUMBER))
print(timeit('revers_5(enter_num)', setup=SETUP, number=NUMBER))

print(revers(enter_num))
print(revers_2(enter_num))
print(revers_3(enter_num))
print(revers_4(enter_num))
print(revers_5(enter_num))

"""
    Первый вариант - рекурсивный имеет факториальную сложность. Отсюда и время выполнения увеличено. Остальные варианты 
имеют линейную сложность
    Второй и пятый варианты решены через цикл. Во втором варианте имеются "лишние переменные", в пятом варианте 
этих переменных нет. Вывод: пятый вариант быстрей чем второй.
    Третий и четвертый варианты решены через строку. Также как и во втором, в третьем варианте присутствуют ненужные 
переменные. Скорость выполнения четвертого варианта выше чем третьего.
По итогу всех замеров, быстрее всех работает четвертый вариант.
"""
