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
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
        return revers(enter_num, revers_num)


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


# четвертая функция через тернарный оператор
def revers_4(enter_num):
    return str(enter_num) if enter_num < 10 else str(enter_num % 10) + revers_4(enter_num // 10)


enternum = 32144891

print(revers(enternum))
print(revers_2(enternum))
print(revers_3(enternum))
print(revers_4(enternum))

print(timeit("revers(enternum)", "from __main__ import revers, enternum", number=1000))
print(timeit("revers_2(enternum)", "from __main__ import revers_2, enternum", number=1000))
print(timeit("revers_3(enternum)", "from __main__ import revers_3, enternum", number=1000))
print(timeit("revers_4(enternum)", "from __main__ import revers_4, enternum", number=1000))

"""
Время исполнения функции revers = 0.12306139999964216
Время исполнения функции revers_2 = 0.0018924999994851532
Время исполнения функции revers_3 = 0.0004233999998177751
Время исполнения функции revers_3 = 0.0031703999993624166

Самый быстрый способ №3,который достигается при помощи среза,реализован на встроенных функциях. На втором месте по 
производительности способ №2 который реализован через цикл. Хуже всего себя показали рекурсивные функции 
которые вызывают себя сами.
"""