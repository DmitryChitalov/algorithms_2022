"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!

Listing измерений времени приложен после кода скрипта.

Свой вариант:
- перевел число в строку,
- в цикле выбрал значения строки с str[len] до элемента str[0]
- полученные символы добавил в новую строку.

вывод о производительности:
revers_3  строка и рекурсивная выборка метолом среза           > 0.202 sec - самый производительный
revers_2  в цикле перенести элементы по одному из
          enter_num в reverse_num действиями математики       > 0.534 sec  - менее производительный
revers_4  строка и рекурсивная выборка в цикле по индексу     > 0.632 sec  - менее производительный
revers    методим рекурсии  перенести элементы по одному из
          enter_num в reverse_num действиями математики       > 0.886 sec -  наименее производительный



"""

from timeit import timeit


def revers(enter_num, revers_num=0):

    if enter_num == 0:
        # print(revers_num)
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    pass
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
    enter_num=str(enter_num)
    reverse_num = ''
    for i in range(len(enter_num), 0 , -1):
        reverse_num += enter_num[i-1]
    return reverse_num




if __name__ == '__main__':

    n = 123456
    # revers(123)
    # print(revers_2(123))
    # print(revers_3(123))
    # print(revers_4(123))
    print('\n --- timings of execution : ----')
    print(f'revers   > {timeit("revers(n)", globals=globals())} sec')
    print(f'revers_2 > {timeit("revers_2(n)", globals=globals())} sec')
    print(f'revers_3 > {timeit("revers_3(n)", globals=globals())} sec')
    print(f'revers_4 > {timeit("revers_4(n)", globals=globals())} sec')

# Scrept listing:
#
#  --- timings of execution : ----
# revers   > 0.8861287 sec
# revers_2 > 0.5341884 sec
# revers_3 > 0.20278189999999996 sec
# revers_4 > 0.6320889000000001 sec
#
# Process finished with exit code 0
