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

# Срез строки самый быстрый способ, константная сложность
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

# В данном случае эффективность за счет использования встроенных функций
def revers_4(enter_num):
    my_list = list(str(enter_num))
    my_list.reverse()
    revers_num = "".join(my_list)
    return revers_num


num = 234567
print(timeit("revers(num,0)", globals=globals()))  # ->1.7128545000450686
print(timeit("revers_2(num,0)", globals=globals()))  # ->1.0515017999568954
print(timeit("revers_3(num)", globals=globals()))  # ->0.2843368999892846
print(timeit("revers_4(num)", globals=globals()))  # ->0.5510705000488088
