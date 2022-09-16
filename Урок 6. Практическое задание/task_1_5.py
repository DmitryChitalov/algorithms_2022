"""
Задание 1.
Это файл для пятого скрипта
"""
"""
Урок 3
Задание 1.
"""

from time import time
from pympler import asizeof
from json import dumps, loads


def timer_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} '
              f'составило {end - start}')
        return result
    return timer


# Пункт а:
@timer_decorator
def write_list(list, n):
    for i in range(n):
        list.append(i)       # Сложность операции O(1)


list1 = []
n = 10 ** 4
write_list(list1, n)
print('-' * 50)


@timer_decorator
def write_dict(dict, n):
    for i in range(n):  # добавления нового элемента имеет сложность О(1).
        dict[i] = i


dict1 = {}
write_dict(dict1, n)
dumped_dict = dumps(dict1)
print(f'Размер словаря: {asizeof.asizeof(dict1)}')
print(f'Размер сжатого словаря: {asizeof.asizeof(dumped_dict)}')
print('_' * 50)


'''
Размер словаря: 614992
Размер сжатого словаря: 137832
Как видно хранение словаря после сжатия оптимизирует затраты памяти
'''