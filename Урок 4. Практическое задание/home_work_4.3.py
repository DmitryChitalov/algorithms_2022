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
    return ''.join(reversed(str(enter_num)))


enter_num = 1234567890

print(
    'число наоборот вариант 1: ',
    timeit(
        f'revers_1({enter_num})',
        globals=globals()))

print(
    'число наоборот вариант 2: ',
    timeit(
        f'revers_2({enter_num})',
        globals=globals()))

print(
    'число наоборот вариант 3: ',
    timeit(
        f'revers_3({enter_num})',
        globals=globals()))

print(
    'число наоборот вариант 4: ',
    timeit(
        f'revers_4({enter_num})',
        globals=globals()))


'''
число наоборот вариант 1:  2.553950806
число наоборот вариант 2:  1.624106935
число наоборот вариант 3:  0.3478793419999997
число наоборот вариант 4:  0.7104314540000001
Вариант 3 оказался самым быстрым.
'''