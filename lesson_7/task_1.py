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
from timeit import timeit
from random import randrange

lst1 = [randrange(-100, 100) for _ in range(10)]
lst2 = [randrange(-100, 100) for _ in range(100)]
lst3 = [randrange(-100, 100) for _ in range(500)]
lst4 = [x for x in range(500)]
lst4.reverse()


def bubble_sort_reverse(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


# Доработанный алгоритм
def bubble_sort_reverse2(lst):
    n = 1
    swap = True
    while n < len(lst):
        while swap:
            swap = False
            for i in range(len(lst) - n):
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swap = True
            n += 1
        return lst


print(f'Исходный массив: {lst1}')
print(f'Массив, отсортированный исходным алгоритмом сортировки методом "пузырька":  {bubble_sort_reverse(lst1.copy())}')
print(f'Массив, отсортированный доработанным алгоритмом сортировки методом "пузырька":'
      f'  {bubble_sort_reverse2(lst1.copy())}')

print(timeit('bubble_sort_reverse(lst1.copy())', globals=globals(), number=1000))  # 0.0056412000000000025
print(timeit('bubble_sort_reverse2(lst1.copy())', globals=globals(), number=1000))  # 0.004546599999999998
print('\n-------------------------------------------------------------------\n')
print(timeit('bubble_sort_reverse(lst2.copy())', globals=globals(), number=1000))  # 0.40343740000000006
print(timeit('bubble_sort_reverse2(lst2.copy())', globals=globals(), number=1000))  # 0.4101827
print('\n-------------------------------------------------------------------\n')
print(timeit('bubble_sort_reverse(lst3.copy())', globals=globals(), number=1000))  # 10.7145789
print(timeit('bubble_sort_reverse2(lst3.copy())', globals=globals(), number=1000))  # 10.8325923
print('\n-------------------------------------------------------------------\n')
print(timeit('bubble_sort_reverse(lst4.copy())', globals=globals(), number=1000))  # 6.0228742
print(timeit('bubble_sort_reverse2(lst4.copy())', globals=globals(), number=1000))  # 0.024377100000002372


"""Исходный и доработанный алгоритмы сортировки методом "пузырька" работают приблизительно с одинаковой скоростью, если 
элементы списка расположены изначально рандомно. Однако, доработанный алгоритм сортировки оказыается эффективнее, если
за проход по списку не совершается ни одной сортировки (список элементов изначально отсортирован или во время сортировки
складывается такая ситуация, что дальнейшая сортировка уже не требуется, даже если n < len(lst)). """
