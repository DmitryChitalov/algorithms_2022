"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
####################################################################
from timeit import timeit
from cProfile import run


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


def revers_4(num_1, num_2=""):
    while num_1 < 10:
        return num_2 + str(num_1)
    else:
        return revers_4(num_1=num_1 // 10, num_2=num_2 + str(num_1 % 10))


def revers_5(num_1, num_2=""):
    while num_1 > 10:
        num_2 = num_2 + str(num_1 % 10)
        num_1 = num_1 // 10

    else:
        return num_2 + str(num_1)

def main(num):
    revers(num)
    revers_2(num)
    revers_3(num)
    revers_4(num)


n = 12390
print(revers(n))
print(revers_2(n))
print(revers_3(n))
print(revers_4(n))
print(revers_5(n))
print('1239 % 10=', 1239 % 10)

print(revers.__name__, timeit("revers(n)", globals=globals(), number=1000))
print(revers_2.__name__, timeit("revers_2(n)", globals=globals(), number=1000))
print(revers_3.__name__, timeit("revers_3(n)", globals=globals(), number=1000))
print(revers_4.__name__, timeit("revers_3(n)", globals=globals(), number=1000))
print(revers_5.__name__, timeit("revers_3(n)", globals=globals(), number=1000))

run('main(n)')

"""
Аналитика:
Самые быстрые программы revers_3, revers_4, revers_5. Так как в них  применяется строковый метод,
в отличии от других(используются математические операции).
"""
