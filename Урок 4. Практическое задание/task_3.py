"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import Timer


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
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


def revers_5(enter_num):
    revers_num = []
    enter_num = str(enter_num)
    for i in range(len(enter_num) - 1, -1, -1):
        revers_num.append(enter_num[i])
    revers_num = ''.join(revers_num)
    return revers_num


print(revers(123))
print(revers_2(123))
print(revers_3(123))
print(revers_4(123))
print(revers_5(123))

t1 = Timer(stmt='revers', setup='from __main__ import revers')
print("функция revers  ", t1.timeit(number=10000000), 'seconds')

t2 = Timer(stmt='revers_2', setup='from __main__ import revers_2')
print("функция revers_2", t1.timeit(number=10000000), 'seconds')

t3 = Timer(stmt='revers_3', setup='from __main__ import revers_3')
print("функция revers_3", t1.timeit(number=10000000), 'seconds')

t4 = Timer(stmt='revers_4', setup='from __main__ import revers_4')
print("функция revers_4", t1.timeit(number=10000000), 'seconds')

t5 = Timer(stmt='revers_5', setup='from __main__ import revers_5')
print("функция revers_5", t1.timeit(number=10000000), 'seconds')

# функция revers   0.22059150016866624 seconds
# функция revers_2 0.22204720019362867 seconds
# функция revers_3 0.2215895999688655 seconds
# функция revers_4 0.3532730001024902 seconds
# функция revers_5 0.23615869996137917 seconds

# Замеры показывают, что наиболее быстрый вариант - это срез. он самый лаконичый и эффективнее всего совершает
# необходимую операцию
