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


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


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
    res = ''.join(reversed(str(enter_num)))
    return res


if __name__ == '__main__':
    number = 34567891250
    print(revers_2(number))
    print(revers_3(number))
    print(revers_4(number))
    print('')
    print('revers_1', timeit('revers_1(number)', globals=globals(), number=100000))
    print('revers_2', timeit('revers_2(number)', globals=globals(), number=100000))
    print('revers_3', timeit('revers_3(number)', globals=globals(), number=100000))
    print('revers_4', timeit('revers_4(number)', globals=globals(), number=100000))

    """
    Результаты замеров:
    revers_1 0.37826460000360385
    revers_2 0.1693929000175558
    revers_3 0.042602600005920976
    revers_4 0.07728179998230189
    
    Самым быстрой получилась функция revers_3, которая реверсирует через срез,
    за ней идет revers_4 использующая встроенную функцию reversed, а самой долгой через реверс,
    при этом и в цикле и в реверсе выполняются арифметические действия.
    Да и из-за вывода реверсного числа ввиде числа, а не строки
    число возвращается вещественным и обрезается последний 0 заданного числа
    Следовательно такую задачу наиболее оптимально выполнять через срез    
    """
