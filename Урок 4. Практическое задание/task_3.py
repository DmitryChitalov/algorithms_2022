"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
import timeit
from random import randint

num_100 = randint(10000, 1000000)
print(num_100)


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
    revers_num = "".join(reversed(str(enter_num)))
    return revers_num


def revers_5(enter_num):
    enter_num = list(str(enter_num))
    enter_num.reverse()
    return enter_num


count_revers_1 = timeit.timeit('revers(num_100)', setup='from __main__ import revers, num_100')
count_revers_2 = timeit.timeit('revers_2(num_100)', setup='from __main__ import revers_2, num_100')
count_revers_3 = timeit.timeit('revers_3(num_100)', setup='from __main__ import revers_3, num_100')
count_revers_4 = timeit.timeit('revers_4(num_100)', setup='from __main__ import revers_4, num_100')
count_revers_5 = timeit.timeit('revers_5(num_100)', setup='from __main__ import revers_5, num_100')

print(count_revers_1, "Результат 1 функции, ( Рекурсия )")
print(count_revers_2, "Результат 2 функции ( Цикл )")
print(count_revers_3, "Результат 3 функции ( Срез )")
print(count_revers_4, "Результат 4 функции ( Метод reversed ) ")
print(count_revers_5, "Результат 5 функции ( Метод reversed ) ")

# Аналитика
# Замеры
# 2.6654694001190364 Результат 1 функции, ( Рекурсия )
# 1.5351632996462286 Результат 2 функции ( Цикл )
# 0.41732339980080724 Результат 3 функции ( Срез )
# 0.8223231001757085 Результат 4 функции ( Метод reversed )
# 0.5860704998485744 Результат 5 функции ( Метод reversed )

# Написал дополнительно 2 функции reverse
# в пятой функции получилось улучшить время выполнения за счет встроеных методов, но догнать время выполнения
# в функции со срезами не удалось, хотя функции выполняются в константной сложности,
# единственное приемлимое объяснение которое смог найти, метод среза написан на языке программирования С
