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
        return


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


def revers_5(enter_num):
    res = []
    num = str(enter_num)
    for i in range(len(num) - 1, -1, -1):
        res.append(num[i])
    res = ''.join(res)
    return res


enter_num = 1234567890

print(timeit("revers_1(enter_num)", globals=globals(), number=1000))
print(timeit("revers_2(enter_num)", globals=globals(), number=1000))
print(timeit("revers_3(enter_num)", globals=globals(), number=1000))
print(timeit("revers_4(enter_num)", globals=globals(), number=1000))
print(timeit("revers_5(enter_num)", globals=globals(), number=1000))


"""
Самый быстрый спобоб решения с использованием среза revers_3 (0.0002592000000000011), 
и немного больше времени потребуется с использованием встроенной функции reversed: revers_4 (0.0005594000000000016), 
Самый медленный способ с использованием рекурсии revers_1 (0.0019031999999999973), 
остальные варианты имеют среднее значение: revers_2 (0.0011887000000000009), 
                                           revers_5 (0.0010318000000000029)
"""