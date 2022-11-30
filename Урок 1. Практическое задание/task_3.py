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

companies = { 'Rohan-Lemke':47,'Beatty-Muller':4000001614,'Murray-Feest':5683231,'Flatley Inc':72049577,'Kuphal, Treutel and Jacobi':2435,
         'Kuphal-Nikolaus':68259,'Torphy, Schmidt and O\'Conner':6880000008599,'Ritchie, Osinski and Reichert':231,
         'Bogisich, Beier and Quigley':36056,'Jacobs, Lueilwitz and Howell':2,'Metz LLC':2410,'Cartwright-Krajcik':81,
         'Schaefer-Goodwin':235294,'Bogisich Group':918432320,'Hickle Group':602244022,'Kshlerin LLC':2318099
}

# Вариант 1 сложность O(n)
def maxprofit1 (data):
    profit=companies.copy() # O(n)
    max_com=[] # O(1)
    for i in range(3): # O(1)
        max_com.append(list(profit.keys())[list(profit.values()).index(max(list(profit.values())))]) # O(N) + O(N) + O(N)+O(N)+O(N)+ O(1)+O(N)+O(N)+O(1) + +O(1)
        profit.pop(list(profit.keys())[list(profit.values()).index(max(list(profit.values())))]) #O(N) + O(N) + O(N)+O(N)+O(N)+ O(1)+O(N)+O(N)+O(1) + +O(1)
    return max_com # O(1)

# Вариант 2 сложность O(n^2)
def profit2 (data):
    max_com=[]  # O(1)
    profit2=companies.copy() # O(n)
    for i in range (3):   # O(1)
        for key,val in companies.items(): # O(n)
            if val == max(profit2.values()): # O(n)
                max_com.append( key) # O(1)
                profit2.pop(key)    #O(1)
                break # O(1)
    return max_com # O(1)

print (maxprofit1(companies))
print (profit2(companies))










