"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
import functools
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


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


def revers_4(numb):  # решение из разбора
    rest_numb, numeral = divmod(numb, 10)
    if rest_numb == 0:
        return str(numeral)
    else:
        return str(numeral) + str(revers_4(rest_numb))


def revers_5(enter_num):
    return ''.join(reversed(str(enter_num)))


def revers_6(enter_num):
    return functools.reduce(lambda x, y: y + x, str(enter_num))


def revers_7(enter_num):
    return bytes(reversed(bytearray(str(enter_num), 'UTF-8'))).decode('UTF-8')


number = 1234567890
# запуск функций и вывод результатов
[print(f"revers_{i}: (число, обратное) {number}, {eval(f'revers_{i}(number)')}") for i in range(1, 8)]
# профилировка каждого алгоритма через timeit
times = [timeit(f"revers_{n}(number)", f"from __main__ import revers_{n}, number", number=100000) for n in range(1, 8)]
t_otn = sorted([(t / min(times), f"revers_{i+1}") for i, t in enumerate(times)])
[print(f'{p}:{t:8.3f}') for t, p in t_otn]

'''
revers_3:   1.000   ; str(enter_num)[::-1]
revers_5:   2.306   ; ''.join(reversed(str(enter_num)))
revers_7:   3.006   ; bytes(reversed(bytearray(str(enter_num), 'UTF-8'))).decode('UTF-8')
revers_6:   4.797   ; functools.reduce(lambda x, y: y + x, str(enter_num))
revers_2:   5.456   ; вычисление в цикле (без рекурсии) с помощью //,%
revers_1:   7.899   ; рекурсивное вычисление  с помощью //,%
revers_4:  13.363   ; рекурсивное вычисление  с помощью //,%
Примерно так расположились по времени исполнения. Хуже всех рекурсия с арифм. операциями.
Лучший результат str[::-1]
'''