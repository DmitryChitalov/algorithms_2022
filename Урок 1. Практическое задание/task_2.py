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

numbers = [10, 2, 3, 10, 566, 88, 99, 1000,]

# O(n) - линейная
def min_number1(nums):
    min_number = nums[0]
    for num in nums:
        if num < min_number:
           min_number = num
    print(min_number)

# O(n^2) - квадратичная
# Пузырьковая сортировка
def min_number2(nums):
    to_change = True
    while to_change:
        to_change = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                to_change = True
    print(nums[0])

#O(n^2) - квадратичная
# Сортировка выборкой
def min_number3(nums):
    for i in range(len(nums)):
        lowest_val_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[lowest_val_index]:
                lowest_val_index = j
        nums[i], nums[lowest_val_index] = nums[lowest_val_index], nums[i]
    print(nums[0])

#O(n^2) - квадратичная
# Сортировка вставками
def min_number4(nums):
    for i in range(1, len(nums)):
        num_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > num_to_insert:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = num_to_insert
    print(nums[0])

min_number1(numbers)
min_number2(numbers)
min_number3(numbers)
min_number4(numbers)