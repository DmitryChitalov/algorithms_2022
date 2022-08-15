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

companies_year_income = {
    'coffee_shop': 1209000,
    'icecream_factoru': 160000,
    'hr_agency': 2153322,
    'car_repair': 1859921,
    'pr_agency': 1272001,
    'private_school': 2104321
}


def first_way(companies: dict) -> list:
    """Функция принимает в себя словарь с компаниями и значениями их годовых прибылей.
    И возвращает три компании с наибольшей прибылью. Требование сортировки прибыли в ТЗ отсутствует
    PS: Можно было бы и в 1 строчку, но это совсем уже не читаемо"""
    top_income = sorted(list(companies.values()), reverse=True)[:3]
    return [key for key, value in companies.items() if value in top_income]


print(*first_way(companies_year_income))


def second_way(companies: dict):
    """ Функция принимает в себя словарь с компаниями и значениями их годовых прибылей.
    Перебирает в цикле все значения словаря, и сравнивает их с максимальными,
    если значение больше хотя бы одного максимального, то значение заменяет его, а другие значения смешаются на 1
    И возвращает три компании с наибольшей прибылью, отсортированные по убыванию величины дохода
    """
    first, second, third = '', '', ''
    max_1, max_2, max_3 = 0, 0, 0
    for key, value in companies.items():
        if value > max_1:
            max_1, max_2, max_3 = value, max_1, max_2
            first, second, third = key, first, second
        elif value > max_2:
            max_2, max_3 = value, max_2
            second, third = key, second
        elif value > max_3:
            max_3 = value
            third = key
    return first, second, third


print(*second_way(companies_year_income))


def third_way(companies: dict):
    """ Функция принимает в себя словарь с компаниями и значениями их годовых прибылей.
    Создает из ключей и значений словаря два упорядоченных списка. В цикле заполняет значение максималього
    ключа по индексу макимального значения. И возвращает три компании с наибольшей прибылью,
    отсортированные по убыванию величины дохода."""
    keys = list(companies.keys())
    values = list(companies.values())
    max_key = []
    while len(max_key) < 3:
        for i in range(len(values)):
            if values[i] == max(values):
                max_key.append(keys[i])
                values[i] = 0
                break
    return max_key


print(*third_way(companies_year_income))
