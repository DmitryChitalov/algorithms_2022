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
    revers_num = ""
    for c in str(enter_num):
        revers_num = c + revers_num
    return revers_num
enter_num = int(input('Введите число : '))
revers(enter_num)
revers_2(enter_num)
revers_3(enter_num)
revers_4(enter_num)


print("Время выполнения функции 1 = ", timeit('revers(enter_num)', globals=globals(), number=1000000))
print("Время выполнения функции 2 = ", timeit('revers_2(enter_num)', globals=globals(), number=1000000))
print("Время выполнения функции 3 = ", timeit('revers_3(enter_num)', globals=globals(), number=1000000))
print("Время выполнения функции 4 = ", timeit('revers_4(enter_num)', globals=globals(), number=1000000))


# Время выполнения функции 1 =  2.0343661
# Время выполнения функции 2 =  1.3790718000000002
# Время выполнения функции 3 =  0.27297239999999956
# Время выполнения функции 4 =  0.8336699999999997

#  Самая эффективная функция 3, которая использует срез