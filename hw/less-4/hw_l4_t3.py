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


def revers_4(enter_num):
    answ = list(map(str, str(enter_num)))
    answ.reverse()
    return ''.join(answ)


print(revers(123456789), timeit("revers(123456789)", globals=globals(), number=10000))
print(revers_2(123456789), timeit("revers_2(123456789)", globals=globals(), number=10000))
print(revers_3(123456789), timeit("revers_3(123456789)", globals=globals(), number=10000))
print(revers_4(123456789), timeit("revers_3(123456789)", globals=globals(), number=10000))


#Две последние функции работают почти одинарово из за схожего процесса выполнения через строки, сложность O(n)