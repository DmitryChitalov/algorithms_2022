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


def revers_4(enter_num):
    a = reversed(str(enter_num))
    b = ''.join(a)
    return b

num = 123456789
print(timeit("revers(num)", globals=globals(), number=10000))
print(timeit("revers_2(num)", globals=globals(), number=10000))
print(timeit("revers_3(num)", globals=globals(), number=10000))
print(timeit("revers_4(num)", globals=globals(), number=10000))

'''
0.02576869999999999
0.017098699999999994
0.0035135999999999917
0.008464299999999994
Две последние функции выполняются быстрее, так как нет циклов и рекурсий!
Но revers_3 самый быстрый, в этой функции используется срез: сложность О(1)
'''
