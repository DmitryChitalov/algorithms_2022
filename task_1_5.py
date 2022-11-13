'''
Курс: Основы Python.
Урок 6. Задание 1.
'''


from memory_profiler import memory_usage
from numpy import array, append


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
def func_1():
    result = []
    with open('nginx_logs.txt', "r", encoding="utf-8") as f:
        for line in f:
            ad = line.split(" - - ")[0]
            typ_and_res = line.split('"')[1]
            typ = typ_and_res.split()[0]
            res = typ_and_res.split()[1]
            result.append((ad, typ, res))

@res
def func_2():
    result = array([])
    with open('nginx_logs.txt', "r", encoding="utf-8") as f:
        for line in f:
            ad = line.split(" - - ")[0]
            typ_and_res = line.split('"')[1]
            typ = typ_and_res.split()[0]
            res = typ_and_res.split()[1]
            append((result, ad, typ, res))


func_1()
func_2()
'''
Выполнение func_1 заняло 2.31640625 Mib
Выполнение func_2 заняло 0.03125 Mib
заменил список на array, массив в numpy занимает меньше памяти!
'''