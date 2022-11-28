"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

def company_1(x):
    one = 0
    two = 0
    three = 0 #3n
    for i, v in dict_.items(): #O(n)
        if int(v) > one: #O(len(dict_))
            two = one    #O(1)
            one = int(v) #O(1)
        elif int(v) > two: #O(len(dict_))
            three = two # O(1)
            two = int(v) # O(1)
        elif int(v) > three: # O(len(dict_))
            three = int(v) # O(1)
    return one, two, three # O(1)

dict_ = {'компания1': '3000000',
         'компания2': '5000000',
         'компания3': '2000000',
         'компания4': '4000000'}

for i in company_1(dict_): #(On)
    for a, x in dict_.items(): # O(On)
        if str(i) == x: # O(len(s))
            print(f'{a}, годовая прибыль: {x}')
#Tn = n**7+9
# или Tn = n**3+13
# или O(n**4)
print(10*'*')
#####################################
one = 0
two = 0
three = 0 #3n
for i, v in dict_.items(): #O(n)
    if int(v) > one: #O(len(dict_))
        two = one    #O(1)
        one = int(v) #O(1)
    elif int(v) > two: #O(len(dict_))
        three = two # O(1)
        two = int(v) # O(1)
    elif int(v) > three: # O(len(dict_))
        three = int(v) # O(1)

for i, v in dict_.items(): #O(n)
    if int(v) == one: # O(len())
        print(i, v)
    elif int(v) == two: # O(len())
        print(i, v)
    elif int(v) == three: # O(len())
        print(i, v)

#Tn = n**2+14
#или Tn = n**8+8
#или O(n**2)
print(10*'*')
##################################
res = []
for i, v in dict_.items(): #O(n)
    res.append(int(v)) #O(1)
max_val = sorted(res)[::-1][:3] #O(n log n)
for i in max_val: #O(n)
    for x, j in dict_.items(): #O(n)
        if str(i) == j: #O(len())
            print(f'{x}, годовая прибыль {j}')
#Tn = n**3+n log n + 2
#O(n**5)
print(10*'*')
####################################
company_list = sorted([int(v) for i, v in dict_.items()])[-3:] #O(n**2)
for i in company_list: #O(n)
    for x, j in dict_.items(): #O(n)
        if str(i) == j: #O(len())
            print(f'{x}, годовая прибыль {j}')

#O(n**4)
print(10*'*')
#############################################
def bubble_sort(list_):
    has_swapped = True
    while (has_swapped):
        has_swapped = False
        for i in range(len(list_) - 1):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                has_swapped = True
    return list_[-3:]

company_list = [int(v) for i, v in dict_.items()]
for i in bubble_sort(company_list):
    for x, j in dict_.items():
        if str(i) == j:
            print(f'{x}, годовая прибыль {j}')

#сложность O(n**4)
# Считаю это решение самым эффективным









