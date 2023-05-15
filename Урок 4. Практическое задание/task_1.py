"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замерыd

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit

def func_1(nums):
    """
    Оригинальная функция проходит по каждому элементу массива и провод сравнение
    :param nums:
    :return:
    """
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """
    Проходит только по чётным элементам и добавляет их сразу
    int((len(nums)-1)/2 - делит на два и округляет вниз, +1 это поправка на функцию range которая считает от 0 до n-1
    :param nums:
    :return:
    """
    new_arr = []
    for i in range(1+int((len(nums)-1)/2)):
        new_arr.append(i*2)
    return new_arr




a = []
for i in range(1000):
    a.append(i)
test1 = lambda : func_1(a)
test2 = lambda : func_2(a)

print(timeit(test1,number=1))
print(timeit(test2,number=1))
print(func_1(a)[-1])
print(func_2(a)[-1])



