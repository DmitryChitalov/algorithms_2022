"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


from timeit import timeit

my_list = [i for i in range(1, 51)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(func_1(my_list))
print(timeit("func_1(my_list)", globals=globals(), number=1000))


def func_2(nums):
    new_my_list = []
    for idx, value in enumerate(nums, 0):
        if nums[idx] % 2 == 0:
            new_my_list.append(idx)
    return new_my_list


print(func_2(my_list))
print(timeit("func_2(my_list)", globals=globals(), number=1000))


def func_3(nums):
    new_arr = []
    idx = 0
    for i in nums:
        if i % 2 == 0:
            new_arr.append(idx)
        idx += 1
    return new_arr


print(func_3(my_list))
print(timeit("func_3(my_list)", globals=globals(), number=1000))


def func_4(nums):
    my_list2 = [idx for idx, value in enumerate(nums) if value % 2 == 0]
    return my_list2


print(func_4(my_list))
print(timeit("func_4(my_list)", globals=globals(), number=1000))


"""
Уменьшить время получилось через 'list comprehension'(как и сказали в конце урока) в четвертом варианте.
Т.к. 'list comprehension' быстрее цикла 'for'...плюс исключен метод '.append'.


Остальных случаях, работу кода замедляют лишние присваивания.


Первый вариант(стандарт)

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
0.0028239000239409506
___________________________________________________________________________________________________
Второй вариант

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
0.0033334000036120415
___________________________________________________________________________________________________
Третий вариант

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
0.0040256999782286584
___________________________________________________________________________________________________
Четвертый вариант

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
0.0032780999899841845
"""