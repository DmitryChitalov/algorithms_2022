"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опишите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

# Сложность O(n)

some_list = [15, 10, 3, 6, 5, 7, 2]


def min_val(lst):
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value


# O(n^2).

def min_val2(lst):
    lst_length = len(lst)
    for i in range(0, lst_length):
        for j in range(0, lst_length - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

    return lst[0]


print(min_val2(some_list))