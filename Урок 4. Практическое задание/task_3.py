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


def my_def(num, renum=str()):
    num = str(num)
    if len(num) == 0:
        return renum
    else:
        num = int(num)
        number = num % 10
        number = str(number)
        renum += number
        num = str(num)
        num = num[:-1]
        return my_def(num, renum)


# def my_def2():
#     try:
#         num1 = int(input('Введите число, которое требуется перевернуть: '))
#         print('Перевернутое число: ', my_def(num1))
#     except ValueError:
#         print('Не верный ввод, попробуйте еще раз')
#         return my_def2()
"""
Тут и без замеров было понятно, что быстрее вариант - 3.
Нет циклов, нет условий.
Приравнивание к строке и ее реверс. O(1)






Первый вариант.
0.0008751999703235924

Второй вариант.
0.0005861999816261232

Третий вариант.
0.00022149999858811498

Четвертый вариант.
0.002626099972985685

"""

NUMM = 12345


print(timeit("revers(NUMM)", globals=globals(), number=1000))
print(timeit("revers_2(NUMM)", globals=globals(), number=1000))
print(timeit("revers_3(NUMM)", globals=globals(), number=1000))
print(timeit("my_def(NUMM)", globals=globals(), number=1000))
