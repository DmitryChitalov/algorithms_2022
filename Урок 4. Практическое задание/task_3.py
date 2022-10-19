"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import timeit, default_timer

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

    # revers_num = reversed(str(enter_num))
    revers_num=''
    for num in reversed(str(enter_num)):
        revers_num += num
    return revers_num


num = 1536546
print(revers(num))
print(revers_2(num))
print(revers_3(num))
print(revers_4(num))

print(timeit('revers(num)', 'from __main__ import revers, num', default_timer, 10000))
print(timeit('revers_2(num)', 'from __main__ import revers_2, num', default_timer, 10000))
print(timeit('revers_3(num)', 'from __main__ import revers_3, num', default_timer, 10000))
print(timeit('revers_4(num)', 'from __main__ import revers_4, num', default_timer, 10000))

## Почему не работает globals() ?
# print(timeit('revers(num)', globals = globals(), default_timer, 10000))




# Выводы
# Вариант 3 - эффективнее, т.к. имеет наименьшую сложность O(1) и минимальное число переменных и операций
#   по сравнению с другими решениями: вариант 1 - рекурсия: сложность O(2^n), 2 - сложность O(n), на 1 переменную больше, больше операций (цикл)
#   вариант 4 - сложность O(n), но больше переменных, и больше операций (цикл).





