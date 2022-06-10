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
from random import randint


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


def revers_4(digit):
    return str(digit) if digit // 10 == 0 else str(digit-(digit//10)*10) + str(revers_4(digit//10))


if __name__ == "__main__":

    number = randint(10000, 1000000)

    print(timeit("revers(number)", globals=globals(), number=10000))
    print(timeit("revers_2(number)", globals=globals(), number=10000))
    print(timeit("revers_3(number)", globals=globals(), number=10000))
    print(timeit("revers_4(number)", globals=globals(), number=10000))

    """
    Листинг вывода
    0.028029464000155713
    0.019513747000019066
    0.0052310360001683875
    0.03987408000011783
    
    В результате быстрее всех оказалась функция revers_3
    Эффект достигнут за счет того, что:
    - не происходит вычислений;
    - преобразование чисел в строку выполняется стандартной функцией, а 
    значит быстро;
    - формирование инвертированного числа, по сути, просто чтение строки 
    в обратном порядке
    """