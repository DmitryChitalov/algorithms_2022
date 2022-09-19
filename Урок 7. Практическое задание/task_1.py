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

from random import shuffle
from timeit import timeit


def sort_bubble(value: list) -> list:
    count = 1
    while count != len(value):
        for i in range(len(value) - count):
            if value[i] < value[i + 1]:
                value[i], value[i + 1] = value[i + 1], value[i]
        count += 1
    return value


def sort_bubble_2(value: list) -> list:
    count = 1
    replacement = True
    while replacement:
        replacement = False
        for i in range(len(value) - count):
            if value[i] < value[i + 1]:
                value[i], value[i + 1] = value[i + 1], value[i]
                replacement = True
        count += 1
    return value


if __name__ == '__main__':
    my_list = list(range(-100, 101))
    shuffle(my_list)
    new_my_lst = my_list[:]
    print(f'Исходный список: {my_list}')
    print('Время: ', timeit('sort_bubble(my_list)', globals=globals(), number=1000))
    print('Время: ', timeit('sort_bubble_2(new_my_lst)', globals=globals(), number=1000))
    print(f'Отсортированный список по убыванию: {my_list}')
    print(f'Отсортированный список по убыванию: {new_my_lst}')


"""
В списке может быть не отсортировано например 2 элемента из 100, в первом случае
когда после двух циклов элементы встанут на место, то алгоритм всё равно будет гонять цикл
до тех пор пока не выполнится условие цикла while.
Во втором случае если за цикл не случилось ни одной перестановки, значит список отсортирован и выходим из цикла
 
Время затраченное в первом случае :  1.2902459999895655
Время затраченное во втором случае:  0.0188404000073205
"""
