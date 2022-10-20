"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import Timer
from timeit import timeit

# итератор с функцией append
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# итератор с конкатенацией
def func_concat(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr = new_arr + [nums[i]]
    return new_arr

# создание массива с помощью list comprehension
def func_list_comp(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr




nums_100 = [num for num in range(100)]
nums_1000 = [num for num in range(1000)]
nums_10000 = [num for num in range(10000)]

# print(func_1(nums_100))
# print(func_concat(nums_100))
# print(func_list_comp(nums_100))

if __name__ == '__main__':
    print('Измерения для списка из 100 элементов на 100 прогонов.')
    t1 = Timer(stmt="func_1(nums_100)", setup="from __main__ import func_1, nums_100")
    print("list append for nums_100 ", t1.timeit(number=100), "seconds")

    t2 = Timer(stmt="func_concat(nums_100)", setup="from __main__ import func_concat, nums_100")
    print("list concat for nums_100 ", t2.timeit(number=100), "seconds")

    t3 = Timer(stmt="func_list_comp(nums_100)", setup="from __main__ import func_list_comp, nums_100")
    print("list comprehension for nums_100 ", t3.timeit(number=100), "seconds")

    print('\nИзмерения для списка из 1000 элементов на 100 прогонов.')
    t1 = Timer(stmt="func_1(nums_1000)", setup="from __main__ import func_1, nums_1000")
    print("list append for nums_1000 ", t1.timeit(number=100), "seconds")

    t2 = Timer(stmt="func_concat(nums_1000)", setup="from __main__ import func_concat, nums_1000")
    print("list concat for nums_1000 ", t2.timeit(number=100), "seconds")

    t3 = Timer(stmt="func_list_comp(nums_1000)", setup="from __main__ import func_list_comp, nums_1000")
    print("list comprehension for nums_1000 ", t3.timeit(number=100), "seconds")

    print('\nИзмерения для списка из 10000 элементов на 100 прогонов.')
    t1 = Timer(stmt="func_1(nums_10000)", setup="from __main__ import func_1, nums_10000")
    print("list append for nums_10000 ", t1.timeit(number=100), "seconds")

    t2 = Timer(stmt="func_concat(nums_10000)", setup="from __main__ import func_concat, nums_10000")
    print("list concat for nums_100000 ", t2.timeit(number=100), "seconds")

    t3 = Timer(stmt="func_list_comp(nums_10000)", setup="from __main__ import func_list_comp, nums_10000")
    print("list comprehension for nums_10000 ", t3.timeit(number=100), "seconds")

    # Оптимизируем локальные замеры времени.
    print("\nlist append for nums_100 ", timeit("func_1(nums_100)", globals=globals(), number=100))

    print("\nlist concat for nums_100 ", timeit("func_concat(nums_100)", globals=globals(), number=100))

    print("\nlist comprehension for nums_100 ", timeit("func_list_comp(nums_100)", globals=globals(), number=100))

    # Определим время выполнения выражения list comprehension 10000 элементов на 10000 прогонов.
    print(timeit("new_arr = [i for i in range(10000) if i % 2 == 0]", number=10000))

# Функция в конкатенацией работает медленнее всего, хотя при количестве элементов 100 и менее это не сильно заметно,
# так как время выполнения мало.
# Оптимизация работы функции использованием list comprehension, даёт выигрыш во времени исполнения, но это становится
# заметно при количестве элементов более 10000. Запись функции тоже более лаконична.
# Оптимизация данной функции неообходима при использовании большого числа входных элементов. При числе элементов
# менне 1000 все используемые функции неплохо работают.