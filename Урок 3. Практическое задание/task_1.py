"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
from re import L
import time
import timeit

def time_counter(*, rep = 1):
      def time_counter_inner1(func):
         def time_counter_inner2(*args, **kwargs):
            num_outer = kwargs.get('num_outer', 0)
            def extra_time_inner(n=1):
               def foo():
                  pass
               start = time.perf_counter()
               for i in range(n):
                  foo()
               trimming_time = time.perf_counter() - start
               return trimming_time

            def extra_time_outer(n=1):
               start = time.perf_counter()
               for i in range(n):
                  pass
               trimming_time = time.perf_counter() - start
               return trimming_time

            start = time.perf_counter()
            for i in range(rep):
               result = func(*args, **kwargs)
            stop = time.perf_counter()
            elapsing_time = stop - start - extra_time_inner(rep) - extra_time_outer(num_outer)
            print(f'{func.__name__} time: '
                  f'{elapsing_time} with repetition {rep}') 
            return result
         return time_counter_inner2
      return  time_counter_inner1

@time_counter(rep=100)
def completing_a_list_1_to_n(n, *args, **kwargs):
   list_ = []
   for num in range(n):
      list_.append(num)
   return list_

@time_counter(rep=100)
def completing_a_dict_1_to_n(n, *args, **kwargs):
   dict_ = {}
   for num in range(n):
      dict_[num] = num 
   return dict_ 

list_ = completing_a_list_1_to_n(n=10**4, num_outer=10**4)
# completing_a_list_1_to_n time: 0.04792860004818067 with repetition 100
list_ = completing_a_list_1_to_n(n=10**5, num_outer=10**5)
# completing_a_list_1_to_n time: 0.5744009999907576 with repetition 100
dict_ = completing_a_dict_1_to_n(n=10**4, num_outer=10**4)
#completing_a_dict_1_to_n time: 0.0777475000359118 with repetition 100
dict_ = completing_a_dict_1_to_n(n=10**5, num_outer=10**5)
#completing_a_dict_1_to_n time: 0.8673404000001028 with repetition 100

# Время заполения списка растет линейно в зависимости от числа элементов
# Время заполения словаря растет почти линейно в зависимости от числа элементов
# Сложность вставки элемента в список в O-нотации - O(1)
# Сложность вставки элемента в словарь в O-нотации - O(1)
# Скорость заполенения у списка несколько быстрее чем у словаря

@time_counter(rep=10**4)
def update_element_in_list(list_, index, value):
   list_[index] = value

@time_counter(rep=10**4)
def update_element_in_dict(dict_, key, value):
   dict_[key] = value

update_element_in_list(list_, index=0, value=123)
# update_element_in_list time: 0.0011893000337295234 with repetition 10000
update_element_in_dict(dict_, key=0, value=123)
# update_element_in_dict time: 0.001415699953213334 with repetition 10000

@time_counter(rep=10**5)
def update_element_in_list(list_, index, value):
   list_[index] = value

@time_counter(rep=10**5)
def update_element_in_dict(dict_, key, value):
   dict_[key] = value

update_element_in_list(list_, index=0, value=123)
# update_element_in_list time: 0.012810799991711974 with repetition 100000
update_element_in_dict(dict_, key=0, value=123)
# update_element_in_dict time: 0.01361740002175793 with repetition 100000


# Время вставки элеметов в список растет линейно в зависимости от числа элементов
# Время вставки элеметов в словарь растет линейно в зависимости от числа элементов
# Сложность вставки элемента в список в O-нотации - O(1)
# Сложность вставки элемента в словарь в O-нотации - O(1)
# Скорость вставки элемента в список немного быстрее чем в словарь

del_elements_in_list_1_to_10000 = """
for i in range(10000):
   del list_[0] """

del_elements_in_dict_1_to_10000 = """
for i in range(10000):
   del dict_[i] """


time_for_del_elements_in_list_1_to_10000 = timeit.timeit(stmt=del_elements_in_list_1_to_10000, globals=globals(), number=1)
time_for_del_elements_in_dict_1_to_10000 = timeit.timeit(stmt=del_elements_in_dict_1_to_10000, globals=globals(), number=1)

print(f'{time_for_del_elements_in_list_1_to_10000=}')
print(f'{time_for_del_elements_in_dict_1_to_10000=}')

# Скорость удаления у словаря(O(1)) значительно быстрее чем у списка(O(n))
# В словаре ключ находится по хэшу, соотвественно его не надо искать перебором
# В списке значение находится по индексу, поэтому если необходимо взять 
# не последний элемент в списке, то элементы приходится перебирать по одному.
# Поэтому если требуется удалять значния из списка или брать произвольное значение, 
# то выгоднее брать либо последний элемент, либо близко к нему




