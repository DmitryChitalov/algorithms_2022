'''
Курс: Алгоритмы и структуры данных на Python
Урок 4. Задание 1.
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
def func_1(nums):
    res = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return res

@res
def func_2(nums):
    res = (i for i in range(len(nums)) if nums[i] % 2 == 0)
    return res

num_1 = [i for i in range(10000)]
func_1(num_1)
func_2(num_1)
'''
Выполнение func_1 заняло 0.10546875 Mib
Выполнение func_2 заняло 0.0 Mib
LC заменил на генератор, тем самым выиграл в памяти
'''