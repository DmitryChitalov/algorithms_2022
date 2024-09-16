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


def bubble_sort_desc(arr):
    n = 1         # счетчик проходов, на первом проходе пузырек поднимает 1й элемент, на втором - второй и тд
    while n < len(arr):
        for i in range(len(arr)-n):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        n += 1
    return arr


def optimized_bubble_sort(arr):
    is_sorted = False          # счетчик не нужен тк выходим из цикла при отсутствии перестановок, используем флаг
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
    return arr


almost_sorted_data = [9, 10, 8, 7, 6, 5, 4, 3, 2, 1, 0]
data = [randint(-100, 100) for i in range(10)]
num = 10000
print(data)
print(bubble_sort_desc(data[:]))
print(optimized_bubble_sort(data[:]))

print('Время выполнения сортировки до оптимизации: ', timeit('bubble_sort_desc(data[:])', number=num, globals=globals()))
print('Время выполнения сортировки после оптимизации: ', timeit('optimized_bubble_sort(data[:])', number=num, globals=globals()))
print('Время выполнения сортировки до оптимизации на почти отсортированном массиве: ', timeit('bubble_sort_desc(almost_sorted_data[:])', number=num, globals=globals()))
print('Время выполнения сортировки после оптимизации на почти отсортированном массиве: ', timeit('optimized_bubble_sort(almost_sorted_data[:])', number=num, globals=globals()))

# Со случайными числами оптимизация не дает результата. Так как оптимизированнный
# вариант прерывает работу при отсутствии перестановок за проход то чем больше отсортирован исходный
# массив тем больший эффект дает оптимизация, что подтверждает тест на почти отсортированном массиве
