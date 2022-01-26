"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

nums = [56, 78, 43, 2321, 1, 4, 7, 9, 12]


def find_minimum_1(nums):  # Сложность O(n^2)
    for i in range(len(nums)):
        smallest_number = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_number]:
                smallest_number = j
        nums[i], nums[smallest_number] = nums[smallest_number], nums[i]
    return nums[0]


print(find_minimum_1(nums))


def find_minimum_2(nums):  # Сложность O(n)
    smallest_number = nums[0]
    for number in nums:
        if number < smallest_number:
            smallest_number = number

    return smallest_number


print(find_minimum_2(nums))
