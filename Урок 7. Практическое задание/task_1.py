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


def bubble_sort(obj_list):
    for _ in range(0, len(obj_list)-1):
        for j in range(len(obj_list)-1):
            if(obj_list[j] < obj_list[j+1]):
                temp = obj_list[j]
                obj_list[j] = obj_list[j+1]
                obj_list[j+1] = temp
    return obj_list


obj_list = [randint(1, 1000) for i in range(5000)]

# print(obj_list)
bubble_sort(obj_list[:])


def bubble_sort_1(obj_list):
    swap = True
    counter = 0
    while(swap):
        swap = False
        for i in range(len(obj_list) - counter - 1):
            if obj_list[i] < obj_list[i+1]:
                obj_list[i], obj_list[i+1] = obj_list[i+1], obj_list[i]
                swap = True
        counter += 1
    return obj_list


bubble_sort_1(obj_list[:])

print(timeit("bubble_sort(obj_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_1(obj_list[:])", globals=globals(), number=1000))


"""
Первый вариант стандартный алгоритм сортировки по убыванию
Во втором варианте вводится переменная swap, которая учитывает проход по списку, в котором не совершается ни одной сортировки
Встрой вариант сортирует быстрее
bubble_sort - 2045.3289244999999
bubble_sort_1 - 1327.3040674999997
"""