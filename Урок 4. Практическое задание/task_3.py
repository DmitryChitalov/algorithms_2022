"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit, default_timer, Timer


n = 512378


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        #enter_num //= 10
        return revers(enter_num // 10, revers_num)



print(revers(n))


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

print(revers_2(n))

def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

print(revers_3(n))


def revers_4(enter_num):
    return str(enter_num) if enter_num < 10 else str(enter_num % 10) + revers_4(enter_num // 10)

print(revers_4(n))


def revers_5(enter_num, revers_num=0):
    for i in range(len(str(enter_num))):
        num = int(enter_num) % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print(revers_5(n))


#t1 = timeit('revers(n)', globals=globals(), number=5000)
#t2 = timeit('revers_2(n)', globals=globals(), number=5000)
#t3 = timeit('revers_3(n)', globals=globals(), number=5000)
print(f'функция {revers.__name__} отработала за', timeit('revers(n)', globals=globals() , number=10000), 'сек.')
print(f'функция {revers_2.__name__} отработала за', timeit('revers_2(n)', globals=globals(), number=10000), 'сек.')
print(f'функция {revers_3.__name__} отработала за', timeit('revers_3(n)', globals=globals(), number=10000),  'сек.')
print(f'функция {revers_4.__name__} отработала за', timeit('revers_4(n)', globals=globals(), number=10000), 'сек.')
print(f'функция {revers_5.__name__} отработала за', timeit('revers_5(n)', globals=globals(), number=10000), 'сек.')

"""функция revers отработала за 0.08397269999999998 сек.
функция revers_2 отработала за 0.05475260000000004 сек.
функция revers_3 отработала за 0.018810099999999996 сек.
функция revers_4 отработала за 0.09747109999999998 сек.
функция revers_5 отработала за 0.09952729999999999 сек.

Функция reverse_3 с переворотом строки с пмощью среза отработала быстрее всех т.к. имеет константную сложность"""