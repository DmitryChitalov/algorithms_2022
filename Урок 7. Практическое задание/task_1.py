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


def bubble_sort(lst_obj):
    n = 1
    cnt = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
            cnt += 1
        n += 1
    return cnt, lst_obj


def bubble_sort_new(array):
    cnt = 0
    flag = True
    for j in range(len(array)-1):
        if flag is False:
            return cnt, array
        flag = False
        for i in range(len(array)-1-j):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = True
            cnt += 1
    return cnt, array



my_list = [randint(-100, 100) for x in range(10)]
print('Пузырек 10 элементов = ',
      timeit('bubble_sort(my_list[:])', globals=globals(), number=1000))
print('Пузырек_new 10 элементов = ',
      timeit('bubble_sort_new(my_list[:])', globals=globals(), number=1000))

my_list = [randint(-100, 100) for x in range(100)]
print('Пузырек 100 элементов = ',
      timeit('bubble_sort(my_list[:])', globals=globals(), number=1000))
print('Пузырек_new 100 элементов = ',
      timeit('bubble_sort_new(my_list[:])', globals=globals(), number=1000))

my_list = [randint(-100, 100) for x in range(1000)]
print('Пузырек 1000 элементов = ',
      timeit('bubble_sort(my_list[:])', globals=globals(), number=1000))
print('Пузырек_new 1000 элементов = ',
      timeit('bubble_sort_new(my_list[:])', globals=globals(), number=1000))


sorted_list = list(reversed([x for x in range(1000)]))
print('(список сортированный) Пузырек 1000 элементов = ',
      timeit('bubble_sort(sorted_list[:])', globals=globals(), number=1000))
print('(список сортированный) Пузырек_new 1000 элементов = ',
      timeit('bubble_sort_new(sorted_list[:])', globals=globals(), number=1000))


diff_list = list(reversed([x for x in range(1000)]))
diff_list[100] = 0
print('(список ПОЧТИ сортированный) Пузырек 1000 элементов = ',
      timeit('bubble_sort(diff_list[:])', globals=globals(), number=1000))
print('(список ПОЧТИ сортированный) Пузырек_new 1000 элементов = ',
      timeit('bubble_sort_new(diff_list[:])', globals=globals(), number=1000))



""" 
    Результаты:
                Пузырек 10 элементов =  0.034334
                Пузырек_new 10 элементов =  0.02839129999999998
                Пузырек 100 элементов =  2.9657342
                Пузырек_new 100 элементов =  2.3078993999999997
                Пузырек 1000 элементов =  277.9554273
                Пузырек_new 1000 элементов =  284.1600526
                
                (список сортированный) Пузырек 1000 элементов =  172.07204330000002
                (список сортированный) Пузырек_new 1000 элементов =  0.324487500000032
                
                (список ПОЧТИ сортированный) Пузырек 1000 элементов =  181.21142900000007
                (список ПОЧТИ сортированный) Пузырек_new 1000 элементов =  1.6267264000000523
            
        Вывод:
                Доработка будет эффективной в случае если массив уже отсортирован или частично отсортирован
"""