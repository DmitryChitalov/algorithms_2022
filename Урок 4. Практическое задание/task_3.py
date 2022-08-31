"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


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
    return ''.join(reversed(str(enter_num)))


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print(timeit("revers(num_100)", globals=globals(), number=1000))
print(timeit("revers_2(num_100)", globals=globals(), number=1000))
print(timeit("revers_3(num_100)", globals=globals(), number=1000))
print(timeit("revers_4(num_100)", globals=globals(), number=1000))

"""
    revers   0.0015156999999999948 рекурсия самый медленный способ из-за многократного вызова функции внутри себя 
    
    revers_2 0.0009806999999999871 цикл быстрее рекурсии
    
    revers_3 0.0003384000000000026 самый быстрый способ, число разворачиватся как строка через срез, не используются 
    арифметические операции
    
    revers_4 0.0005999000000000004 мой варинат, разворот через reversed, быстрее цикла и рекурсии, но уступает
    по скорости развороту через срез
"""
