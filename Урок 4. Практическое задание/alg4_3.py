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


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


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
    enter_num = reversed(str(enter_num))
    return ''.join(enter_num)


nums = 123456789
print(revers_1(nums))
print(revers_2(nums))
print(revers_3(nums))
print(revers_4(nums))
print(f'рекурсией: {timeit(f"revers_1(nums)", globals=globals(), number=10000)}')
print(f'циклом: {timeit(f"revers_2(nums)", globals=globals(), number=10000)}')
print(f'срезом: {timeit(f"revers_3(nums)", globals=globals(), number=10000)}')
print(f'reversed и join: {timeit(f"revers_4(nums)", globals=globals(), number=10000)}')


# срезом эффективнее, тк обращение по индексу и нет математических вычислений, в отличие от 1и 2 способов.
# reversed и join медленнее работают, возможно потому что 2 действия (вызов функции и метода)
