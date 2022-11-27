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
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# Добавим реверс числа через реверс списка:
def revers_4(enter_num):
    revers_list = list(str(enter_num))
    revers_list.reverse()
    revers_num = "".join(revers_list)
    return revers_num


test_num = 123456789

print('Рекурсия -', timeit(f'revers_1({test_num})', globals=globals()))
print('-'*100)
print('Цикл -', timeit(f'revers_2({test_num})', globals=globals()))
print('-'*100)
print('Срез из строки -', timeit(f'revers_3({test_num})', globals=globals()))
print('-'*100)
print('Реверс списка из строки -', timeit(f'revers_4({test_num})', globals=globals()))
print('-'*100)

"""
Получившиеся результаты:

Рекурсия - 1.7139440999962972
----------------------------------------------------------------------------------------------------
Цикл - 1.1649120000001858
----------------------------------------------------------------------------------------------------
Срез из строки - 0.25143609999940963
----------------------------------------------------------------------------------------------------
Реверс списка из строки - 0.44680959999823244
----------------------------------------------------------------------------------------------------

Срез отрабатывает наиболее оперативно, т.к. имеет сложность O(N).
Добавленный способ на втором месте (имеет сложность O(N)).
"""
