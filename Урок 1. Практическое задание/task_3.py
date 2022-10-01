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
def bubble_sort(nums):                                                      #O(n^2)
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True                                                          #O(1)
    while swapped:                                                          #O(n)
        swapped = False
        for i in range(len(nums) - 1):                                      #O(n)
            if nums[i] > nums[i + 1]:                                       #O(1)
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]                 #O(1)
                # Устанавливаем swapped в True для следующей итерации
                swapped = True                                              #O(1)




def sort_1 (inp_dict):                                                         # O(n log n)
    sort_dict = {}                                                              # O(1)
    sort_keys = sorted(inp_dict, key = inp_dict.get, reverse=True)[0:3]         # O(n log n + 3)

    for k in sort_keys:                                                         # O(n)
        sort_dict[k] = inp_dict[k]                                              # O(1)

    return sort_dict                                                            # O(1)



def sort_2 (inp_dict):                                                              # O(n log n)
    sort_tuple = sorted(inp_dict.items(), key = lambda x: x[1], reverse = True)     # O(n log n)
    sort_dict = dict(sort_tuple[0:3])                                               # O(3)

    return sort_dict                                                                # O(1)

def sort_3 (inp_dict):                          #O(n^2)
    inp_lst = list(inp_dict.items())            #O(n)
    lst = []                                    #O(1)

    for i in inp_lst:                           #O(n)
        lst.append(i[1])                        #O(1)

    bubble_sort(lst)                            #O(n^2)
    lst = lst[-1:-4:-1]                         #O(n)
    return lst


# def sort_4 (inp_dict):
#     sort_dict={}
#     sort_dict = {x: y for x, y in filter(lambda x: inp_dict[x[0]] == max(inp_dict.values()), inp_dict.items())}
#     return sort_dict


companies = {
    'Toyota': 10000,
    'Renault': 60000,
    'Audi': 80000,
    'BMW': 150000,
    'Citroen': 55000,
    'Hyundai': 75000,
    'Skoda': 65000
}

print(sort_1(companies))
print(sort_2(companies))
print(sort_3(companies))