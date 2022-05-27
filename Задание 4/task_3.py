"""
Задание 3.
Приведен код, формирующий из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit

def revers(enter_num, revers_num=0):
    if enter_num == 0:
# так не работает
#        return
# надо так
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
# так не работает
#        revers(enter_num, revers_num)
# надо так
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

def revers_4(value, res=''):
    if value == 0:
        if res == '':
            res = '0'
        return res
    else:
        return revers_4(value//10, res + str(value%10))


n = 1234567890
print(revers(n))
print(revers_2(n))
print(revers_3(n))
print(revers_4(n))

print(f'revers: время = {timeit("revers(n)", globals=globals())}')
print(f'revers_2: время = {timeit("revers_2(n)", globals=globals())}')
print(f'revers_3: время = {timeit("revers_3(n)", globals=globals())}')
print(f'revers_4: время = {timeit("revers_4(n)", globals=globals())}')

'''
Варианты с циклом эффективнее вариантов с рекурсией потому, что на вызов функции требуется дополнительное время.
В варианте 3 цикл спрятан внутри средств интерпретатора где он реализован наиболее эффективно.
В варианте 2 цикл реализован средствами интерпретатора, поэтому работает медленнее.
'''