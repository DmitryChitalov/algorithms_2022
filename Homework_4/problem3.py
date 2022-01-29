from timeit import timeit
from random import randint


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

def reverse(enter_num):
    return ''.join(reversed(str(enter_num)))

n = randint(11, 1000000000)
print(timeit('revers(n)', globals=globals()))           # тут много раз вызывается функция
print(timeit('revers_2(n)', globals=globals()))         # здесь просто цикл
print(timeit('revers_3(n)', globals=globals()))         # здесь строка проходится один раз
print(timeit('reverse(n)', globals=globals()))          # здесь строка проходится дважды
                                                        # всё это видно из замеров