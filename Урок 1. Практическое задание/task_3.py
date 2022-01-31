"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
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
#Сложность O(n**2)
company_info = {'rosneft': 473248, 'tatneft': 456000, 'lukoil': 90124, 'interpol': 1300005, 'neftegaz': 1940000} #O(1)
sorted_info=sorted(company_info.values()) #O(1)+O(nlogn)+O(1)
sorted_three=sorted_info[-3:] #O(n)
get_max = {k:v for k, v in company_info.items() if v in sorted_three} #O(n**2)
print(get_max)
#T(n)=1+1+nlogn+1+n+n**2=3+nlogn+2n**2

#Cложность O(nlogn)
info = {'rosneft': 473248, 'tatneft': 456000, 'lukoil': 90124, 'interpol': 1300005, 'neftegaz': 1940000} #O(1)
import operator
new_info=dict(sorted(info.items(), key=operator.itemgetter(1), reverse=True)[:3]) #O(nlogn)
print(new_info)

