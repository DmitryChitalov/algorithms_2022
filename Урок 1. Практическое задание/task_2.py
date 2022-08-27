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

numbers = [10, 2, 3, 10, 566, 88, 99, 1000, ]

# O(n^2) - квадратичная
def min_number1(nums):
    to_change = True
    while to_change:
        to_change = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                to_change = True
    return nums[0]

# O(n) - линейная
def min_number2(nums):
    min_number = nums[0]
    for num in nums:
        if num < min_number:
            min_number = num
    return min_number


print(min_number1(numbers))
print(min_number2(numbers))

