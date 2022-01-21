"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
my_list = [-3, 1, 4, 3, -9, 0, -2, 0, -2, 8, 2]

# O(n^2)
# До этого решения было сложнее додуматься

for i in my_list:
    el_min = i
    for j in my_list:
        if el_min > j:
            el_min = j
print(f'Минимальный элемент (O(n^2)) {el_min}')


# O(n)

el_min = 0
for i in my_list:
    if i < el_min:
        el_min = i
print(f'Минимальный элемент (O(n)) {el_min}')
