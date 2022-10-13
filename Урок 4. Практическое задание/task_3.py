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


def revers(enter_num, revers_num=0):  # Неверный результат при больших числах
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        revers_num = int((revers_num + num / 10) * 10)
        enter_num //= 10
        revers(enter_num, revers_num)
    return revers(enter_num, revers_num)

def revers_2(enter_num, revers_num=0):  # Неверный результат при больших числах
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        revers_num = int((revers_num + num / 10) * 10)
        enter_num //= 10
    return revers_num

def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num, revers_num=''):
    if enter_num > 0:
        revers_num, enter_num = f'{revers_num}{enter_num % 10}', enter_num // 10
        return revers_4(enter_num, revers_num)
    return revers_num


enter_num = 123456789
print(revers(enter_num))
print(timeit("revers(enter_num)", number=100000, globals=globals()))
print('--------------------')
print(revers_2(enter_num))
print(timeit("revers_2(enter_num)", number=100000, globals=globals()))
print('--------------------')
print(revers_3(enter_num))
print(timeit("revers_3(enter_num)", number=100000, globals=globals()))
print('--------------------')
print(revers_4(enter_num))
print(timeit("revers_4(enter_num)", number=100000, globals=globals()))
print('--------------------')


"""
Функция revers проигрывает остальным за счёт использования в ней рекурсии.
Использование цикла в функции revers_2 даёт определённый выигрыш во времени.
Лидирует функция revers_3 (O(n)), в которой используется встроенная
функция получения среза.
Функция revers_4, собрана из revers и revers_2 и даёт перед ними преимущество
(видимо, за счёт уменьшения использования математических операций).
"""