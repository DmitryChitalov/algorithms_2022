"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


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
    lst_num = []
    for i in reversed(str(enter_num)):
        lst_num.append(i)
    revers_num = ''.join(lst_num)
    return int(revers_num)



print(f'Выполнение revers(enter_num) заняло', timeit(f"revers({enter_num})", globals=globals(), number=10000))
print(f'Выполнение revers_2(enter_num) заняло', timeit(f"revers_2({enter_num})", globals=globals(), number=10000))
print(f'Выполнение revers_3(enter_num) заняло', timeit(f"revers_3({enter_num})", globals=globals(), number=10000))
print(f'Выполнение revers_4(enter_num) заняло', timeit(f"revers_4({enter_num})", globals=globals(), number=10000))

"""
Выполнение revers(enter_num) заняло 0.03495274599999999
Выполнение revers_2(enter_num) заняло 0.025493913000000007
Выполнение revers_3(enter_num) заняло 0.006095046000000007
Выполнение revers_4(enter_num) заняло 0.021465730999999988


В соответствии с полученными результатами можно сделать вывод, что решение с использованием среза наиболее 
эффективно в плане времени. Решения №1,с помощью рекурсии и решение №2 с помощью цикла while используют вычисления,
что замедляет их время выполнения. А решение №3 хоть и использует встроенные функции, но за счет использования
цикла for так же проигрывает по скорости срезу.
Следовательно использование среза в данной задаче является оптимальным..

"""
