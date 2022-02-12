
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def check_even_3(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num


if __name__ == '__main__':

    my_generator, mem_diff = check_even_3(list(range(100000)))
    print(type(my_generator))
    for i in my_generator:
        print(i)

    print(f"Выполнение заняло {mem_diff} Mib")

# Выполнение заняло 0.01171875 Mib
