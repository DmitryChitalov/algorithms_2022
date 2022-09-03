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

N = 23 ** 100  # Число для "отзеркаливания"


def revers(enter_num, revers_num=''):
    if enter_num == 0:
        return revers_num
    else:
        revers_num += str(enter_num % 10)
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=''):
    while enter_num != 0:
        revers_num += str(enter_num % 10)
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    reverse_num = ''
    for el in str(enter_num):
        reverse_num = el + reverse_num
    return reverse_num


print(f'Рекурсия : {timeit("revers(N)", globals=globals(),number=10000)}')
print(f'Цикл : {timeit("revers_2(N)", globals=globals(),number=10000)}')
print(f'Срез строки : {timeit("revers_3(N)", globals=globals(),number=10000)}')
print(f'Посимвольный перебор строки : {timeit("revers_4(N)", globals=globals(),number=10000)}')

'''
Рекурсия : 0.6549074000213295
Цикл : 0.43801270006224513
Срез строки : 0.01126370020210743
Посимвольный перебор строки : 0.10998630011454225

Как мы видим из замеров: самым высоким показателем производительности обладает срез: в среднем в 10/40 раз быстрее,
чем прочие способы. Преимущество скорости достигается за счет того, что иттерации в срезе происходят на более
быстром языке (Си)
'''
