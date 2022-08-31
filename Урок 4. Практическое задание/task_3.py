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


def revers_1(enter_num):
    quotient, remainder = divmod(enter_num, 10)  # частное, остаток
    if not quotient:
        return str(remainder)
    else:
        return str(remainder) + str(revers_1(quotient))


def revers_2(enter_num, revers_num=0):
    lenght = len(str(enter_num))
    while enter_num > 0:
        revers_num = (revers_num * 10 + enter_num % 10)
        enter_num //= 10
    return '0'*(lenght - len(str(revers_num))) + str(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


entered_num = 123456789000
print(f"{entered_num} исходное число")

print(revers_1(entered_num), end=' ')
print('число наоборот - рекурсия: ',
      timeit(stmt='revers_1(entered_num)',
             globals=globals())
      )

print(revers_2(entered_num), end=' ')
print('число наоборот - циклы: ',
      timeit(stmt='revers_2(entered_num)',
             globals=globals()),
      )

print(revers_3(entered_num), end=' ')
print('число наоборот - срез: ',
      timeit(stmt='revers_3(entered_num)',
             globals=globals())
      )

print(revers_4(entered_num), end=' ')
print('число наоборот - функция reversed:',
      timeit(stmt='revers_4(entered_num)',
             globals=globals())
      )
"""
123456789000 исходное число
000987654321 число наоборот - рекурсия:  5.730796788
000987654321 число наоборот - циклы:  2.816176221
000987654321 число наоборот - срез:  0.37233093999999944
000987654321 число наоборот - функция reversed: 0.8058947819999993

Исходя из результата, отсортируем методы в порядке убывания эффективности:
1) срез  -  самая эффективная реализация
2) функция reversed
3) циклы
4) рекурсия
"""