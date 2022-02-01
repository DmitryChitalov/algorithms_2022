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
        return int(revers_num)  # добавил вывод int(revers_num), иначе не работало
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)  # добавил return, иначе не работало


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
    enter_num = list(str(enter_num))
    enter_num.reverse()
    revers_num = ''.join(enter_num)
    return revers_num


numb = 1233576457567
print(timeit("revers(numb)", setup="from __main__ import revers, numb",
             number=1000))
# Самый долгий алгоритм т.к. использована рекурсия,сложность экспоненциальная
# 0.003428500000000001

print(timeit("revers_2(numb)", setup="from __main__ import revers_2, numb",
             number=1000))
# Алгоритм через цикл, несколько быстрее предыдущего, сложность O(N)
# 0.002561599999999997

print(timeit("revers_3(numb)", setup="from __main__ import revers_3, numb",
             number=1000))
# Реверс числа с помощью среза получается самым эффективным, судя по времени исполнения, сложность O(N)
# 0.0003438000000000052

print(timeit("revers_4(numb)", setup="from __main__ import revers_4, numb",
             number=1000))
# Алгоритм с использованием встроенной функции reverse() и джойном тоже довольно эффективен, хотя и дольше среза, 
# сложность O(N) 
# 0.0007293999999999981 
