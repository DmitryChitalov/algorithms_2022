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


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


def revers_5(enter_num):
    revers_num = ''
    for i in reversed(str(enter_num)):
        revers_num += i
    return revers_num


n = 123456789

print('Рекурсия: ', timeit("revers_1(n)", globals=globals(), number=10000))
print('Цикл:     ', timeit("revers_2(n)", globals=globals(), number=10000))
print('Срез:     ', timeit("revers_3(n)", globals=globals(), number=10000))
print('Реверс:   ', timeit("revers_4(n)", globals=globals(), number=10000))
print('Реверс:   ', timeit("revers_5(n)", globals=globals(), number=10000))

"""
Рекурсия:  0.01540290005505085
Цикл:      0.010470599867403507
Срез:      0.002346599940210581
Реверс:    0.0045217000879347324
Реверс:    0.006499399896711111

Очевидно, самый быстрый вариант - срез. Фактически операция в одно действие.
Встроенные методы строки работают быстрее чем штатная функция reversed()
или классический перебор циклом.
Вариант через рекурсию, её стеком вызовов, самый медленный
"""
