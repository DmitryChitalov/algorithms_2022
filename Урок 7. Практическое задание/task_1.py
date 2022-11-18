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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_improved(lst_obj):
    n = 1
    already_sorted = True
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                already_sorted = False
        if already_sorted is True:
            break
        n += 1
    return lst_obj


just_list = [346, 12, 9, 1, 2, 64, 218, 3, 69, 24, 125]
print(f'Неотсортированный массив: {just_list}\n')

print(f'Bubble алгоритм: '
      f'{timeit("bubble_sort(just_list[:])",globals=globals(),number=1000)}')

print(f'Доработанный bubble алгоритм: '
      f'{timeit("bubble_sort_improved(just_list[:])",globals=globals(),number=1000)}\n')

print(f'Отсортированный массив: {bubble_sort_improved(just_list)}\n')

print(f'Bubble алгоритм на уже отсортированном списке: '
      f'{timeit("bubble_sort(just_list[:])",globals=globals(),number=1000)}')

print(f'Доработанный bubble алгоритм на уже отсортированном списке: '
      f'{timeit("bubble_sort_improved(just_list[:])",globals=globals(),number=1000)}\n')

print('Вывод: сравнив обычный и доработанный варианты "пузырька", могу сказать, что при сортировке неотсортированного\n'
      'массива очень небольшое преимущество будет у обычного пузырька, ведь нет дополнительных элементов, но если\n'
      'массив уже отсортирован, то доработанный вариант будет намного быстрее, ведь после одного прохода он сразу\n'
      'прекращает работу. В итоге, доработанный вариант будет эффективен, если заранее неизвестно, будет массив\n'
      'отсортирован или нет')
