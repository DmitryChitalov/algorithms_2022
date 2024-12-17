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
from memory_profiler import memory_usage


# Функция декоратор для измерения потребления памяти и подсчёта времени.
def count_memory_usage(func):
    """Counts memory usage and time usage of a function."""

    def wrapper(in_array):
        mem_usage_before = memory_usage()[0]
        result = func(in_array.copy())
        print(timeit(lambda: func(in_array.copy()), number=10))
        mem_usage_after = memory_usage()[0]
        print(f"Использовано памяти: {mem_usage_after - mem_usage_before} MiB")
        return result

    return wrapper


@count_memory_usage
# Функция сортировки пузырьком без оптимизации.
def bubble_sort_descending(sort_arr: list[int]) -> list[int]:
    n = len(sort_arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sort_arr[j] < sort_arr[j + 1]:
                sort_arr[j], sort_arr[j + 1] = sort_arr[j + 1], sort_arr[j]
    return sort_arr


@count_memory_usage
# Функция сортировки пузырьком по убыванию с оптимизацией.
def bubble_sort_descending_optimized(sort_arr: list[int]) -> list[int]:
    n = len(sort_arr)
    for i in range(n):
        swapped = False  # Флаг, показывающий, была ли хотя бы одна перестановка.
        for j in range(0, n - i - 1):
            if sort_arr[j] < sort_arr[j + 1]:
                sort_arr[j], sort_arr[j + 1] = sort_arr[j + 1], sort_arr[j]
                swapped = True
        if not swapped:  # Если не было перестановок, массив отсортирован.
            break
    return sort_arr


# Генерация случайного массива [-100, 99).
random_array = [randint(-100, 99) for _ in range(10000)]

# Вызов функций сортировки для получения статистических данных и вывод результатов.
bubble_sort_descending(random_array.copy())
bubble_sort_descending_optimized(random_array.copy())

"""
Полученные результаты:
Для функции bubble_sort_descending(random_array.copy()):
85.76988600000004
Использовано памяти: 0.16015625 MiB

для функции bubble_sort_descending_optimized(random_array.copy()):
87.81971429999976
Использовано памяти: 0.15625 MiB

Выводы:
Оптимизация полезна для уже отсортированных или почти отсортированных по убыванию массивов,
а в случае случайных данных прирост будет небольшим.
"""
