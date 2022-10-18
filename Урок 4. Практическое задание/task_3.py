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


print(timeit("revers(1055783)", globals=globals(), number=1000000))
print(timeit("revers_2(1055783)", globals=globals(), number=1000000))
print(timeit("revers_3(1055783)", globals=globals(), number=1000000))


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


print(timeit("revers_4(1055783)", globals=globals(), number=1000000))

# Время выполнения кода 1) 2.2619043000158854
# Время выполнения кода 2) 1.4786285000154749
# Время выполнения кода 3) 0.33130009996239096
# Время выполнения кода 4) 0.6411944000283256
# Мы видим, что срез отрабатывает быстрее, моё решение не намного уступает срезу
# Из-за меньшего количества операций и меньшего количества объявления переменных
# Первые два решения не очень хорошо оптимизированы
