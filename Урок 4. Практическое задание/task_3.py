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
    revers_num = str(enter_num % 10)
    remain = enter_num // 10
    while remain:
        revers_num += str(remain % 10)
        remain //= 10
    return revers_num



setup = 'from __main__ import '
num = 12345678912345456789876543


print(timeit('revers(num)', setup=setup+'revers, num'))
print(timeit('revers_2(num)', setup=setup+'revers_2, num'))
print(timeit('revers_3(num)', setup=setup+'revers_3, num'))
print(timeit('revers_4(num)', setup=setup+'revers_4, num'))


"""
Оценка алгоритмов по О-нотации:
                    revers(num) - O(n!)
                    revers2(num) - O(n)
                    revers3(num) - O(1)
                    revers4(num) - O(n)

Время выполнеия алгоритмов по timeit:
                    revers(num) - 14.5439271
                    revers_2(num) - 10.5535552
                    revers_3(num) - 1.7193533999999993
                    revers_4(num) - 17.525256900000002

Вывод:
        Самый эффективный алгоритм - revers_3(num)
        По оценке сложности в О-нотации n(1)
        По оценке времени выполнения также дал лучший результат.
        
        "Также интересно, что мой алгоритм, который по О-нотации
        o(n) дает почти такой же результат по времени выполнения,
        что и рекурсия"
"""