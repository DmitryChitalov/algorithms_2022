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

dict = [{'company':'МРОК', 'income': 100},
        {'company':'МРАК', 'income': 200},
        {'company':'МРЕК', 'income': 300},
        {'company':'МРУК', 'income': 400},
        {'company':'МРЫК', 'income': 500}
    ]

def first(dict): #O(1)
    max = 0 #O(1)
    max_key = -1 #O(1)
    newDict = [] #O(1)
    for key in range(len(dict)): #O(n)
        if dict[key]['income'] > max: #O(1)
            max = dict[key]['income'] #O(1)
            max_key = key #O(1)
            

    newDict.append(dict.pop(max_key)) #O(1)
    if(len(dict) > 0): #O(1)
        newDict2 = first(dict) #O(2^n)
        newDict = newDict + newDict2 #O(1)
    
    return newDict #O(1)

top = first(dict)
print(top[0:3])
#O(2^n)


dict = [{'company':'МРОК', 'income': 100},
        {'company':'МРАК', 'income': 200},
        {'company':'МРЕК', 'income': 300},
        {'company':'МРУК', 'income': 400},
        {'company':'МРЫК', 'income': 500}
    ]

def second(dict):
   
    
    newDict = [] #O(1)
    for i in range(len(dict)): #O(n)
        max = 0 #O(1)
        max_key = -1 #O(1)
        for b in range(len(dict)): #O(n^2)
            if dict[b]['income'] > max:  #O(1)
                max = dict[b]['income'] #O(1)
                max_key = b #O(1)
                
            
        newDict.append(dict.pop(max_key)) #O(1)
    return newDict #O(1)
    
top = second(dict) #O(1)
print(top[0:3]) #O(b -a)
#O(n^2)