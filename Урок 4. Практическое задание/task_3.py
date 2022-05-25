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
    if enter_num == 0:
        return ""
    return f'{str(enter_num % 10)}{revers_4(enter_num // 10)}'


test_num = 1234567890

print('revers_1: ', timeit("revers_1(test_num)", globals=globals(), number=1000))
print('revers_2: ', timeit("revers_2(test_num)", globals=globals(), number=1000))
print('revers_3: ', timeit("revers_3(test_num)", globals=globals(), number=1000))
print('revers_4: ', timeit("revers_4(test_num)", globals=globals(), number=1000))

"""
Проситься добавить вариант решения данной задачи через классическую рекуссию (revers_4): красиво, элегантрно, и наиболие
ресурсоемко, отдаем четвертое место. На третьем месте распологается  вариант 1 (reverse_1) - рекуссия, но 
"в одну сторону", в почти 2 раза быстрее варианта 4. Второе место нашего хитпарада - вариант 2 (reverse_2): классический
цикл, достаточно быстр, прост для понимания, в общем наше все. И наконец, первое место! Вариант номер 3 (reverse_3)
С огромным разрывом, лаконичностью кода, и спользованием встроенных функций (взятие среза) , и, злые языки поговаривают,
на стероида усиленных С (но это не точно) одерживает заслуженную победу!
Мои результаты замеров времени:
revers_1:  0.0017760000191628933
revers_2:  0.001097199972718954
revers_3:  0.00024200009647756815
revers_4:  0.003987699979916215

 """