"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


from timeit import Timer


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


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
    n_list = list(str(enter_num))
    n_list.reverse()
    n2 = "".join(n_list)
    return n2


my_num = 1234567
print(revers_1(my_num))
r1 = Timer(stmt="revers_1(my_num)", setup="from __main__ import revers_1", globals=globals())
print(f"revers_1: Число {my_num}, перевернутое {revers_1(my_num)}, время {r1.timeit(number=10000)} seconds")

r2 = Timer(stmt="revers_2(my_num)", setup="from __main__ import revers_2", globals=globals())
print(f"revers_2: Число {my_num}, перевернутое {int(revers_2(my_num))}, время {r2.timeit(number=10000)} seconds")

r3 = Timer(stmt="revers_3(my_num)", setup="from __main__ import revers_3", globals=globals())
print(f"revers_3: Число {my_num}, перевернутое {int(revers_3(my_num))}, время {r3.timeit(number=10000)} seconds")

r4 = Timer(stmt="revers_4(my_num)", setup="from __main__ import revers_4", globals=globals())
print(f"revers_4: Число {my_num}, перевернутое {revers_4(my_num)}, время {r4.timeit(number=10000)} seconds")

"""
Наиболее эффективной является способ 3 с использованием разворота через срез строки.
В отличие от метода 4 нет необходимости переводить в список и назад собирать в строку.
Рекурсивный метод 1 показал себя самым долгим
"""