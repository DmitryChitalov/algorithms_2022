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


# Классический вариант
def bubble_sort(my_list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1
    return my_list


my_array = [randint(-100, 100) for _ in range(10)]
print('исходный массив:', my_array)

# замер 10: 0.014546700003847945
print(
    timeit(
        "bubble_sort(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort(my_array), '\n')

my_array = [randint(-100, 100) for _ in range(100)]
print('исходный массив:', my_array)

# замер 100: 0.9264003000062075
print(
    timeit(
        "bubble_sort(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort(my_array), '\n')

my_array = [randint(-100, 100) for _ in range(200)]
print('исходный массив:', my_array)

# замер 200: 3.9482208999979775
print(
    timeit(
        "bubble_sort(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort(my_array), '\n')


# Оптимизированный вариант

def bubble_sort_optimize(my_list):
    n = 1
    while n < len(my_list):
        counter = 0
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                counter += 1
        if counter == 0:
            break
        n += 1
    return my_list


my_array = [randint(-100, 100) for _ in range(10)]
print('исходный массив:', my_array)

# замер 10:  0.010672199998225551
print(
    timeit(
        "bubble_sort_optimize(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort_optimize(my_array), '\n')

my_array = [randint(-100, 100) for _ in range(100)]
print('исходный массив:', my_array)

# замер 100: 1.0987595000042347
print(
    timeit(
        "bubble_sort_optimize(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort_optimize(my_array), '\n')

my_array = [randint(-100, 100) for _ in range(200)]
print('исходный массив:', my_array)

# замер 200: 4.340785799999139
print(
    timeit(
        "bubble_sort_optimize(my_array[:])",
        globals=globals(),
        number=1000))

print('отсортированный массив:', bubble_sort_optimize(my_array), '\n')

# Вывод: доработанный алгоритм в целом работает немного медленнее, чем классический, потому что в него добавлен
# счетчик и дополнительная проверка. Но когда функции передается уже отсортированный массив, доработанный алгоритм
# это распознает и не делает лишние операции по сортировке, поэтому выполнится значительно быстрее.
