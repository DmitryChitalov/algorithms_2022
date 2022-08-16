"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


from random import sample


def min_value_list_1(list_obj):
    """Функция должна вернуть минимальное значение списка

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,


    Сложность: Квадратичная (O(n**2))
    """
    min_number = list_obj[0]
    for i in range(len(list_obj) - 1):  # O(n)
        for j in range(1, len(list_obj)):  # O(n)
            if list_obj[j] < list_obj[i] and list_obj[j] < min_number:
                min_number = list_obj[j]

    return f'Минимальное число списка - {min_number}'


def min_value_list_2(list_obj):
    """Функция должна вернуть минимальное значение списка

    Алгоритм 2:
    Проходимся по списку и для каждого элемента проверяем, больше ли он этого элемента


    Сложность: Линейная (O(n))
    """
    min_number = list_obj[0]  # O(1)

    for element in list_obj:      # O(n)
        if min_number > element:  # O(1)
            min_number = element

    return f'Минимальное число списка - {min_number}'


for j in (0, 20):
    lst = sample(range(1, 500), j)

print(lst)
print(min(lst))  # Для проверки
print(min_value_list_1(lst))
print(min_value_list_2(lst))
