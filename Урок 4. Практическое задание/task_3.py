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
test_num = 123456


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


def revers_4(num):
    num = str(num)
    r_num = ''
    for i in range(len(num) - 1, -1, -1):
        r_num += num[i]
    return r_num


def revers_5(num):
    revers_num = ''.join(sorted(str(num), reverse=True))
    return revers_num


print(timeit("revers(test_num)", globals=globals(), number=10000))
print(timeit("revers_2(test_num)", globals=globals(), number=10000))
print(timeit("revers_3(test_num)", globals=globals(), number=10000))
print(timeit("revers_4(test_num)", globals=globals(), number=10000))
print(timeit("revers_5(test_num)", globals=globals(), number=10000))

"""
Вывод: наиболее быстрым способом является фунция 3 - использование среза. Т.к. в этом случае нам не приходится делать
дополнительные вычисления, использовать перебор элементов в цикле или прибегать к рекурсии.

Самая затратная по времени функция - с использованием рекурсии. Цикл while в данном случае работает медленнее 
чем цикл for, решение с помощью join медленнее решения с помощью срезов, т.к. создается еще и спиок с 
обратной сортировкой.
"""
