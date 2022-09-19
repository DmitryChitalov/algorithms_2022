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
import random
import timeit


def rand_mas():
    mass = []
    for i in range(100):
        mass.append(int(random.uniform(-100, 100)))
    return mass


def sort_mass_old(new_mass):
    for i in range(len(new_mass) - 1):
        for j in range(len(new_mass) - 1 - i):
            if new_mass[j] < new_mass[j + 1]:
                new_mass[j], new_mass[j + 1] = new_mass[j + 1], new_mass[j]
    return new_mass


def sort_mass(new_mass):
    for i in range(len(new_mass) - 1):
        k = False
        for j in range(len(new_mass) - 1 - i):
            if new_mass[j] < new_mass[j + 1]:
                new_mass[j], new_mass[j + 1] = new_mass[j + 1], new_mass[j]
                k = True
        if not k:
            break
    return new_mass


mass = rand_mas()
print(mass)

per = """
sort_mass_old(mass.copy())
"""
per1 = """
sort_mass(mass.copy())
"""

print(timeit.timeit(setup='', stmt=per, number=10000, globals=globals()))
print(timeit.timeit(setup='', stmt=per1, number=10000, globals=globals()))
print(sort_mass(mass.copy()))
print(sort_mass_old(mass.copy()))
