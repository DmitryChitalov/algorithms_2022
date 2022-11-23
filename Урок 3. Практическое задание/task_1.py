"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from time import time

def calculate_time(func):
   # Расчитать время выполнения функции 
   def __wrapper(*args, **kwargs):
      start_time = time()
      func_result = func(*args, *kwargs)
      end_time = time()
      print(f"\nВрмя выполнения функции {func.__name__} составило: {end_time - start_time:0.5f}")
      return func_result
   return __wrapper


# a) -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

@calculate_time
def fill_list_append(lst, lenght):     # Общая сложность O(n)
   for item in range(lenght):          # O(n)
      lst.append(item)                 # O(1)

@calculate_time
def fill_list_appfront(lst, lenght):   # Общая сложность O(n^2)
   for item in range(lenght):          # O(n)
      lst.insert(0, item)              # O(n)

@calculate_time
def fill_dict(dct, lenght):          # Общая сложность O(n)
   for item in range(lenght):          # O(n)
      dct[item] = item                 # O(1)

# b) -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

@calculate_time
def get_items_from_list(lst):          # Общая сложность O(n)
   for item in range(len(lst)):        # O(n)
      tmp = lst[item]                  # O(1)

@calculate_time
def get_items_from_dict(dct):          # Общая сложность O(n)
   for item in range(len(dct)):        # O(n)
      tmp = dct[item]                  # O(1)

# c) -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

@calculate_time
def del_items_from_list(lst):          # Общая сложность O(1)
   while lst:                          # O(1)
      lst.pop()                        # O(1)

@calculate_time
def del_items_from_dict(dct):          # Общая сложность O(n)
   for item in range(len(dct)):        # O(n)
      dct.pop(item)                    # O(1)

if __name__ == "__main__":
   lenght = 10000
   new_list_append = []
   new_list_appfront = []
   new_dct_1 = {}
   print("\na)-=-=-=-=-=-==-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-")
   fill_list_append(new_list_append, lenght)
   fill_list_appfront(new_list_appfront, lenght)
   fill_dict(new_dct_1, lenght)
   # Словарь представляет из себя хеш-таблицу, его заполнение происходит быстрее чем списка
   # Врмя выполнения функции fill_list_append составило: 0.00283
   # Врмя выполнения функции fill_list_appfront составило: 0.02928
   # Врмя выполнения функции fill_dict составило: 0.00336

   print("\nb)-=-=-=-=-=-==-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-")
   get_items_from_list(new_list_append)
   get_items_from_dict(new_dct_1)
   # Скорость получения элемента приблизительно одинакова для словаря и списка
   # Врмя выполнения функции get_items_from_list составило: 0.00264
   # Врмя выполнения функции get_items_from_dict составило: 0.00285

   print("\nc)-=-=-=-=-=-==-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-")
   del_items_from_list(new_list_append)
   del_items_from_dict(new_dct_1)
   # Скорость удаления элементов списка происходит быстрее, так как в словаре происходит вычисление хеша
   # Врмя выполнения функции del_items_from_list составило: 0.00224
   # Врмя выполнения функции del_items_from_dict составило: 0.00420