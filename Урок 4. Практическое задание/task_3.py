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
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


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
    if not enter_num // 10:
        return enter_num % 10
    return f'{str(enter_num % 10)}{revers_4(enter_num // 10)}'


num = 4567893
print('Время revers', timeit('revers(num)', globals=globals(), number=10000))
print('Время revers_2', timeit('revers_2(num)', globals=globals(), number=10000))
print('Время revers_3', timeit('revers_3(num)', globals=globals(), number=10000))
print('Время revers_4', timeit('revers_4(num)', globals=globals(), number=10000))

"""
Функция revers_3 показывает наименьшее время выполнения, т.к. она имеет наименьшую сложность: встроенная функция 
преобразования в строку + проход по строке со сложностью O(n), где n - количество цифр в числе
"""
