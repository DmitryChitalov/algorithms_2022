"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


from timeit import timeit, repeat, default_timer
from random import randint

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
    return int(revers_num)

def revers_4(enter_num):
    enter_num = str(enter_num).split()
    revers_num = []
    for i in range(len(enter_num)):
        revers_num.append(enter_num[-i-1])
    return int(''.join(revers_num))

def revers_4(enter_num):
    enter_num = str(enter_num).split()
    revers_num = []
    for i in range(len(enter_num)):
        revers_num.append(enter_num[-i-1])
    return int(''.join(revers_num))

setup = '''
from random import randint
from __main__ import revers, revers_2, revers_3, revers_4
enter_num = randint(1000000, 10000000)
'''


functions = [
    'revers(enter_num)',
    'revers_2(enter_num)',
    'revers_3(enter_num)',
    'revers_4(enter_num)'
    ]

for func in functions:
    result = repeat(func, setup, default_timer, 3, 1000)
    print(func[:-11])
    print(result)
    print('Берем минимальное число - ' + str(min(result)))

'''
Мои результаты:

revers
[0.0019844199996441603, 0.0019714199988811743, 0.0019768689999182243]
Берем минимальное число - 0.0019714199988811743
revers_2
[0.0013375290000112727, 0.0013235500009614043, 0.0013454100007948]
Берем минимальное число - 0.0013235500009614043
revers_3
[0.0005528599976969417, 0.0005148299969732761, 0.0004843400020035915]
Берем минимальное число - 0.0004843400020035915
revers_4
[0.0010304300012649037, 0.0009301399986725301, 0.0009414599990122952]
Берем минимальное число - 0.000930139998672530

Получается что от самой эффективной функции к наименее эффективной:
revers_3 -> rever_4 -> revers_2 -> revers
'''
