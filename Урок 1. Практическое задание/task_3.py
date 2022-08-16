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

def top_three_O_n_sq(firms, top_size=3):  # O(n^2)
    top, f = [], firms.copy()
    if len(f) <= top_size:
        return f
    else:
        while len(top) != top_size:
            k = list(f.keys())[list(f.values()).index(max(f.values()))]
            v = f[list(f.keys())[list(f.values()).index(max(f.values()))]]
            top.append({k: v})
            del f[k]
    return top

def top_three_O_n(firms, top_size=3):  # O(n)
    return sorted(firms.items(), key=lambda kv: kv[1])[::-1][:top_size]


if __name__ == '__main__':
    companies = {'Horns and hooves': 200_000,
                 'Flippers and tails': 500_000,
                 'Mars': 100_000,
                 'Space-X': 400_000,
                 'Bugulma': 900_000}

    print(top_three_O_n_sq(companies))
    print(top_three_O_n(companies))

    