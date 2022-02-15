"""
На маленьких данных доработка показывает примерно такие же результаты, доработка эффективна при работе с большим
массивом данных:
# Пузырьковая сортировка 10 эл-в: 0.07786649999999999
# Пузырьковая сортировка 100 эл-в: 3.3387645
# Пузырьковая сортировка 1000 эл-в: 92.39562020000001
**************************************************************
# Пузырьковая сортировка доработаная, 10 эл-в: 0.0783801
# Пузырьковая сортировка доработаная, 100 эл-в: 3.2665108999999997
# Пузырьковая сортировка доработаная, 1000 эл-в: 91.0140653

"""
from random import randint
from timeit import timeit

numbers = [randint(-100, 100) for _ in range(1000)]


def bubble_sort(nums):
    n = 1
    print(nums)
    while n < len(nums):
        for i in range(len(nums) - n):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_sorting = True
        n += 1
    return print(nums)


def bubble_sort_2(nums):
    is_sorting = True
    n = 1
    print(nums)
    while is_sorting:
        while n < len(nums):
            for i in range(len(nums) - n):
                is_sorting = False
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    is_sorting = True
            n += 1
    return print(nums)


print(f'Пузырьковая сортировка 10 эл-в: {timeit("bubble_sort(numbers[:])", globals=globals(), number=1000)}')
# Пузырьковая сортировка 10 эл-в: 0.07786649999999999
# Пузырьковая сортировка 100 эл-в: 3.3387645
# Пузырьковая сортировка 1000 эл-в: 92.39562020000001
print(f'Пузырьковая сортировка доработаная, 1000 эл-в: {timeit("bubble_sort_2(numbers[:])", globals=globals(), number=1000)}')
# Пузырьковая сортировка доработаная, 10 эл-в: 0.0783801
# Пузырьковая сортировка доработаная, 100 эл-в: 3.2665108999999997
# Пузырьковая сортировка доработаная, 1000 эл-в: 91.0140653
