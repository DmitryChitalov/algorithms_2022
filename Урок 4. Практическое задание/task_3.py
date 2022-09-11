"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
import timeit

mycode = """
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
"""

mycode2 = """
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num
"""

mycode3 = """
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
"""

mycode4 = """
def revers_4(enter_num):
    num = list(enter_num)
    num.reverse()
    num2 = "".join(num)
    return num2
"""

print(timeit.timeit(setup='', stmt=mycode, number=10000))
print(timeit.timeit(setup='', stmt=mycode2, number=10000))
print(timeit.timeit(setup='', stmt=mycode3, number=10000))
print(timeit.timeit(setup='', stmt=mycode4, number=10000))

"""
Вариант 3 - 4 работают лучше всех остальных так как используют только встроенные методы python. 
"""
