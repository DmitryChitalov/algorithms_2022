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

def puzurek(massiv):
    for x in range(len(massiv)):
        for i in range(len(massiv)-1):
            if massiv[i] < massiv[i+1]:
                massiv[i], massiv[i+1] = massiv[i+1], massiv[i]
    return massiv

def puzurek_modern(massiv):
    for x in range(len(massiv)):
        massiv_copy = massiv.copy()
        for i in range(len(massiv)-1):
            if massiv[i] < massiv[i+1]:
                massiv[i], massiv[i+1] = massiv[i+1], massiv[i]
        if massiv_copy == massiv:
            return massiv
    return massiv

massiv = [randint(-100, 100) for el in range(-100, 100)]
print(f"изначально: {massiv}\nизмененный: {puzurek_modern(massiv)}\n")

print("обычный результат " + str(timeit("puzurek(massiv)", "from __main__ import puzurek, massiv", number = 1000)))
print("результат после изменений " + str(timeit("puzurek_modern(massiv)", "from __main__ import puzurek_modern, massiv", number = 1000)))

"""
обычный результат 2.0306969999801368
результат после изменений 0.011134000029414892

- изменения ускорили процесс
"""
