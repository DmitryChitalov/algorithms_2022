from timeit import timeit
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

def revers_4(enter_num):
    revers_num = str(enter_num % 10)
    remain = enter_num // 10
    while remain:
        revers_num += str(remain % 10)
        remain //= 10
    return revers_num

setup = 'from __main__ import '
num = 12345678912345487789876543

print(timeit('revers(num)', setup=setup+'revers, num'))
print(timeit('revers_2(num)', setup=setup+'revers_2, num'))
print(timeit('revers_3(num)', setup=setup+'revers_3, num'))
print(timeit('revers_4(num)', setup=setup+'revers_4, num'))


"""     Аналитика
    Вемя затраченное на выполнение операций:
    1 - 7.4185146
    2 - 4.8584003
    3 - 0.42228140000000103
    4 - 7.692235100000001
    По оценки времени наиболее лучший вариант  это 3 метод среза
"""
