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
import time
from copy import deepcopy


# Для создания исходного списка используем функцию fill_list

def fill_list(range1):
    test1_list = []
    for ii in range(0, range1):
        test1_list.append(randint(-100, 100))
    return test1_list


def sort_bubble_rev(start_list1):
    start_val = time.time()
    for i in range(len(start_list)):
        for j in range(range_to_fill - i - 1):
            if start_list1[j] > start_list1[j + 1]:
                start_list1[j], start_list1[j + 1] = start_list1[j + 1], start_list1[j]
    end_val = time.time()
    start_list1.reverse()
    return end_val - start_val, start_list1


def sort_bubble_rev_opt(start_list11):
    start_val1 = time.time()
    for i in range(len(start_list)):
        change_mark = 0
        for j in range(range_to_fill - i - 1):
            if start_list11[j] > start_list11[j + 1]:
                start_list11[j], start_list11[j + 1] = start_list11[j + 1], start_list11[j]
                change_mark += 1
        if change_mark > 0:
            pass
        else:
            start_list11.reverse()
            return time.time() - start_val1, start_list11
    end_val1 = time.time()
    start_list11.reverse()
    return end_val1 - start_val1, start_list11


range_to_fill = int(input("Введите кол-во чисел в массиве:    "))

print('+++++++++++++++++++++Базовое решение++++++++++++++++++++++++++++++++++')

start_list = fill_list(range_to_fill)
start_list2 = deepcopy(start_list)
print(f'Начальный список:{start_list}')

time_count1, finish_list = sort_bubble_rev(start_list)
print(f'Время сортировки: {time_count1}')
print(f'Cортированнный список:{finish_list}')

print('+++++++++++++++++++++Оптимизированное решение++++++++++++++++++++++++++++++++++')

print(f'Начальный список:{start_list2}')

time_count2, finish_list2 = sort_bubble_rev_opt(start_list2)
print(f'Время сортировки: {time_count2}')
print(f'Cортированнный список:{finish_list2}')


"""
Анализ: доработка помогла ускорить сортировку на массивах более 300 и менее 1000 элементов. До 300 элементов 
оба варианта сортируют примерно одинаково, после 1000 стандартная пузырьковая сортировка начинает сортировать быстрее.
"""