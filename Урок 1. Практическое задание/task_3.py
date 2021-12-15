"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!



ВЫВОДЫ:
первая реализация самая удачная по параметру: асимптотическая сложность, плюс у меня есть некая уверенность что она
будет еще быстрее за счет того, что функция sorted реализована не на пайтоне

Все процедуры выводят данные в разном формате, т.к. формат вывода в задании не указан.
"""


# Вариант 1, встроенная сортировка, O(nlogn)
def variant1(vault):
    vault_gen = iter(sorted(vault.items(), reverse=True, key=lambda profit: profit[1]))  # O(nlogn)
    for i in range(3):  # O(1)
        print(next(vault_gen))  # O(1)


# Вариант 2, с промежуточным списком, O(n)
def variant2(vault):
    r_list = [('', 0), ('', 0), ('', 0)]  # O(1)
    for k, v in vault.items():  # O(n)
        for i in range(3):  # O(1)
            if v > r_list[i][1]:  # O(1)
                r_list.insert(i, (k, v))  # O(1)
                r_list.pop()  # O(1)
                break  # O(1)
    print(r_list)


# Вариант 3, сортировка пузырьком, O(n^2)
def variant3(vault):
    # keys = list(vault.keys())  # O(n)
    vault_sort = [(k, v) for k, v in vault.items()]  # O(n)
    for i in range(len(vault_sort)):  # O(n) * O(n)
        m, idxm = vault_sort[0][1], 0  # O(1)
        for j in range(len(vault_sort) - i):  # O(n)
            if m > vault_sort[j][1]:  # O(1)
                m, idxm = vault_sort[j][1], j  # O(1)
        vault_sort[idxm], vault_sort[j] = vault_sort[j], vault_sort[idxm]  # O(1)

    vault_iter = iter(vault_sort)  # O(1)
    for i in range(3):  # O(1)
        print(next(vault_iter))  # O(1)


if __name__ == "__main__":

    vault = {'Umbrella': 1500,
             'SIGSON': 2500,
             'LaMerk Industries': 4500,
             'Rupture Farms': 500,
             'Aesir Corporation': 4500,
             'Page Industries': 500,
             'Black Mesa': 1921,
             'Vault - Tec': 2534}

    print('Variant 1:')
    variant1(vault)

    print('Variant 2:')
    variant2(vault)
    
    print('Variant 3:')
    variant3(vault)
