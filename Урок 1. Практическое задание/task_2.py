"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
#chek_1
my_list = [700, 22, 20, 3, 55, 28, 15]        #O(1)
min_number = my_list[0]                       #O(1)
for i in my_list:                             #O(n)
    for j in range(my_list.index(i) + 1, len(my_list) - 1, 1): #O(n)
        if min_number > my_list[j]:           #O(len(n))
            min_number = my_list[j]           #O(1)
print(min_number)

#chek_2
my_list = [700, 22, 20, 3, 55, 28, 15]
min_number = my_list[0]                     #O(1)
for i in my_list:                           #O(n)
    if i < min_number:                      #O(len(i))
        min_number = i                      #O(1)
print(min_number)
