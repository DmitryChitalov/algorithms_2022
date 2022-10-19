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

def revers_join(enter_num):
    return "".join(reversed(str(enter_num)))


print(
    timeit(
        f"revers({num})",
        globals=globals(),
        number=1000
    )
)

print(
    timeit(
        f"revers_2({num})",
        globals=globals(),
        number=1000
    )
)
print(
    timeit(
        f"revers_3({num})",
        globals=globals(),
        number=1000
    )
)
print(
    timeit(
        f"revers_join({num})",
        globals=globals(),
        number=1000
    )
)

'''
Функции при амере показали следующие результаты:
1. revers (рекурсия) 0.004296800005249679
2. revers_2 (цикл) 0.0027350999880582094
3. reverse_3 (срез) 0004332999815233052
4. revers_join (reversed+join) 0.0009071000386029482

самая быстрая функция reverse_3 так как использует встроенные методы, мой вариант оказался чуть медленне
'''