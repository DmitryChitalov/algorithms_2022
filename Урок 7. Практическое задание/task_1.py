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

# Сортировка пузырьковая


def bubble_sort(numbers_list):
    x = 1
    count = 0
    while x < len(numbers_list):
        for i in range(len(numbers_list) - x):
            if numbers_list[i] < numbers_list[i + 1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
        count += 1
        x += 1
    return f'{numbers_list} - отсортированный список № 1, количество циклов - {count} '


# Сортировка пузырьковая мод !!!

def bubble_sort_v_2(numbers_list):
    x = 1
    count = 0
    flag = False

    while x < len(numbers_list):
        for i in range(len(numbers_list) - x):
            if numbers_list[i] < numbers_list[i + 1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
                flag = True
        x += 1
        count += 1
        if not flag:
            break
    return f'{numbers_list} - отсортированный список № 2, количество циклов - {count} '


def bubble_sort_v_3(numbers_list):
    x = 1
    count = 0
    flag = False
    num = max(numbers_list)
    numbers_list.remove(num)
    numbers_list.insert(0, num)
    num = min(numbers_list)
    numbers_list.remove(num)
    numbers_list.append(num)
    del num

    while x < len(numbers_list):
        for i in range(len(numbers_list) - x):
            if numbers_list[i] < numbers_list[i + 1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
                flag = True
        x += 1
        count += 1
        if not flag:
            break
    return f'{numbers_list} - отсортированный список № 3, количество циклов - {count} '


numbers_list = [randint(-100, 100) for i in range(15)]
print(f'{numbers_list} - исходный список')

print(bubble_sort(numbers_list))
time_func = timeit("bubble_sort(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции № 1')

print(bubble_sort_v_2(numbers_list))
time_func_2 = timeit("bubble_sort_v_2(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func_2} - время выполнения функции № 2')

print(bubble_sort_v_3(numbers_list))
time_func_3 = timeit("bubble_sort_v_3(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func_3} - время выполнения функции № 3')

# Аналитика
# Как видим в первом варианте мы заходим в цикл столько раз сколько есть в нем элементов,
# Во втором варианте добавил флаг, он позволяет нам остановиться как только условие не выполниться,
# что сокращает кол-во цыклов
# В третьем варианте хотел проверить, измениться ли время,
# если я очевидно поставлю самый большой и самый маленький элемент на их позиции, как видим это увеличило время
# [18, 6, -49, -87, -95, 43, 92, 95, 51, -18, 93, -62, 19, 68, -78] - исходный список
# [95, 93, 92, 68, 51, 43, 19, 18, 6, -18, -49, -62, -78, -87, -95] - отсортированный список № 1, количество циклов - 14
# 0.18871669936925173 - время выполнения функции № 1
# [95, 93, 92, 68, 51, 43, 19, 18, 6, -18, -49, -62, -78, -87, -95] - отсортированный список № 2, количество циклов - 1
# 0.044412399642169476 - время выполнения функции № 2
# [95, 93, 92, 68, 51, 43, 19, 18, 6, -18, -49, -62, -78, -87, -95] - отсортированный список № 3, количество циклов - 1
# 0.06310540065169334 - время выполнения функции № 3
# Готово
