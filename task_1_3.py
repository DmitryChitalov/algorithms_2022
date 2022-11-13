'''
Курс: Алгоритмы и структуры данных на Python
Урок 4. Задание 3.
'''


from memory_profiler import memory_usage


def res(func):
    def wrapper(*args):
        d1 = memory_usage()
        fun = func(*args)
        d2 = memory_usage()
        drop = d2[0] - d1[0]
        print(f"Выполнение заняло {drop} Mib")
        return fun
    return wrapper


@res
def revers_1(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

@res
def revers_2(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    del enter_num
    return revers_num

st = ('123456789'*10000)
revers_1(st)
revers_2(st)
'''
Выполнение revers_1 заняло 0.09765625 Mib
Выполнение revers_2 заняло 0.0 Mib
Используя del я удалил ссылку на объект и освободил память!
'''