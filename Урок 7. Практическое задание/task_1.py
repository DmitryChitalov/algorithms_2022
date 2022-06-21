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


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def optimized_bubble(array):
    n = len(array)
    is_sorted = True
    for i in range(n):
        for j in range(n - i - 1):
            is_sorted = True
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False
        if is_sorted:
            break
    return array


if __name__ == "__main__":
    for n in (10, 100, 1000):
        my_list = [randint(-100, 100) for i in range(n)]
        print(f"Длинна массива: {n}")
        print(timeit("bubble_sort(my_list[:])", number=1000, globals=globals()))
        print(timeit("optimized_bubble(my_list[:])", number=1000, globals=globals()))
"""
Длинна массива: 10
0.005991645157337189
0.005505552049726248
Длинна массива: 100
0.4978366787545383
0.4470277149230242
Длинна массива: 1000
58.72050487762317
63.25626200437546

Выйгрыш в производительности оптимизированного алгоритма зависит от того, насколько отсортированным 
будет исходный массив, на коротких массивах вероятность выше.
"""