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
    enter_num = str(enter_num)
    res = ''.join(reversed(enter_num))
    return res


num1 = 234
num2 = 435668232
num3 = 135464677858524

print(f'Функция-рекурсия')
print(timeit("revers(num1)", "from __main__ import revers, num1", number=1000))
print(timeit("revers(num2)", "from __main__ import revers, num2", number=1000))
print(timeit("revers(num3)", "from __main__ import revers, num3", number=1000))

print(f'Функция с циклом while')
print(timeit("revers_2(num1)", "from __main__ import revers_2, num1", number=1000))
print(timeit("revers_2(num2)", "from __main__ import revers_2, num2", number=1000))
print(timeit("revers_2(num3)", "from __main__ import revers_2, num3", number=1000))

print(f'Функция с использованием среза')
print(timeit("revers_3(num1)", "from __main__ import revers_3, num1", number=1000))
print(timeit("revers_3(num2)", "from __main__ import revers_3, num2", number=1000))
print(timeit("revers_3(num3)", "from __main__ import revers_3, num3", number=1000))

print(f'Функция с переворотом строки')
print(timeit("revers_4(num1)", "from __main__ import revers_4, num1", number=1000))
print(timeit("revers_4(num2)", "from __main__ import revers_4, num2", number=1000))
print(timeit("revers_4(num3)", "from __main__ import revers_4, num3", number=1000))

# Аналитика показала, что функция с использованием среза выполняется быстрее,
# самая медленная по времени функция с рекурсией причём скорость выполнения падает по мере того
# как растёт длина вводимого числа
# функция с переворотом строки также показала себя не плохо, выполняется довольно быстро
