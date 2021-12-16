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
DATA_COMPANY_1 = {
    'Apple': 456184.544,
    'Samsung': 1565362.56,
    'Xiaomi': 415651.5658,
    'Huawei': 45783.43,
    'LG': 4642,
    'Asus': 6952894,
    'Acer': 456567
}
DATA_COMPANY_2 = {
    'yandex': 2000,
    'gazprom': 500,
    'microsoft': 2300,
    'perecrestok': 5400,
    'rosnano': 10,
    'appel': 2000,
    'biocad': 4030,
    'apteka': 299,
    'hiomi': 569,
    'wacom': 8901,
    'adidas': 4313,
    'acron': 6703
}


# O(N * logN)
def solve_1(dictionary: dict):
    """
    Функция нахождения 3 наибольших значений в словаре.
    Методом сортировки значений словаря, форматируя его в список.

    Сложность: O(N * logN)
    :param dictionary: dict()
    :return: list()
    """
    result = list(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))  # O(N * logN)
    return result[:3]


#  O(N^2)
def solve_2(dictionary: dict):
    maxes = {}  # O(1)
    for k in dictionary.keys():  # O(N)
        max_ = dictionary.get(k)  # O(1)
        for k2 in dictionary.keys():  # O(N)
            if max_ < dictionary.get(k2):  # O(1)
                max_ = dictionary.get(k)  # O(1)
            maxes[k] = max_  # O(1)
    return list(sorted(maxes.items(), key=lambda v: v[1], reverse=True))[:3]  # O(1)


if __name__ == '__main__':
    assert solve_1(DATA_COMPANY_1) == [('Asus', 6952894), ('Samsung', 1565362.56), ('Acer', 456567)]
    print(solve_1(DATA_COMPANY_1))
    assert solve_1(DATA_COMPANY_2) == [('wacom', 8901), ('acron', 6703), ('perecrestok', 5400)]
    print(solve_2(DATA_COMPANY_2))
