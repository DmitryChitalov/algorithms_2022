"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.


Долгно думал так и не придумал как цикл в цикле зафигачить на сие задачу

Сложность второго алгоритма должна быть O(n) - линейная.

ls = [5, 120, 10, 3, 52]

ln = ls[0]

for i in ls:
    if i < ln:
        ln = i

print("Минимальное значение: ", ln)


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
