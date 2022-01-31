"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
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


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def revers_4(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_4(enter_num, revers_num)


if __name__ == '__main__':
    import timeit

    # revers(123456)
    # revers_2(123456)
    # revers_3(123456)
    # revers_4(123456)

    t = timeit.Timer(lambda: revers(123456))
    print(t.repeat(3))
    t = timeit.Timer(lambda: revers_2(123456))
    print(t.repeat(3))
    t = timeit.Timer(lambda: revers_3(123456))
    print(t.repeat(3))
    t = timeit.Timer(lambda: revers_4(123456))
    print(t.repeat(3))

# Вариант первый с рекурсией выполняется дольше других (факториальная сложность).
# Самый быстрый варинт из трех представленных - третий с реверсом строки.
# Четверный вариант c мемоизацией рекурсии оказывается выйгрышным
# за счет сокращения числа рекурсивных вызовов.
