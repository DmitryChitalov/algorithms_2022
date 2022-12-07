"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time


def measure_time(func):
    def inner1(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        work_time = time.time() - t1
        print(f'Время выполнения {func.__name__} {work_time:.3f}')

    return inner1


def fill_list(cnt: int):
    result = []
    for i in range(cnt):
        result.append(i * 2)
    return result


def fill_dict(cnt: int):
    result = {}
    for i in range(cnt):
        result[i] = i * 2
    return result


# A)
@measure_time
def measure_fill_list(list_task_0, cnt: int):
    for u in range(cnt):
        list_task_0.append(u * 2)
    return list_task_0


@measure_time
def measure_fill_dict(dict_task_0, cnt: int):
    for q in range(cnt):
        dict_task_0[q] = q + 1
    return dict_task_0


# Экспериментальная проверка
# 10000   0.003
# 20000   0.004
# 40000   0.005
# 80000   0.012
# 160000  0.017
# 320000  0.055
# 640000  0.082
# 1280000     0.181
# 2560000     0.393
# 5120000     0.703
# 10240000    1.425
# Сложность в обоих случаях будет O(n)

# B)
@measure_time
def measure_get_from_list(list_task_1: list, cnt: int):
    idx = 0
    for y in range(cnt):
        x = list_task_1[idx]
        idx += 1
        if idx > len(list_task_1) - 1:
            idx = 0


# 1000    2.201
# 2000    2.277
# 4000    2.271
# 8000    2.258
# 16000   2.269
# 32000   2.267
# 64000   2.274
# 128000  2.207
# 256000  2.260
# 512000  2.289
# 1024000 2.297
@measure_time
def measure_get_from_dict(dict_task_2: dict, cnt: int):
    idx = 0
    for o in range(cnt):
        x = dict_task_2.get(idx)
        idx += 1
        if idx > len(dict_task_2.keys()) - 1:
            idx = 0


# 1000    3.193
# 2000    3.072
# 4000    3.087
# 8000    3.083
# 16000   3.250
# 32000   3.263
# 64000   3.061
# 128000  3.050
# 256000  3.141
# 512000  3.072
# 1024000 3.130
# Сложность в обоих случаях будет O(n)

# C)
@measure_time
def measure_delete_from_list(list_task_3: list, cnt: int):
    if cnt > len(list_task_3):
        raise Exception('Кол-во операций больше длины списка')
    for j in range(cnt):
        del list_task_3[0]


# Удаление с конца
# 100000  0.011
# 200000  0.015
# 400000  0.007
# 800000  0.009
# 1600000 0.015
# 3200000 0.007
# 6400000 0.009
# 12800000    0.009
# 25600000    0.007
# 51200000    0.013
# 102400000   0.022

# Удаление с начала
# 10000   0.025
# 20000   0.033
# 40000   0.082
# 80000   0.214
# 160000  0.479
# 320000  2.351
# 640000  4.832
# 1280000 10.370
# 2560000 21.121
# 5120000 41.954
# 10240000    83.892
@measure_time
def measure_delete_from_dict(dict_task_3: dict, cnt: int):
    if cnt > len(dict_task_3.keys()):
        raise Exception('Кол-во операций больше длины словаря')
    for j in reversed(range(cnt)):
        if dict_task_3.get(j):
            del dict_task_3[j]


# 10000   0.002
# 20000   0.004
# 40000   0.001
# 80000   0.002
# 160000  0.003
# 320000  0.002
# 640000  0.003
# 1280000 0.002
# 2560000 0.002
# 5120000 0.002
# 10240000    0.002
# Сложность в обоих случаях будет O(n)


def main():
    operation_cnt = 100000
    size = 1000

    for i in range(11):
        print(size)
        list_task_1 = fill_list(size)
        measure_fill_list(list_task_1, operation_cnt)
        measure_get_from_list(list_task_1, operation_cnt)
        measure_delete_from_list(list_task_1, operation_cnt)
        size *= 2

    for i in range(11):
        print(size)
        dict_task_1 = fill_dict(size)
        measure_fill_dict(dict_task_1, operation_cnt)
        measure_get_from_dict(dict_task_1, operation_cnt)
        measure_delete_from_dict(dict_task_1, operation_cnt)
        size *= 2


# Аналитика
# Список и словарь заполняются одинаково быстро за O(1) потому, что манипуляции с памятью не требуются(только при заполнении capacity)
# Чтение элементов из списка и словаря выполняется за O(1), потому, что доступ к элементам по индексу(смещению)
# Элементы из конца списка и словаря удаляются за O(1), а из начала списка за O(n), потому, что требуется выделение и копирование памяти