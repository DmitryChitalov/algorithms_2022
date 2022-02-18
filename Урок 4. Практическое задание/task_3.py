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

res_bulitin = timeit('''
digit = 6456486
def revers_4(digit):
    return ''.join(reversed(list(str(digit))))
''', number=10000)

print(f'получение обратных чисел:\nрекурсивное {res_recurs}\n\
цикл while {res_while}\nсрез {res_slice}\n\
через встроенную {res_bulitin}')
'''
цикл while самый быстрый т.к. в нем есть только деление
рекурсивная самая долгая из за использования стека и многократного вызова самой себя
срез и через встроенные функции работают дольше т.к. в них 
производиться перевод в str и в list
'''