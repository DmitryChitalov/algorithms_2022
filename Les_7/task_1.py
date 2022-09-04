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

"""
вводим переменную flag, чтобы вовремя остановиться 
Если значения менялись местами, flag = True, 
тогда процесс сортировки поторяется. 
Если никто не поменялся, сортировка закончилась, flag = False, 
функция заканчивает работу и отдаёт список
замеры на списках из 100 элементов
до оптимизации
0.275259109000217
после оптимизации
0.005947902000116301
проверим на 1000 элементов:
30.46276523100005
0.1454506729996865
идея сработала, расходимся

интереса ради написала свой вариант сортировки
0.0001325940029346384
0.00031366199982585385
0.01904041300076642
"""
from random import randint
from timeit import timeit


lst_test = [randint(-100, 100) for i in range(1000)]
lst_test_1 = [randint(-100, 100) for i in range(1000)]

print(lst_test)
print(lst_test_1)


def sort_array(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


print(timeit('sort_array(lst_test)', globals=globals(), number=1000))
print(lst_test)


def optim_sort_array(lst):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = True
    return lst


print(timeit('optim_sort_array(lst_test_1)', globals=globals(), number=1000))
print(lst_test_1)

# идея сортировки удалять по одному минимальный элемент списка, и записывать их в новый массив
# поиск индекса минимального элемента
def find_max(lst):
    max_ind = 0
    max_el = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_el:
            max_el = lst[i]
            max_ind = i
    return max_ind


# собираем сортированный список из удалённых минимальных элементов
def sorting_array(lst):
    res_lst = []
    n = len(lst)
    i = 0
    while i < n:
        i += 1
        res_lst.append(lst.pop(find_max(lst)))
    return lst


lst_1 = [randint(-100,100) for i in range(10)]
lst_2 = [randint(-100,100) for i in range(100)]
lst_3 = [randint(-100,100) for i in range(1000)]


print(timeit('lst = sorting_array(lst_1)', globals=globals(), number=1000))
print(timeit('lst = sorting_array(lst_2)', globals=globals(), number=1000))
print(timeit('lst = sorting_array(lst_3)', globals=globals(), number=1000))