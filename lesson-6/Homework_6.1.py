from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...

# Рекурсия
@decor
def sum_finder_recur(number, founded_sum=0, row_element=1):
    if number > 0:
        founded_sum += row_element
        row_element /= -2
        number -= 1
        return sum_finder_recur(number, founded_sum, row_element)
    else:
        return founded_sum


# Цикл
@decor
def sum_finder_cycle(number):
    row_element = 1
    founded_sum = 0
    for i in range(number):
        founded_sum += row_element
        row_element /= -2
    return founded_sum


#  my_sum1, mem1 = sum_finder_recur(10**2)
# print(mem1)
# Выполнение заняло 0.21484375 Mib

my_sum2, mem2 = sum_finder_cycle(10**2)
print(mem2)
# Выполнение заняло 0.00390625 Mib