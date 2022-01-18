"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
def min_1(list):   # O(n)
    min_elem = list[0]
    for i in range(len(list)-1):
        if min_elem > list[i]:
           min_elem = list[i]
    return min_elem

def min_2(list):    # O(n^2)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                sorted = False
    return(list[0])


test_list = [1,2,3,4,9,8,7,6,5,365,-5,12]
print(len(test_list))
print (min_1(test_list))
print (min_2(test_list))