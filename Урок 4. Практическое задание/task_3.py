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


def revers_4(enter_num):
    l = []
    for i in str(enter_num):
        l.append(i)
    l.reverse()
    l = ''.join(l)
    return l


enter_num = 123456789

print(f'revers time execution: {timeit("revers(enter_num)", globals=globals())}')
print(f'revers_2 time execution: {timeit("revers_2(enter_num)", globals=globals())}')
print(f'revers_3 time execution: {timeit("revers_3(enter_num)", globals=globals())}')
print(f'revers_4 time execution: {timeit("revers_4(enter_num)", globals=globals())}')

"""Учитывая результаты исполнения четырех функций:
revers time execution: 2.6963815
revers_2 time execution: 1.8414309579999997
revers_3 time execution: 0.37559666699999994
revers_4 time execution: 1.236689084

Наиболее быстрое исполнение у функции revers_3 работающей на основе срезов.
Самое длительное время исполнения у фунции на основе рекурсии.
"""



