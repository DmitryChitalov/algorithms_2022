"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


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
    return ''.join(reversed(enter_num))


def revers_5(enter_num):
    enter_num = str(enter_num)
    result = ''
    for i in range(len(enter_num) - 1, -1, -1,):
        result += enter_num[i]

    return result

# 0.006726036001055036  # revers
# 0.00371148100020946  # revers_2
# 0.000649677998808329  # revers_3
# 0.0015882420011621434  # revers_4
# 0.0031632939990231534  # revers_5


"""
Профилировал 5 разных алгоритмов, и пришел к выводу, что самым удачным будет
срез строки в обратном направлении revers_3. За ним моя функция revers_4
использовал встроенную функцию reversed, и склейка join.
Функция revers самая медленная так как используется рекурсия,
что образует стек вызовов.
"""


