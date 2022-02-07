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


def timer(func):
    def wrapper(*args):
        start = time.perf_counter()
        example = func(*args)
        finish = time.perf_counter()
        return example, f'время выполнения функции: {finish - start}'
    return wrapper

# a)
@timer
def create_list(count):
    lst = []
    for x in range(count):
        lst.append(x * 10)  # O(1)
    return lst


@timer
def create_dict(count):
    dct = {}
    for x in range(count):
        dct[x] = x * 10  # O(1)
    return dct


lst1, timer_lst1 = create_list(8)
print(lst1, type(lst1), timer_lst1)

dct1, timer_dct1 = create_dict(8)
print(dct1, type(dct1), timer_dct1)
print()

# У списка и словаря одинаковая сложность заполнения в О-нотациии О(1). Словарь заполняется медленнее, чем список,
# из-за того что еще уходит время на работу хэш функции.
# b)
@timer
def get_elem(data, key_or_index):
    elem = data[key_or_index] # 0(1)
    return elem


@timer
def delete_elem(data, key_or_index):
    data.pop(key_or_index)
    return data


elem_lst1, timer_elem_lst1 = get_elem(lst1, 1)
print(elem_lst1, timer_elem_lst1)

elem_dct1, timer_elem_dct1 = get_elem(dct1, 2)
print(elem_dct1, timer_elem_dct1)
print()

lst2 = delete_elem(lst1, 0)
print(lst2[0], type(lst2[0]), lst2[1])
dct2, timer_dct2 = delete_elem(dct1, 0)
print(dct2, type(dct2), timer_dct2)

# Сложности в O-нотации для операции получения элемента из списка и словаря одинаковые и равны О(1)
# Скорость выполнения операции получения элемента из списка и словаря приблизительно одинаковая
# Сложности в O-нотации для операции удаления элемента из списка и словаря: для списка - О(n), для словаря - О(1)
# Скорость выполнения операции удаления элемента из словаря  выше чем из списка,
# потому что словарь является хэш-таблицей, где данная операция имеет сложность в О нотации 0(1)
