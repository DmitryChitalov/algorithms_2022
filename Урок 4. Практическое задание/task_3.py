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


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return int(revers(enter_num, revers_num))


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return int(revers_num)


def revers_4(enter_num):
    return int(''.join(list(reversed(list(str(num))))))


num = 123456789

print('revers O(n):', timeit('revers(num)', globals=globals(), number=10000))
print('revers_2 O(n)', timeit('revers_2(num)', globals=globals(), number=10000))
print('revers_3 O(1)', timeit('revers_3(num)', globals=globals(), number=10000))
print('revers_4 O(n)', timeit('revers_4(num)', globals=globals(), number=10000))

"""
revers O(n): 0.020020199939608574
revers_2 O(n) 0.011229799943976104
revers_3 O(1) 0.0031787999905645847
revers_4 O(n) 0.0065879999892786145

revers_3 имеет наилучшие результаты замеров времени.
В данном задании можно наблюдать, как О-нотация подтверждается
замерами.
"""
