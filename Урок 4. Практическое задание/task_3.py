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


def revers_4(enter_num, a =''):
    if enter_num == 0:
        return
    else:
        number = enter_num % 10
        num_str = str(number)
        a = a + num_str
        enter_num = enter_num // 10

    revers_4(enter_num, a)


def revers_5(enter_num):
    rev = [str(i) for i in str(enter_num)]
    rev.reverse()
    return ''.join(rev)

enter_num = 12345670
print(timeit("revers(enter_num)", setup="from __main__ import revers, enter_num", number=10000))
print(timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num", number=10000))
print(timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num", number=10000))
print(timeit("revers_4(enter_num)", setup="from __main__ import revers_4, enter_num", number=10000))
print(timeit("revers_5(enter_num)", setup="from __main__ import revers_5, enter_num", number=10000))

# самые неэффективные по времени функция это рекурсивные (revers и revers_4)
# самая быстрая с применением среза, обращаемся сразу по индексу
# все остальные все +- одинаковые