"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


from timeit import Timer

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

def revers_4(a):
    if a // 10 == 0:
        return a
    else:
        return str(a % 10) + str(revers_4(a // 10)) 


t1 = Timer(stmt= "revers(348650)", setup="from __main__ import revers")
print(t1.timeit())

t2 = Timer(stmt= "revers_2(348650)", setup="from __main__ import revers_2")
print(t2.timeit())

t3 = Timer(stmt= "revers_3(348650)", setup="from __main__ import revers_3")
print(t3.timeit())

t4 = Timer(stmt= "revers_4(348650)", setup="from __main__ import revers_4")
print(t4.timeit())

#По времени хуже всех работают рекурсии
#Чуть лучше работает цикл
#Самый быстрый вариант - revers_3. Т.е. чем меньше операций и чем они проще, тем функция работает быстрее
