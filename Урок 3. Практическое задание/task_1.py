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
import time
import timeit

def time_counter(*, rep = 1):
    def time_counter_inner1(func):
        def time_counter_inner2(*args, **kwargs):
            start = time.perf_counter()
            for i in range(rep):
               result = func(*args, **kwargs)
            print(f'{func.__name__} time: '
                  f'{time.perf_counter() - start} with repetition {rep}') 
            return result
        return time_counter_inner2
    return  time_counter_inner1


@time_counter(rep=100)
def completing_a_list_1_to_100000():
   list_ = []
   for num in range(10**5):
      list_.append(num)
   return list_

@time_counter(rep=100)
def completing_a_dict_1_to_100000():
   dict_ = {}
   for num in range(10**5):
      dict_[num] = num 
   return dict_ 
   

list_ = completing_a_list_1_to_100000()
dict_ = completing_a_dict_1_to_100000()

# Скорость заполенения у списка и у словаря абсолютно одинаковые

@time_counter(rep=100000)
def update_element_in_list(list_, index, value):
   list_[index] = value

@time_counter(rep=100000)
def update_element_in_dict(dict_, key, value):
   dict_[key] = value

update_element_in_list(list_, 0, 123)
update_element_in_dict(dict_, 0, 123)

# Скорость изменений значений у списка и у словаря абсолютно одинаковые

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




