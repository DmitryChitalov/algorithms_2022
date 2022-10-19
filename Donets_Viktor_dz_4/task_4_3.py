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
    revers_num = ''
    for i in str(enter_num):
        revers_num = i + revers_num
    return revers_num


def revers_5(enter_num):
    return reversed(str(enter_num))


n = int(input('Введите число: '))
print(timeit("revers(n)", globals=globals(), number=1000))
print('!' * 25)
print(timeit("revers_2(n)", globals=globals(), number=1000))
print('!' * 25)
print(timeit("revers_3(n)", globals=globals(), number=1000))
print('!' * 25)
print(timeit("revers_4(n)", globals=globals(), number=1000))
print('!' * 25)
print(timeit("revers_5(n)", globals=globals(), number=1000))


"""
Введите число: 123456
0.001535399999738729
!!!!!!!!!!!!!!!!!!!!!!!!!
0.0010228999999526422
!!!!!!!!!!!!!!!!!!!!!!!!!
0.00031979999994291575
!!!!!!!!!!!!!!!!!!!!!!!!!
0.000708900000063295
!!!!!!!!!!!!!!!!!!!!!!!!!
0.0002934000003733672
"""


"""
Из выходных данных выше видно, что при реверсе числа операции с числами 
производяться медленее. Самые быстрые функции это встроенная функция реверса 
строки и реверс с помощью среза строки. Самая медленная - рекурсия.
"""
