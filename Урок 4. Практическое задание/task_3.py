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
from collections import deque

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
''', number=10000)

res_while = timeit('''
digit = 6456486
def revers_2(digit, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num
''', number=10000)

res_slice = timeit('''
digit = 6456486
def revers_3(digit):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
''', number=10000)

res_decue = timeit('''
digit = 6456486
def revers_4(digit):
    dec = deque()
    digit = str(digit)
    for i in digit:
        dec.appendleft(i)
    return ''.join(dec)
''', number=10000)

print(f'получение обратных чисел:\nрекурсивное {res_recurs}\n\
цикл while {res_while}\nсрез {res_slice}\n\
deque {res_decue}')

'''рекурсивное 0.0008742350000829902
цикл while 0.0004850730001635384
срез 0.00046118199861666653
deque 0.00046681300045747776

Использование рекурсии самое долгое, а остальные примерно равны по времени
т.к. везде используется цикл
'''