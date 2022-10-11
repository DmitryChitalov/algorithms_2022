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


def my_revers(enter_num):
    my_list = []
    for el in reversed(str(enter_num)):
        my_list.append(el)
    return ''.join(my_list)


# print(my_list)
# return el


n = 10005000

print(f"Замер revers >>> "
      f"{timeit('revers(n)', globals=globals(), number=105000)}")
# Замер revers >>> 0.27942606600000003
print(f"Замер revers_2 >>> "
      f"{timeit('revers_2(n)', globals=globals(), number=105000)}")
# Замер revers_2 >>> 0.194141034
print(f"Замер revers_3 >>> "
      f"{timeit('revers_3(n)', globals=globals(), number=105000)}")
# Замер revers_3 >>> 0.05625192599999995
print(my_revers(n))
print(f"Замер my_revers >>> "
      f"{timeit('my_revers(n)', globals=globals(), number=105000)}")
# Замер my_revers >>> 0.16085230500000003

"""Проведены исследования времени работы функций предложенных + моя (my_revers).
Замеры времени показали, что наибольшей эффективностью обладает функция со срезом
значений строкового выражения нашего числа. При достаточно длинном числе (8 знаков),
моя реализация с получением значения списка, где лежит наше перевернутое значение, 
была бы на 2 месте. Реверсы же с циклом while, а особенно первая функция с рекурсией
здесь являются наименее эффективными"""
