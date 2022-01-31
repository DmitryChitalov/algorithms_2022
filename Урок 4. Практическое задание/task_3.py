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
    enter_num = str(enter_num)
    revers_num = ''.join(reversed(enter_num))
    return revers_num


enter_num = 1234567899874563210
print(timeit("revers(enter_num)", globals=globals(), number=1000))      # 0.006542599999999996
print(timeit("revers_2(enter_num)", globals=globals(), number=1000))    # 0.0056104000000000015
print(timeit("revers_3(enter_num)", globals=globals(), number=1000))    # 0.0005196999999999979
print(timeit("revers_4(enter_num)", globals=globals(), number=1000))    # 0.0012665999999999927

# быстрее всего выполняется переворот строки с помощью среза,
# затем с помощью встроенных функций reversed() и join(),
# самый медленный способ с использованием рекурсии
