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

""" Исходная """
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


""" доработаная """
def bubble_sort_reverse(lst: list)-> list:
    """
    Reversed bubble sort,
    :param lst: list
    :return: list
    """
    cycle = True
    while cycle:
        cycle = False
        for index in range(len(lst)-1):
            if lst[index] < lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
                cycle = True
    #print(lst)
    return lst



if __name__ == "__main__":
    for list_size in (10, 100, 1000):
        lst = [randint(-10000, 10000) for _ in range(list_size)]
        print(f'bubble_sort on {list_size} elements: {timeit("bubble_sort(lst[:])", globals=globals(), number=100)}s')
        print(f'bubble_sort_reverse on {list_size} elements: {timeit("bubble_sort_reverse(lst[:])", globals=globals(), number=100)}s')
        lst_second = [randint(-100, 100) for _ in range(list_size)]
        print(f'bubble_sort on {list_size} elements: {timeit("bubble_sort(lst_second[:])", globals=globals(), number=100)}s')
        print(f'bubble_sort_reverse on {list_size} elements: {timeit("bubble_sort_reverse(lst_second[:])", globals=globals(), number=100)}s')
    """
    Результаты диапазон -10000, 10000:
        bubble_sort on 10 elements: 0.0008541000000000035s
        bubble_sort_reverse on 10 elements: 0.0009826000000000001s
        bubble_sort on 100 elements: 0.0688909s
        bubble_sort_reverse on 100 elements: 0.0985719s
        bubble_sort on 1000 elements: 7.6837647s
        bubble_sort_reverse on 1000 elements: 11.9530867s
    Результаты диапазон -100, 100:
        bubble_sort on 10 elements: 0.0009300999999999962s
        bubble_sort_reverse on 10 elements: 0.0009291999999999981s
        bubble_sort on 100 elements: 0.07402710000000001s
        bubble_sort_reverse on 100 elements: 0.1111141s
        bubble_sort on 1000 elements: 8.494308700000001s
        bubble_sort_reverse on 1000 elements: 12.553833099999999s
    Вывод:
        Доработка не помогла, оригинальная функция работает лучше. 
        Доработанная функция в диапазоне -10000 до 10000:
            на 10 елементах медленее на 14 %, 
            на 100 медленее на 42%, 
            на 1000 медленее на 55% 
        Доработанная функция в диапазоне -100 до 100:
            на 10 елементах та же скорость,
            на 100 медленее на 50%, 
            на 1000 медленее на 47%
        Замеры естественно зависят то диапазона чисел в массиве и колличества элементов в массиве. 
    """