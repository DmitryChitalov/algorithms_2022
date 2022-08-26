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
    my_list = [i for i in str(enter_num)]
    my_list.reverse()
    my_list = ''.join(my_list)
    return my_list



enter_num = int(input("Num - "))
print(timeit.timeit('revers(enter_num)', number=10000, globals=globals()))
print(timeit.timeit('revers_2(enter_num)', number=10000, globals=globals()))
print(timeit.timeit('revers_3(enter_num)', number=10000, globals=globals()))
print(timeit.timeit('revers_4(enter_num)', number=10000, globals=globals()))

# Встроенные методы предсказуемо быстрее цикла и рекурсии.
# Ну а наиболее эффективный способ показыыают замеры времени (срез)
