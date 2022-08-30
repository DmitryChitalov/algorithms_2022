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


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(revers(35060))
print(timeit('revers(350)', globals=globals(), number=1000000), '\n')

print(revers_2(35060))
print(timeit('revers_2(350)', globals=globals(), number=1000000), '\n')

print(revers_3(35060))
print(timeit('revers_3(350)', globals=globals(), number=1000000), '\n')

#Собственный вариант решения:


def revers_4(enter_num):
    enter_num = str(enter_num)
    emp_list = []
    for x in enter_num:
        emp_list.insert(0, x)
    res_str = ''.join(emp_list)
    return res_str


print(revers_4(35060))
print(timeit('revers_4(350)', globals=globals(), number=1000000))


"""
Не смотря на то, что предложенный вариант решения revers_4 при замерах модулем timeit оказался быстрее функций revers_1 и revers_2,
самой эффективной реализацией является revers_3, т.к использует встроенные функции языка, которые всегда работают быстрее, что подтвержают замеры времени выполнения.
"""