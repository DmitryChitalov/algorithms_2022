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


def bubble_sort(my_list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1
    return my_list


def bubble_sort2(my_list):
    n = 1
    while n < len(my_list):
        f = True
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                f = False
        else:
            if f is False:
                n += 1
            else:
                return my_list
    return my_list


my_list = [randint(-100, 100) for _ in range(10)]
print(my_list)
print(bubble_sort(my_list[:]))
print(timeit('bubble_sort(my_list[:])', globals=globals(), number=1000))
print(timeit('bubble_sort(my_list[:])', globals=globals(), number=10000))
print(timeit('bubble_sort(my_list[:])', globals=globals(), number=100000))

print(my_list)
print(bubble_sort2(my_list[:]))
print(timeit('bubble_sort2(my_list[:])', globals=globals(), number=1000))
print(timeit('bubble_sort2(my_list[:])', globals=globals(), number=10000))
print(timeit('bubble_sort2(my_list[:])', globals=globals(), number=100000))

"""
При использовании моей модификации, скорость выполнения сортировки увеличилась, так как отпала необходимость проходить 
список раз за разом в ничего в нем не меняя, а сортировка заканчивается в момент когда уже нечего менять местами.    
"""
