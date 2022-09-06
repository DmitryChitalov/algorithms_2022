"""
замечания:
ваш массив будет отсортирован уже к первому шагу замеров
всегда нужно передавать копию массива
мы об этом говорили на уроке и неоднократно


исправила замеры:
замеры на списках из 10, 100 и 1000 элементов
до оптимизации:
0.006679712999812182
0.4758669950001604
52.63517727899989
после оптимизации:
0.006220523000138201
0.4629167719999714
52.7878440129999

такая себе оптимизация. На самом деле много будет зависит от сгенерированного массива.
если массив максимально приближен к отсортированному, то оптимизированный пузырёк будет работать лучше,
а так особо разницы нет

для подтверждения создадим вручную списки lst_ord  и lst_dis,
где в lst_ord последние последние 12 элементов будут уже упорядочены, сделаем замеры
до оптимизации:
lst_ord 0.014587351999580278
lst_dis 0.014840972999991209
после оптимизации:
0.0068996639993201825
0.010417362000225694
Для обычного пузырька разницы нет, оптимизированный работает быстрее на lst_ord


ну и заодно переделала замеры сортировки, которую написала сама
на 10, 100 и 1000 элементов
0.004961147999893001
0.2072738090000712
19.44184595600018
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


def optim_sort_array(lst):
    for j in range(len(lst)):
        flag = False
        for i in range(len(lst) - j - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = True
        if not flag:
            break
    return lst



# проверим, что сортировка работает
print(sort_array(lst_test))
print(optim_sort_array(lst_test_1))

# сгенерируем массивы для замеров
lst_10 = [randint(-100, 100) for i in range(10)]
lst_100 = [randint(-100, 100) for i in range(100)]
lst_1000 = [randint(-100, 100) for i in range(1000)]

print(timeit('sort_array(lst_10[:])', globals=globals(), number=1000))
print(timeit('sort_array(lst_100[:])', globals=globals(), number=1000))
print(timeit('sort_array(lst_1000[:])', globals=globals(), number=1000))
# print(timeit('optim_sort_array(lst_10[:])', globals=globals(), number=1000))
# print(timeit('optim_sort_array(lst_100[:])', globals=globals(), number=1000))
# print(timeit('optim_sort_array(lst_1000[:])', globals=globals(), number=1000))

# создадим сами массивы для сортировки
lst_ord = [3, 6, 78, 24, 87, 9, 10, -45, -73, -74, -75, -76, -77, -78, -79, -80, -81, -82, -83, -84]
lst_dis = [3, 6, 78, 24, 87, 9, 10, -45, -76, 34, 2, -10, -78, -77, -80, -79, -82, -81, -84, -83]

print(timeit('sort_array(lst_ord[:])', globals=globals(), number=1000))
print(timeit('sort_array(lst_dis[:])', globals=globals(), number=1000))
# print(timeit('optim_sort_array(lst_ord[:])', globals=globals(), number=1000))
# print(timeit('optim_sort_array(lst_dis[:])', globals=globals(), number=1000))


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
        res_lst.append(lst.pop(find_max(lst)))
        i += 1
    return res_lst


lst_1 = [randint(-100,100) for i in range(10)]
lst_2 = [randint(-100,100) for i in range(100)]
lst_3 = [randint(-100,100) for i in range(1000)]

print(timeit('sorting_array(lst_1[:])', globals=globals(), number=1000))
print(timeit('sorting_array(lst_2[:])', globals=globals(), number=1000))
print(timeit('sorting_array(lst_3[:])', globals=globals(), number=1000))