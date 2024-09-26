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
    return ''.join(reversed(str(enter_num)))


num = 528

print(f'Исходное число: {num}')
print(f'Вариант 1: {int(revers(num))} за {timeit("revers(num)", globals=globals(), number=100000)}')  # 0.0839
print(f'Вариант 2: {int(revers_2(num))} за {timeit("revers_2(num)", globals=globals(), number=100000)}')  # 0.0466
print(f'Вариант 3: {revers_3(num)} за {timeit("revers_3(num)", globals=globals(), number=100000)}')  # 0.0266
print(f'Вариант 4: {revers_4(num)} за {timeit("revers_4(num)", globals=globals(), number=100000)}')  # 0.0495
"""
Наиболее эффективно воспользоваться вариантом 3, т.к. это встроенная функция (итерация в обратном порядке),
вариант 4 и 2 сопоставимы, в 4-м варианте задействовано соединение итерируемых элементов и во - 2-м используется цикл,
что несколько увеличивает скорость отработки кода [сложность O(N)], наименее скоростным оказался 1-й метод, т.к.
рекурсия соответствует экспоненциальной (степенной) сложности O(2^N)
"""