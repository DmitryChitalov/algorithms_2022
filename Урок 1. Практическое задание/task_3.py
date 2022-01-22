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

COMPANIES = {'OOO "Ньютон"': 123456,
             'АО "Эйнштейн"': 123321,
             'OOO "Рога и копыта"': 123123,
             'ЗАО "Лидер"': 654321}


# короче код и выполнение линейно зависит о числа элементов,
# для получения отсортированного словаря используется генераторное выражение
def companies_found_1(companies, my_count):
    """
    Функция вывода my_count лидеров по годовой прибыли:
    сложность линейная O(n)
    """
    i = 1  # O(1)

    # O(n) + O(n log n) + O(1) + O(1) -> O(n)
    gen = (item for item in sorted(companies.items(), key=lambda x: x[1], reverse=True))

    while i <= my_count:  # O(1)
        print(next(gen))  # O(1)
        i += 1  # O(1)


if __name__ == '__main__':
    companies_found_1(COMPANIES, 3)


# вместо цикла использован рекурсивный вызов, хотя циклом было бы быстрее
def companies_found_2(companies):
    """
    Функция вывода трех лидеров по годовой прибыли:
    сложность линейная O(n)
    """
    best_companies = companies.copy()  # O(n)
    min_item = min(best_companies.items(), key=lambda x: x[1])  # O(n)
    if len(companies) <= 3:  # O(1)
        return best_companies  # O(1)
    del best_companies[min_item[0]]  # O(1)
    return companies_found_2(best_companies)  # O(n)


if __name__ == '__main__':
    print(companies_found_2(COMPANIES))


# вариант из разбора
def companies_found_3(companies):
    """
    Функция вывода трех лидеров по годовой прибыли:
    сложность линейно-логарифмическая O(n log n)
    """
    companies_list = list(companies.items())  # O(1)
    companies_list.sort(key=lambda x: x[1], reverse=True)  # O(n log n)
    for i in range(3):  # O(1)
        print(companies_list[i])  # O(1)


if __name__ == '__main__':
    companies_found_3(COMPANIES)
