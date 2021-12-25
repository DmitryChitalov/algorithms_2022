"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from timeit import timeit

NUMBER = 1230


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


def my_revers_slice(number):
    return str(number % 10)[::-1]


# def my_revers_reversed(number):
#     return reversed(str(number % 10))


"""
Самый быстрый вариант - мною предложенный, так как по сравнению с 3 вариантом не создаются переменные,
на которые тоже тратится время, хоть и незначительное.
Первый вариант - рекурсия - самый медленный
Второй - цикл - быстрее рекурсии
Третий - преобразование числа в строку и развёрнутый срез
Мой - такой же как и третий, но без переменных
Пробовал с функцией reversed, но разницы со срезом практически нет, и порой кто-то из них быстрее оказывается. 
"""
if __name__ == '__main__':
    revers(NUMBER)
    revers_2(NUMBER)
    revers_3(NUMBER)
    my_revers_slice(NUMBER)
    # my_revers_reversed(NUMBER)
    print(timeit("revers(NUMBER)", globals=globals()))
    print(timeit("revers_2(NUMBER)", globals=globals()))
    print(timeit("revers_3(NUMBER)", globals=globals()))
    print(timeit("my_revers_slice(NUMBER)", globals=globals()))
    # print(timeit("my_revers_reversed(NUMBER)", globals=globals()))
