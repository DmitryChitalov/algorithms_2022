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


# создадим словарь: ключ - название компании, значение - годовая прибыль
from random import randint, choice

names = []
dict_companies = {}
for i in range(1, 10):
    names.append('Company_' + str(i))
for name in names:
    dict_companies[name] = randint(10000, 10000000)
print(dict_companies)

# назвала бы это решение самым эффективным. Линейная сложность и наиболее читабельный код
def three_max(**dict_comp):  # O(N)
    """
    Функция реализует поиск трёх компаний с наибольшей годовой прибылью.
    подвох с одинаковыми суммами прибылей
    :param dict_comp: dict
        словарь из ключей - названий компаний со значениями - годовой прибыли
    :return: list
        возвращает список из 3 названий компаний с наибольшей прибылью
    """

    lst_rich = []  # будущий список 3 богатейших компаний
    while len(lst_rich) <= 2:
        # выбираем название компании, с которого начнём сравнивать и находим её прибыль
        key_max = list(dict_comp)[0]  # O(N)
        max = dict_comp[key_max]  # O(1)
        # перебираем ключи-компании и сравниваем прибыль, если больше, меняем референс
        for key in dict_comp.keys():  # O(N)
            if dict_comp[key] > max:  # O(1)
                max = dict_comp[key]  # O(1)
                key_max = key  # O(1)
        lst_rich.append(key_max)  # O(1)
        del dict_comp[key_max]  # O(1)
    return lst_rich  # O(1)


print(three_max(**dict_companies))


# создадим список кортежей вида (название компании, прибыль)
tuples_companies = []
for name in names:
    tuples_companies.append((name, randint(10000, 10000000)))
print(tuples_companies)

# небольшая рекурсия, бессмысленно и беспощадно
def three_max_1(**dict_comp): # O(2^N)
    """
    :param dict_comp: dict
        словарь из ключей - названий компаний со значениями - годовой прибыли
    :return: tuple(название компании, прибыль)
        кортеж из названия компании и прибыли
    """
    if len(dict_companies) - len(dict_comp) < 3: # O(1)
        # берём кортежи из названия и прибыли и ищеем максимум по прибыли
        max_val = max(dict_comp.items(), key=lambda x: x[1]) # O(N)
        del dict_comp[max_val[0]] # O(1)
        print(max_val) # O(1)
        return three_max_1(**dict_comp) # O(2^N)


three_max_1(**dict_companies)


def three_max_2(tuple_comp): # O(NlogN)
    """
    :param tuple_comp: list
        список кортежей вида (название компании, прибыль)
    :return:
    """
    sorted_tuple_comp = sorted(tuple_comp, key=lambda x: x[1]) # O(NlogN)
    return sorted_tuple_comp[2], sorted_tuple_comp[1], sorted_tuple_comp[0] # O(1)

print(three_max_2(tuples_companies))
