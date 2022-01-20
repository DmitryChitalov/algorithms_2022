# Реализуйте поиск трех компаний с наибольшей годовой прибылью.задание1_3

from collections import Counter
from memory_profiler import profile
from json import dumps


@profile
def sorted_1():
    company = {i: i * 2 for i in range(100000)}
    count = Counter(company)
    print(count.most_common(3))


@profile
def sorted_2():
    company = dumps({i: i * 2 for i in range(100000)})
    count = Counter(company)
    print(count.most_common(3))


sorted_1()
sorted_2()
# благодаря созданию словаря через json память значительно уменьшается (использовалась сериализация)
