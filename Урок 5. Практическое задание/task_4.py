"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

#######################################################################################################################
"""
В задании выполнил замеры времени и подсчет в процентах следующих операций:

- проход по словарю циклом --> OrderedDict всегда медленней отрабатывает. В среднем процентов на 60 - 100 медленнее

- получение элемента из словаря --> OrderedDict где-то на границе, то быстрее чем обычный словарь, то медленней.
Средние показатели от 0 до 15 процентов как в плюс так и в минус

- добавление 100 элементов в словарь  --> OrderedDict где-то на границе, то быстрее чем обычный словарь, то медленней.
Средние показатели от 0 до 15 процентов как в плюс так и в минус

- удаление 100 элементов --> OrderedDict всегда медленней отрабатывает. В среднем процентов на 150 - 200 медленнее

Применение OrderedDict не совсем целесообразно. Так как в большинстве проверенных в данном задании случаев 
отрабатывает медленней чем словарь dict.
Возможно применение если только необходимо отметить, что в данном словаре нужно, чтобы было по порядку добавления. 
Чтобы можно было увидеть, что в словаре нельзя менять местами содержимое. 
"""
#######################################################################################################################

from collections import OrderedDict
from timeit import timeit

one_dict = {i: i + i for i in range(1000)}
two_dict = OrderedDict({i: i + i for i in range(1000)})


def diff_time(func_1, func_2):
    """
    Функция вывода разности скорости выполнения в процентах.
    """
    if func_1 > func_2:
        return f'OrderedDict быстрее чем dict на {100 - (100 * func_2 / func_1)} процента(ов)'
    elif func_1 < func_2:
        return f'OrderedDict медленнее чем dict на {(100 * func_2 / func_1) - 100} процента(ов)'


def enumeration_value(test_dict):
    """
    Функция проходит по словарю циклом for
    """
    for k, v in test_dict.items():
        continue
    return test_dict


time_func_1 = timeit(f'enumeration_value(one_dict)', globals=globals(), number=10000)
print(f'Время прохода циклом for по словарю dict: {time_func_1}')

time_func_2 = timeit(f'enumeration_value(two_dict)', globals=globals(), number=10000)
print(f'Время прохода циклом for по словарю OrderedDict: {time_func_2}')
print(diff_time(time_func_1, time_func_2))


# OrderedDict медленнее чем простой словарь

def getting_value(test_dict):
    """
    Получение элемента словаря
    """
    return test_dict[50]


time_func_1 = timeit(f'getting_value(one_dict)', globals=globals(), number=10000)
print(f'Время получение элемента из словаря dict: {time_func_1}')

time_func_2 = timeit(f'getting_value(two_dict)', globals=globals(), number=10000)
print(f'Время получение элемента из словаря OrderedDict: {time_func_2}')
print(diff_time(time_func_1, time_func_2))


# Получение элемента из словаря OrderedDict быстрее чем из простого словаря (в большинстве замеров).
# Также бывает, что замеры показывают, что словарь OrderedDict медленнее простого словаря dict.


def adding_element(test_dict):
    """
    Добавление элемента в словарь
    """
    for i in range(101):
        test_dict[i + 1000] = i + 2000
    return test_dict


time_func_1 = timeit(f'adding_element(one_dict)', globals=globals(), number=1)
print(f'Время добавления элемента в словарь dict: {time_func_1}')

time_func_2 = timeit(f'adding_element(two_dict)', globals=globals(), number=1)
print(f'Время добавления элемента в словарь OrderedDict: {time_func_2}')
print(diff_time(time_func_1, time_func_2))


# Добавление элемента в словарь OrderedDict медленнее чем добавление в простой словарь dict.
# Также бывает, что замеры показывают, что словарь OrderedDict быстрее простого словаря dict.

def del_element(test_dict):
    """
    Удаление элемента в словарь
    """
    for i in range(100):
        test_dict.pop(i)
    return test_dict


time_func_1 = timeit(f'del_element(one_dict)', globals=globals(), number=1)
print(f'Время удаления элемента из словаря dict: {time_func_1}')

time_func_2 = timeit(f'del_element(two_dict)', globals=globals(), number=1)
print(f'Время удаления элемента из словаря OrderedDict: {time_func_2}')
print(diff_time(time_func_1, time_func_2))

# Удаление элемента из словаря OrderedDict медленнее чем удаление элемента из словаря dict.
