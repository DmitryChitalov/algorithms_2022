"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""
import random


def get_min_val_1(nums):    # O(n**2)
    length = len(nums)                                      # O(1)
    for i in range(length):                                 # O(n)
        for j in range(length - i - 1):                     # O(n)
            if nums[j] > nums[j + 1]:                       # O(1)
                nums[j], nums[j + 1] = nums[j + 1], nums[j] # O(1)
    return nums[0]                                          # O(1)

def get_min_val_2(nums):    # O(n)
    min_val = nums[0]   # O(1)
    for i in nums:      # O(n)
        if i < min_val: # O(1)
            min_val = i # O(1)
    return min_val      # O(1)

if __name__ == '__main__':
    lst = [random.randint(-10, 10) for i in range(10)]

    print(lst)
    print(get_min_val_1(lst))
    print(get_min_val_2(lst))
