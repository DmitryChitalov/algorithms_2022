"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import Timer, timeit


res_recurs = timeit('''
digit = 6456486

def revers(digit, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
''', number=10000000)

res_while = timeit('''
digit = 6456486
def revers_2(digit, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num
''', number=10000000)

res_slice = timeit('''
digit = 6456486
def revers_3(digit):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
''', number=10000000)

res_bulitin = timeit('''
digit = 6456486
def revers_4(digit):
    return ''.join(reversed(str(digit)))
''', number=10000000)

print(f'получение обратных чисел:\nрекурсивное {res_recurs}\n\
цикл while {res_while}\nсрез {res_slice}\n\
через встроенные функции {res_bulitin}')
'''
получение обратных чисел:
рекурсивное 0.8104424530001779
цикл while 0.4668023230005929
срез 0.42643833700003597
через встроенные функции 0.42886248200011323

срез - является самым быстрым
'''