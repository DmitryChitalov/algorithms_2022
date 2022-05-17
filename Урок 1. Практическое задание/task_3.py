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
from random import randint


def findmax3_n(seqence: list[tuple]) -> list:  # Сложность: # O(N)
    result = []
    temp_list = seqence.copy()  # O(N)
    for i in range(3):  # O(1)

        index_of_iter = 0  # O(1)
        # Обходим список и удаляем последователь каждое максимальное занчение 3 раза, добавляя в результат
        for j in range(len(temp_list)):  # O(N)
            if temp_list[j][1] > temp_list[index_of_iter][1]:  # O(1)
                index_of_iter = j  # O(1)
        result.append(temp_list.pop(index_of_iter))  # O(1)
    return result


def findmax3_n_log_n(seqence: list[tuple]) -> list:  # Сложность: O(N*LOG N)
    # Сортируем список и выдаём три последних значения
    # Конструктор потому, что мне нравятся конструкторы
    return sorted(seqence, key=lambda x: x[1], reverse=True)[0:3]  # O(N*LOG N)


Company_count = 10  # Количество компаний
Profit_range = (100, 4000)  # Диапазон прибыли
companies = [(f'Компания №{Company + 1}', randint(*Profit_range)) for Company in
             range(Company_count)]  # формируем список компаний
print(companies)
print(findmax3_n(companies))
print(findmax3_n_log_n(companies))
