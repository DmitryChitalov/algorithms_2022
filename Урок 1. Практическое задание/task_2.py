"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.
"""
# Сложность: O(n^2)

def min_val_ver1(list_of_values: list) -> str:
  min = list_of_values[0]
  for i in range(0, len(list_of_values)): # O(n)
    for k in range(0, len(list_of_values)): # O(n)
      if list_of_values[i] <= list_of_values[k]: # O(1)
        if list_of_values[i] <= min: # O(1)
          min = list_of_values[i] # O(1)
  return min # O(1)


"""
Сложность второго алгоритма должна быть O(n) - линейная.
"""
# Сложность: O(n)

def min_val_ver2(list_of_values: list) -> str:
  min = list_of_values[0] # O(1)
  for i in range(1, len(list_of_values)): # O(n)
    if list_of_values[i] < min:# O(1)
      min = list_of_values[i] # O(1)
  return min # O(1)
  
"""
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""
