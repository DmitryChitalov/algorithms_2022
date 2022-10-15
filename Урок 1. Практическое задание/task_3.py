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
companies = {
  'PUPU' : 100000,
  'Annino' : 435000,
  'FOrk' : 156784243,
  'Work' : 6870267,
  'MiuMiu' : 98260234,
  'WOW!' : 5176891513465
}

def first_func(dict_of_companies):
  maximum = int()
  for i in dict_of_companies:
    if dict_of_companies[i] > maximum:
      company1 = i
      maximum = dict_of_companies[i]
  maximum = int()
  for i in dict_of_companies:
    if dict_of_companies[i] > maximum and dict_of_companies[i] < company1:
      company2 = i
      maximum = dict_of_companies[i]
  maximum = int()
  for i in dict_of_companies:
    if dict_of_companies[i] > maximum and dict_of_companies[i] < company2:
      company3 = i
      maximum = dict_of_companies[i]
  return company1, company2, company3


def second_func(dict_of_companies):
  dict_of_companies_copy = dict_of_companies.copy()
  maximum = max(dict_of_companies_copy.values())
  company1 = {k:v for k, v in dict_of_companies_copy.items() if v == maximum}
  del dict_of_companies_copy[company1]
  maximum = max(dict_of_companies_copy.values())
  company2 = {k:v for k, v in dict_of_companies_copy.items() if v == maximum}
  del dict_of_companies_copy[company2]
  maximum = max(dict_of_companies_copy.values())
  company3 = {k:v for k, v in dict_of_companies_copy.items() if v == maximum}
  del dict_of_companies_copy[company3]
  return company1, company2, company3


def third_func(dict_of companies):
  pass



