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

import time


def timer_decorator(function):
   """Декоратор, засекает время."""
   def timer(*args, **kwargs):
      if NameError:
         None
      else:
         list_to_fill.clear()
      start = time.time()
      function(*args, **kwargs)
      stop = time.time()
      print(f"Время выполнения функции '{function.__name__}': {stop - start:.18f} сек")   
   return timer


def function_a():
   """Добавление элементов в начало (insert(0, i)) выполняется очень долго из-за сложности O(n^2), 
   остальные функции вставки действуют быстро."""
   
   elements = 100_000
   global list_to_fill
   list_to_fill = []

   @timer_decorator
   def appending_list():      
      for i in range(elements):  # O(n)
         list_to_fill.append(i)  # O(1)

   @timer_decorator
   def inserting_list_to_end():
      for i in range(elements):  # O(n)
         list_to_fill.insert(99999999999999, i)  # добавление в конец; # O(1) судя по времени, # O(n) судя по документу со сложностями операций из 2 урока.

   @timer_decorator
   def inserting_list_to_start():
      for i in range(elements):  # O(n)
         list_to_fill.insert(0, i)  # добавление в начало; # O(n)

   @timer_decorator
   def generator_list():
      generator_lst = [x for x in range(0, elements)]  # O(n)

   @timer_decorator
   def lambda_list():
      lambda_lst = [(lambda i: i) (i) for i in range (0, elements)]  # O(n)

   @timer_decorator
   def inserting_dictionary():
      dictionary = {}
      for i in range(elements):  # O(n)
         dictionary[i] = i  # O(1)
   
   return appending_list(), inserting_list_to_end(), inserting_list_to_start(), generator_list(), lambda_list(), inserting_dictionary() ,print("")
   

def function_b():
   """Поиск по значению (в словаре по ключу) и изменение происходит очень быстро как в списке, так и в словаре."""
   elements = 1_000
   filled_list = [i for i in range(0, elements)]
   filled_dictionary = {i: i for i in range(elements)}
   
   @timer_decorator
   def change_list_elem():
      for i in filled_list[200:300]:  # O(n)
         filled_list[i] = 'hello'  # O(1)

   @timer_decorator
   def change_dictionary_elem():
      for i in range(230, 550):  # O(n)
         filled_dictionary[i] = 'hello'  # O(1)
      
      
   return change_list_elem(), change_dictionary_elem(), print('')


def function_c():
   """Удаление не с конца, а с указанием индекса, происходит у функций pop(i) и remove(i) со сложностью O(n^2),
   остальные функции справляются быстро."""
   elements = 200_000
   filled_list = [i for i in range(0, elements)]
   filled_dictionary = {i: i for i in range(elements)}

   @timer_decorator
   def pop_list():
      for i in range(30_000):  # O(n)
         filled_list.pop()  # O(1)

   @timer_decorator
   def pop_list_from_start():
      for i in filled_list[:30_000]:  # O(n)
         filled_list.pop(i)   # O(n)

   @timer_decorator
   def del_list():
      del filled_list[80_000:120_000]  # O(n)

   @timer_decorator
   def remove_list():
      for i in filled_list[:30_000]:  # O(n)
         filled_list.remove(i)  # O(n)

   @timer_decorator
   def pop_dictionary():
      for i in range(30_000):  # O(n)
         filled_dictionary.pop(i)  #O(1)

   return pop_list(),pop_list_from_start(), del_list(), remove_list(), pop_dictionary()   


function_a()
function_b()
function_c()  
