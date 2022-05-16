"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
# Решение larg_prof_3 эффективнее в плане производительности.

def get_key(my_dict : [dict], value : [int]) -> int: #O(n)
    for k, v in my_dict.items(): #O(n)
        if v == value: # O(1)
            return k # O(1)


def larg_prof_3(obj : [dict]) -> tuple: # O(n))
    cop_obj=obj.copy() # O(n)
    fst = max(cop_obj.values()) # O(n)
    n_fst = get_key(cop_obj, fst) # O(n)
    cop_obj.pop(n_fst) # O(1)
    sec = max(cop_obj.values())
    n_sec = get_key(cop_obj, sec)
    cop_obj.pop(n_sec)
    thr = max(cop_obj.values())
    n_thr = get_key(cop_obj, thr)
    cop_obj.pop(n_thr)
    return n_fst, n_sec, n_thr # O(3)

def larg_prof_3_sec(obj : [dict]) -> list: # O(nlogn)
    obj_val = sorted(obj.values(), reverse=True) #O(nlogn)
    sorted_obj = [] # O(n)
    for v in obj_val: # O(n)
        sorted_obj.append(get_key(obj,v)) # O(n)
    return sorted_obj[:3] # O(3)




info = {
    1:1000,
    2:41434,
    3:871374187,
    4:1873,
    5:21938981,
    6:123123,
}

print(larg_prof_3(info))
print(larg_prof_3_sec(info))

