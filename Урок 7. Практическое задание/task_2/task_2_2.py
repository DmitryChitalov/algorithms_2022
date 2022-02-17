"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


# идея вычисления медианы без сортировки массива:
# внешний цикл - проходим по всем значениям val_j, во внутреннем сравниваем val_j с каждым значением.
# если < инкремент count_lt_gt иначе декремент. Усли == инкремент count_eq
# условие выхода получил при отладке: от count_lt_gt==0 до abs(count_lt_gt) <= count_eq при повторах значений.
def median_wo_sort(lst):  # корректная работа для массивов размером 2m + 1
    for val_j in lst:
        count_lt_gt, count_eq = 0, -1  # сравнение с собой обнуляет счетчик count_eq
        for val_i in lst:
            if val_i == val_j:
                count_eq += 1
            else:
                count_lt_gt += 1 if val_j < val_i else -1
        if abs(count_lt_gt) <= count_eq:
            return val_j


def median_sorted(lst):  # средний, если len(list_) нечет, или среднее от двух средних значений
    q, r = divmod(len(lst), 2)
    return sorted(lst)[q] if r else sum(sorted(lst)[q - 1:q + 1]) / 2


# проверка правильной работы
# x = [randint(-100, 100) for _ in range(11)]
# print(median_sorted(x[:]))
# print(median_wo_sort(x[:]))

# замеры на массивах длиной 10, 100, 1000 элементов
x0 = [randint(-100, 100) for _ in range(1001)]
print(timeit("median_sorted(x0[:])", globals=globals(), number=1000))  # 0.068
print(timeit("median_wo_sort(x0[:])", globals=globals(), number=1000))  # 4.070

x1 = [randint(-100, 100) for _ in range(101)]
print(timeit("median_sorted(x1[:])", globals=globals(), number=1000))  # 0.0028
print(timeit("median_wo_sort(x1[:])", globals=globals(), number=1000))  # 0.1762

x2 = [randint(-100, 100) for _ in range(11)]
print(timeit("median_sorted(x1[:])", globals=globals(), number=1000))  # 0.0026
print(timeit("median_wo_sort(x1[:])", globals=globals(), number=1000))  # 0.1026

"""
Поиск медианы с помощью стандартной сортировки Timsort вне конкаренции.
Поиск медианы с помощью реализованной функции без сортировки имеет квадратичную сложность и 
по мере увеличения длины массива резко замедляется.
"""