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


# Рекурсия решается дольше всех
# 0.21323430000000002
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


# цикл решается тоже долго по сравнению с другим функциями
# 0.1554895
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# срез самое быстрое решение. потому что встроенный функционал. Ничего высчитывать не нужно
# 0.050080800000000036
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# решение при помощи встроенной функции достаточно быстро
# 0.10874970000000006
def revers_4(enter_num):
    revers_num = ''.join(reversed(str(enter_num)))
    return int(revers_num)


numbers = 1350679

print(timeit('revers(numbers)', globals=globals(), number=100000))
print(timeit('revers_2(numbers)', globals=globals(), number=100000))
print(timeit('revers_3(numbers)', globals=globals(), number=100000))
print(timeit('revers_4(numbers)', globals=globals(), number=100000))