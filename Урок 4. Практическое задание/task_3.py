"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
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
    res = ''
    for i in str(enter_num):
        res = i + res
    return res


def revers_5(enter_num):
    res = []
    for i in range(len(str(enter_num)) - 1, -1, -1):
        res.append(str(enter_num)[i])
    res = ''.join(res)
    return res



print(revers(enter_num))
print(revers_2(enter_num))
print(revers_3(enter_num))
print(revers_4(enter_num))
print(revers_5(enter_num))





print(timeit("revers(enter_num, revers_num=0)", globals=globals(), number=1000))
print(timeit("revers_2(enter_num, revers_num=0)", globals=globals(), number=1000))
print(timeit("revers_3(enter_num)", globals=globals(), number=1000))
print(timeit("revers_4(enter_num)", globals=globals(), number=1000))
print(timeit("revers_5(enter_num)", globals=globals(), number=1000))


# время выполнения revers  - 0.0012499000000000017
# время выполнения revers_2 - 0.0007715999999999973
# время выполнения revers_3 - 0.00022719999999999685
# время выполнения revers_4 - 0.0005409000000000004
# время выполнения revers_5 - 0.0018789999999999987
# наиболее эффективный алгоритм revers_3, в котором используется срез






