"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randint
from timeit import timeit


def bubble(nums):
    length = len(nums)
    for i in range(length):
        for j in range(length - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def bubble_new(nums):
    length = len(nums)
    for i in range(length):
        change_flag = False
        for j in range(length - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                change_flag = True
        if not change_flag:
            break
    return nums


my_list = [randint(-100, 100) for i in range(100)]

# исходный массив
print('Исходный массив')
print(my_list)
print('-' * 50)

# сортировка исходного массива
print('Замер сортировки исходного массива')
print(timeit("bubble(my_list[:])", globals=globals(), number=10000))
print('-' * 50)

# сортировка исходного массива улучшенной функцией
print('Замер сортировки исходного массива улучшенной функцией')
print(timeit("bubble_new(my_list[:])", globals=globals(), number=10000))
print('-' * 50)

# сортировка исходного массива
bubble(my_list)
print('Отсортированный массив')
print(my_list)
print('-' * 50)

# сортировка отсортированного массива обычной функцией
print('Замер сортировки отсортированного массива обычной функцией')
print(timeit("bubble(my_list)", globals=globals(), number=10000))
print('-' * 50)

# сортировка отсортированного массива улучшенной функцией
print('Замер сортировки отсортированного массива улучшенной функцией')
print(timeit("bubble_new(my_list)", globals=globals(), number=10000))
print('-' * 50)



# улучшенная функция показывает существенную разницу в скорости на отсортированном списке, т.к. только один проход,