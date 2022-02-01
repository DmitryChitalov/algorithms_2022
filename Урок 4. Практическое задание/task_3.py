"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
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
    return ''.join(reversed(str(enter_num)))


def revers_5(enter_num):
    return str(enter_num)[::-1]


n = 123456


print(timeit("revers(n)", globals=globals()))  # 6.459536847, 5.063969108999999, 4.958731209
print(timeit("revers_2(n)", globals=globals()))  # 3.7303306259999998, 3.165328452, 3.014265441000001
print(timeit("revers_3(n)", globals=globals()))  # 1.126390572, 0.8646630460000004, 0.852792968000001
print(timeit("revers_4(n)", globals=globals()))  # 2.1394708530000006, 1.4860853449999993, 1.494103549
print(timeit("revers_5(n)", globals=globals()))  # 1.0158344340000003, 0.8166117049999997, 0.7312809710000003

# Из трех функции, самой быстрой по исолнению является revers_3(n), так как срезы работают быстрей.
# Мной предложены два варианта: функция revers_4(n) и revers_5(n).
# Функция revers_4(n) со встроенной функцией sorted работает чуть медленнее, чем revers_3(n), но быстрей revers(n) и
# revers_2(n). Её работа оптимальней из-за использования встроенной функции reversed, однако операция .join
# забирает какое-то количество времени.
# Функция revers_5(n) (1 предложенный) является доработкой самой быстрого варианта решения revers_3(n), что позволило
# еще немного оптимизировать время выполнения.
