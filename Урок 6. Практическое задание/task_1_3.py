#Это файл для третьего скрипта

from pympler import asizeof
# курс алгоритмы дз3 задание 1


#неоптимизированное решение
def list_gen(num):
    return [i for i in range(1, num+1)]


# оптимизированное
def lst_gen(n):
    for i in range(1, n+1):
        yield i


print(asizeof.asizeof(lst_gen(100)))
print(asizeof.asizeof(list_gen(100)))
# 424
# 4120
"""
применение генератора снижает расход памяти почти в 10 раз
"""