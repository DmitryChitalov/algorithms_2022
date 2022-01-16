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
    reversed_str = ''
    if enter_num == 0:
        return reversed_str
    else:
        enter_num = int(enter_num)
        last_num = enter_num % 10
        return str(last_num) + str(revers_4(enter_num // 10))


def revers_5(enter_num):
    reversed_list = []
    for i in reversed(str(enter_num)):
        reversed_list.append(i)
    return ''.join(reversed_list)


num_to_reverse = 147852369
print(revers_5(num_to_reverse))

print(timeit('revers(num_to_reverse)', globals=globals()))
print(timeit('revers_2(num_to_reverse)', globals=globals()))
print(timeit('revers_3(num_to_reverse)', globals=globals()))
print(timeit('revers_4(num_to_reverse)', globals=globals()))
print(timeit('revers_5(num_to_reverse)', globals=globals()))

"""
Замеры времени:
6.6437063
4.3705196
0.9877783999999998
14.0228683
3.412704599999998

Из 5 вариантов решений задачи наиболее эффективным оказывается третий - через срезы, здесь меньше всего выполняемых
операций.
"""
