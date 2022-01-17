"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
import random
# O(n)
nums_list = [random.randint(0, 100) for i in range(15)]  # O(1)
min_num = nums_list[0]  # O(1)

for item in nums_list:  # O(n)
    if item < min_num:  # O(1)
        min_num = item  # O(1)

print(f'1: {nums_list}')  # O(1)
print(f'1: {min_num}')  # O(1)

# O(n^2)
random_nums = [random.randint(0, 100) for i in range(15)]  # O(1)
min_element = random_nums[0]  # O(1)

for item in random_nums:  # O(n)
    for i in range(1, len(random_nums)):  # O(n) + O(1)
        if item < min_element:  # O(1)
            min_element = item  # O(1)
print(f'2: {random_nums}')  # O(1)
print(f'2: {min_element}')  # O(1)

