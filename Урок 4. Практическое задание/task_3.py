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
    list_1 = list(str(enter_num))
    list_1.reverse()
    revers_num = "".join(list_1)
    return revers_num


num = 87648
print(timeit("revers(num,0)", globals=globals()))  # 1.4761770000004617
print(timeit("revers_2(num,0)", globals=globals()))  # 1.0722294999995938
print(timeit("revers_3(num)", globals=globals()))  # 0.3501461999994717
print(timeit("revers_4(num)", globals=globals()))  # 0.5816566000003149

# В revers_3 срез строки. Это самый быстрый способ, т.к. сложность О(1)
# В моем варианте эффективность получается за счет встроенных функций.
