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

number = 42375345


def revers(enter_num, revers_num=0):
    # print(revers_num)
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
        # return str(revers(enter_num, revers_num))


print(
    timeit(
        'revers(number)',
        globals=globals(),
        number=10000))
# print(revers(number))


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print(
    timeit(
        'revers_2(number)',
        globals=globals(),
        number=10000))
# print(revers_2(number))


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

'''
3-й вариант решения самый быстрый, так как в нём в основном используются встроенные функции python и срезы строк
'''
print(
    timeit(
        'revers_3(number)',
        globals=globals(),
        number=10000))


def revers_4(num):
    if num == 0:
        return ''
    return int(f'{str(num % 10)}{revers_4(num // 10)}')


print(
    timeit(
        'revers_4(number)',
        globals=globals(),
        number=10000))