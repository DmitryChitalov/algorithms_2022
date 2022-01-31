"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

#Сложность O(n**2)
def get_min(lst):
    min_el=lst[0] #O(1)
    for i in range(len(lst)): #O(n)
        if min_el>=lst[i]: #O(n)
            min_el=lst[i] #O(1)
    return min_el #O(1)

#T(n)=1+n*n+1+1=3+n**2

print(get_min([2,34,-15,4,6]))

#Сложность O(n**3)
def get_min1(lst):
    i = 0 #O(1)
    j = i + 1 #O(1)

    for x in range(len(lst)-1): #O(n)
        if lst[i] > lst[j]: #O(n)
            lst.pop(i) #O(n)

        elif lst[j] > lst[i]: #O(n)
            lst.pop(j) #O(n)

        elif lst[i]==lst[j]: #O(n)
            lst.pop(i) #O(n)

    return lst #O(1)
print(get_min1([9,35,9,23,66]))
#T(n)=1+1+n*n*n+1=3+n**3

#Сложность O(n)
def get_min2(lst):
    min=lst[0] #O(1)
    for val in lst: #O(n)
        if val<min: #O(1)
            min=val #O(1)
    return min #O(1)
#T(n)=1+n+1+1+1=3+n
print(get_min2([12, 25,258,-25,12]))
