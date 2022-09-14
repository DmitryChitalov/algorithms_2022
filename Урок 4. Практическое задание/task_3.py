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
    rev_num = ''
    for i in reversed(str(enter_num)):
        rev_num += i
    return rev_num


nums = 12345
print(timeit('revers(nums)', globals=globals(), number=10000))
print(timeit('revers_2(nums)', globals=globals(), number=10000))
print(timeit('revers_3(nums)', globals=globals(), number=10000))
print(timeit('revers_4(nums)', globals=globals(), number=10000))

"""
Самое эффективное решение через срез revers_3, т.к. строки это проиндексированные элементы,
обращение по индексам работает быстрее чем в цикле переприсваивать
значения переменным и рекурсия со её стеком вызовов
revers = 0.021815399995830376
revers_2 = 0.007605300001159776
revers_3 = 0.0027072000011685304
revers_4 = 0.0062507999973604456
"""
