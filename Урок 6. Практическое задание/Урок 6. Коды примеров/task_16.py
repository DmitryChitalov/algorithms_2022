from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


@memory
def check_even_1(lst):
    new_list = [i for i in lst if i % 2 == 0]
    return new_list


@memory
def check_even_2(lst):
    new_list = filter(lambda x: x % 2 == 0, lst)
    return new_list


check_even_1(list(range(5000000)))
check_even_2(list(range(5000000)))

"""
Выполнение заняло 19.453125 Mib
Выполнение заняло 0.00390625 Mib
"""
