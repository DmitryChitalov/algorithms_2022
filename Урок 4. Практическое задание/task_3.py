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


def revers_4(enter_num):
    revers_num = ''.join(reversed(str(enter_num)))
    return revers_num


print(timeit("revers(12345678901234567890)", setup="from __main__ import revers", number=10000))
# Самый медленный способ - рекурсия. Вызов самой функции из себя потребляет много ресурсов.
# В данном случае прироста производительности при использовании рекурсии нет.
print(timeit("revers_2(12345678901234567890)", setup="from __main__ import revers_2", number=10000))
#  Цикл while оказался быстрее почти в два раза. Одно число уменьшаем - второе создаем.
print(timeit("revers_3(12345678901234567890)", setup="from __main__ import revers_3", number=10000))
# Здесь с числом работают, как со строкой. Используются встроенные функции.
# Это самый быстрый способ. Он бвстрее рекурсии почти в 20 раз.
# Создается новая строка через срез с конца первой строки шагом 1.
print(timeit("revers_4(12345678901234567890)", setup="from __main__ import revers_4", number=10000))
# Чуть медленнее, чем срез (в 2 раза).Разница связано с компилированием кода.
# Более читаемый код. Оптимизация кода не вссегда улучшает его работу.
# reversed() - возвращает итерратор, который выдает символы с конца строки.
# .join() - соединяет символы в строку.
# Почти в 8 раз быстрее рекурсии.
