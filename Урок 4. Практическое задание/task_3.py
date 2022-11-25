"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему!!!
И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
import cProfile
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


num = 123123131

cProfile.run('revers_1(num)')
cProfile.run('revers_2(num)')
cProfile.run('revers_3(num)')

print(f'1 - {timeit("revers_1(num)", "from __main__ import revers_1, num", number=10000)}')
print(f'2 - {timeit("revers_2(num)", "from __main__ import revers_2, num", number=10000)}')
print(f'3 - {timeit("revers_3(num)", "from __main__ import revers_3, num", number=10000)}')


"""
Третья функция самая быстрая, т.к. написана на основе встроенных функций
Вторая немного быстрее первой, т.к. в ней применён цикл.
Первая самая медленная из-за использования рекурсии.
"""