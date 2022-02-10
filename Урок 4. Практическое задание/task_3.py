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
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


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
    return "".join(reversed(str(enter_num)))


input_number = int(input(f'Введите число для преобразования: '))
for func in (revers_1, revers_2, revers_3, revers_4):
    print(f'{func.__name__}: затраченое время {timeit("func(input_number)", globals=globals(), number=10000)}')

"""
Первая и вторая функции заметно медленнее из-за рекурсии в revers_1 O(2^n) и цикла в revers_2 эти алгоритмы
выполняются значительно дольше. Самый быстрый алгоритм использует срез.
Использование встроенных функций join и reversed в revers_4 требует вдвое больше времени, чем срез.
"""