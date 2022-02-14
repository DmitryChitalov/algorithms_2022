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
from statistics import median
from timeit import timeit


def get_median(lst, m):
    for i, mc in enumerate(lst):  # mc = median candidate
        ls_count = 0  # Количество элементов меньше, чем m
        gr_count = 0  # Количество элементов, которые больще m
        j = 0  # Переменная для индексации на внутреннем цикле.

        # Если количество слева или справа не переполнено цикл продолжается.
        # В противном случае, начинается следующая итерация внешнего цикла.
        while (ls_count <= m) and (gr_count <= m):
            if i != j:  # Не проверяем кандидата на медиану с самим собой
                if mc > lst[j]:
                    ls_count += 1
                elif mc < lst[j]:
                    gr_count += 1
                else:
                    # Пытаемся равные медиане элементы раскидывать либо влево либо вправо.
                    if ls_count >= gr_count:
                        gr_count += 1
                    else:
                        ls_count += 1
                # Если это условие выполняется, то медиана найдена, можно ее вернуть
                if (gr_count == m) and (ls_count == m):
                    return mc
            j += 1
    else:
        return 'Медиана не найдена??'


# Проверка работы
m = 1000
lst = [randint(0, 5000) for _ in range(2 * m + 1)]
srt = sorted(lst[:])

print('Проверка работы и сравнение: ')
print(f'Сортировкой: {srt[m]}')
print(f'Функция get_median: {get_median(lst[:], m)}')
print(f'Функция median из модуля statistics: {median(lst[:])}')

print('Замеры: ')

for m in (10, 100, 1000):
    lst = [randint(0, 5000) for _ in range(2 * m + 1)]

    print(
        f'При {m=}: ',
        timeit(
            'get_median(lst[:], m)',
            globals=globals(),
            number=100
        )
    )
