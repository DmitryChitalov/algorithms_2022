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
    a = reversed(str(enter_num))
    b = ''.join(a)
    return b

@res
def revers_2(enter_num):
    yield reversed(str(enter_num))

st = ('123456789')
revers_1(st)
revers_2(st)
'''
Выполнение revers_1 заняло 0.015625 Mib
Выполнение revers_2 заняло 0.0 Mib
Оператор yield исключил сохранения промежуточных результатов!
'''