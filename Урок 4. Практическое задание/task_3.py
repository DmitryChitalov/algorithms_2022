"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
# ==============================================================================
# === Ответ ====================================================================
# ==============================================================================
# 1) revers самый медленый, потеря времени на математических операциях и 
# рекурсивные вызовы с присваиваниями
# 2) revers_2 на предпоследнем месте по скорости, основаня потеря времени 
# на метематических операциях
# 3) revers_3 самый быстрый способ при числах больше 10000, за счет 
# оптимизированного по скорости выполнения
# обратного среза, которым и реверсируется строка с числом
# 4) revers_3 на втором месте по скорости при числах больше 10000, 
# если числа меньше то на первом месте за счет прерасчитанных данных в словаре
# Результаты замеров randint(10**1, 10**4):
# revers---min time:    0.017670099972747266
# revers_2---min time:  0.01515390002168715
# revers_3---min time:  0.009366999962367117
# revers_4---min time:  0.008621899993158877
# ==============================================================================

from timeit import repeat, default_timer
from random import randint


funcs = []

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return str(int(revers_num))
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)

funcs.append("revers")

# ====================================
def revers_2(enter_num):
    revers_num = 0
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return str(int(revers_num))

funcs.append("revers_2")

# ====================================
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

funcs.append("revers_3")

# ====================================
def revers_4(enter_num, precalculus = {num: str(num)[::-1] for num in range(10**5)}, step = 10**5):
    if enter_num < step:
        return precalculus[enter_num]
    result = ''
    while div_:= enter_num // step:
        result += precalculus[enter_num % step]
        enter_num = div_
    result += precalculus[enter_num]
    return result

funcs.append("revers_4")

for func in funcs:
    print(f'{f"{func}---min time: ":22}'+
          str(min(repeat(f'{func}(randint(10**1, 10**4))', default_timer, globals=globals(), repeat=3, number=10000))))


