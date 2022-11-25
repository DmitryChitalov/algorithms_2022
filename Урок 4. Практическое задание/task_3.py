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
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return int(revers_num)

def revers_4(number):
    return int(''.join(reversed(str(number))))

if __name__ == "__main__":
    number = 123456789

    print(timeit("revers(number)", number=1000, globals=globals()))
    print(timeit("revers_2(number)", number=1000, globals=globals()))
    print(timeit("revers_3(number)", number=1000, globals=globals()))
    print(timeit("revers_4(number)", number=1000, globals=globals()))

    # Быстрее выолняется функция revers_3, т.к. в ней выполняется наименьшее количество операций.
    # Функция revers_1 фыполняется дольше всего из-за вызова рекурсии.