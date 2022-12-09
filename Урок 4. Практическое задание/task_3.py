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
    return ''.join(n for n in reversed(str(enter_num)))


num = int(input('Введите число: '))
t1 = timeit('revers(num)', globals=globals(), number=1000)
t2 = timeit('revers_2(num)', globals=globals(), number=1000)
t3 = timeit('revers_3(num)', globals=globals(), number=1000)
t4 = timeit('revers_4(num)', globals=globals(), number=1000)
print(f'Время выполнения функции revers  {t1}')
print(f'Время выполнения функции revers_2  {t2}')
print(f'Время выполнения функции revers_3 {t3}')
print(f'Время выполнения функции revers_4  {t4}')

'''
Как видлно из аналитики функция revers_4 выполняется быстрее остальных за счет использования итератора, особенно ращзница
будет заметна при итерировании числа большего порядка.
'''
