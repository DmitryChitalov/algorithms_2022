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
    enter_num = str(enter_num)
    return "".join(reversed(enter_num))


number = 123456789

print(timeit('revers(number)', globals=globals()))
print(timeit('revers_2(number)', globals=globals()))
print(timeit('revers_3(number)', globals=globals()))
print(timeit('revers_4(number)', globals=globals()))

'''
Вывод.
Быстрее всего работает функция 3, переворачивающая строку по срезу. 
Встроенные строковые функции работают быстрее, их сложность - О(1). 
В функциях 3 и 4 не используются итерация и рекурсия, это также делает их быстрее. 
У рекурсивной функции факториальная сложность, она работает медленнее всех.
'''