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
        print(revers_num)
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
    print(revers_num)
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num, result=''):  # свой вариант, по факту оптимизированная первая так как тоже через рекурсию
    if enter_num == 0:
        return result
    else:
        result += str(enter_num % 10)
    revers_4(enter_num // 10, result)


print(f'Время выполнения функции revers: {timeit("revers", "from __main__ import revers", number=10000)}')
print(f'Замер времени функции revers_2: {timeit("revers_2", "from __main__ import revers_2", number=10000)}')
print(f'Замер времени функции revers_3: {timeit("revers_3", "from __main__ import revers_3", number=10000)}')
print(f'Замер времени функции revers_4: {timeit("revers_4", "from __main__ import revers_4", number=10000)}')

"""
Результаты 5 замеров:
Время выполнения функции revers: 8.260000000000212e-05
Замер времени функции revers_2: 8.249999999999924e-05
Замер времени функции revers_3: 8.249999999999924e-05
Замер времени функции revers_4: 8.249999999999924e-05

Время выполнения функции revers: 9.019999999999861e-05
Замер времени функции revers_2: 9.009999999999574e-05
Замер времени функции revers_3: 8.99999999999998e-05
Замер времени функции revers_4: 8.99999999999998e-05

Время выполнения функции revers: 8.260000000000212e-05
Замер времени функции revers_2: 8.260000000000212e-05
Замер времени функции revers_3: 8.249999999999924e-05
Замер времени функции revers_4: 9.889999999999899e-05

Время выполнения функции revers: 8.270000000000499e-05
Замер времени функции revers_2: 8.260000000000212e-05
Замер времени функции revers_3: 8.260000000000212e-05
Замер времени функции revers_4: 9.750000000000036e-05

Время выполнения функции revers: 8.260000000000212e-05
Замер времени функции revers_2: 8.260000000000212e-05
Замер времени функции revers_3: 8.260000000000212e-05
Замер времени функции revers_4: 0.00011339999999999961

выводы у меня вообще неоднозначные, тесты показывают одно, но по факту рекурсия и цикл должны работать медленнее среза
буду ждать вашего комментария, или я где-то глобально допускаю ошибку, так как все тесты примерно одинаковые
"""