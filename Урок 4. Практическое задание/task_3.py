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

numbers = 123456789

# Самый медленный вариант ~ 0,17 сек

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

# Средний вариант по длительности ~ 0,11 сек

def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

# Самый быстрый из трех вариантов при помоще среза ~ 0,02 сек

def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

# Вариант 4 при помощи reversed. Третий по скорости из четырех ~ 0,06 сек, но зато самый компактный и элегантный.

def revers_4(enter_num):
    revers_num = ''.join(reversed(str(enter_num)))
    return int(revers_num)

# Вариант 5 через цикл for. ~ 0,08 сек.

def revers_5(enter_num):
    reversed_lst = ''
    for i in str(enter_num):
        reversed_lst = i + reversed_lst
    return int(reversed_lst)


print(timeit('revers(numbers)', globals=globals(), number=100000))
print(timeit('revers_2(numbers)', globals=globals(), number=100000))
print(timeit('revers_3(numbers)', globals=globals(), number=100000))
print(timeit('revers_4(numbers)', globals=globals(), number=100000))
print(timeit('revers_5(numbers)', globals=globals(), number=100000))