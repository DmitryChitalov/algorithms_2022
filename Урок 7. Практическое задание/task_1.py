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
from random import randint


lst = []
for _ in range(1000):
    lst.append(randint(-100, 100))
print(lst)


def func_1(lst_obj):
    for i in range(len(lst_obj) - 1):
        for j in range(len(lst_obj) - i - 1):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
    return lst_obj


f1 = """
func_1(lst)"""

print(timeit(f1, globals=globals(), number=50), 'fiunc_1')


def func_2(lst_obj):
    for i in range(len(lst_obj) - 1):
        for j in range(len(lst_obj) - i - 1):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
            break
    return lst_obj

f2 = """
func_2(lst)"""
print(func_2(lst))
print(timeit(f2, globals=globals(), number=50), 'fiunc_2')

"""
Результат выполнения:
1.4808988000149839 -- исходная функция сортировки
0.012850600003730506 -- доработанная
В результате доработки время выполнения существенно уменьшилось, чем больше массив тем больший эффект
дает такая доработка
"""
