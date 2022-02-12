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

def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj

def bubble_sort_smart(lst):
    n = 1
    while n < len(lst):
        unordered = True
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                unordered = False
        if unordered == True:
            break

    return lst

# orig_list = [100, 100, 100, 95, 94, 92, 92, 90, 89, 87, 86, 84, 83, 82, 77, 74, 74, 73, 73, 72, 68, 66, 65, 63, 60, 56,
#               53, 49, 46, 46, 43, 41, 35, 34, 33, 31, 30, 30, 28, 18, 18, 18, 17, 17, 13, 12, 10, 4, 4, 2, 1, -5, -5,
#               -13, -16, -17, -21, -22, -26, -27, -29, -30, -31, -32, -33, -38, -38, -40, -41, -48, -50, -52, -52, -57,
#               -58, -58, -58, -61, -62, -64, -64, -70, -72, -77, -78, -80, -81, -82, -86, -86, -89, -89, -90, -91, -94,
#               -94, -95, -96, -98, -100]
orig_list = [randint(-100, 100) for _ in range(10)]
#orig_list = [randint(-100, 100) for _ in range(100)]
#orig_list = [randint(-100, 100) for _ in range(1000)]

print(timeit("bubble_sort(orig_list[:])",
             globals=globals(),
             number=1000))
print(timeit("bubble_sort_smart(orig_list[:])",
             globals=globals(),
             number=1000))

print(orig_list)
print(bubble_sort(orig_list))
print(bubble_sort_smart(orig_list))
#при обработке небольших списков(10) время с доработкой немного меньше
# 0.013248899999999994
# 0.010224200000000003
#Если список отсортированный то время с доработкой время работы меньше в разы
# 0.3099869
# 0.005763499999999977
# при увеличении колличества элементов в списке(100) время работы с доработкой начинает рости
# 0.6591533
# 0.8354919999999999
# при большом колличестве несортированных элементов (1000) время с доработкой увеличивается
# 79.2742705
# 120.52962350000001