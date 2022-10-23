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
from random import randint


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
    enter_num = str(enter_num)
    return ''.join([enter_num[i] for i in range(len(enter_num)-1, -1, -1)])


some_num = randint(100000, 100000000)
print('Исходное число: ', some_num)

print('Рекурсия')
print(revers_1(some_num))
print(timeit(f'revers_1({some_num})', globals=globals()))

print('Цикл')
print(revers_2(some_num))
print(timeit(f'revers_2({some_num})', globals=globals()))

print('Срезы')
print(revers_3(some_num))
print(timeit(f'revers_3({some_num})', globals=globals()))

print('Свой вариант')
print(revers_4(some_num))
print(timeit(f'revers_4({some_num})', globals=globals()))

'''
Исходное число:  73269167
Рекурсия
76196237.0
1.1529932000012195
Цикл
76196237.0
0.7744634000009682
Срезы
76196237
0.19076750000022002
Мой вариант
76196237
0.6714653999988514

Process finished with exit code 0

Вывод: Рекурсия - самая медленная по исполнению функция из-за наличия арифметических операций.
Также циклы и моя созданная функция  одни из медленных функций (наличие перебора).
Самая быстрая функция тут срезы, так как тут только работа с числом как со строкой
'''
