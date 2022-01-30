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
"А"


def decorator_time(func):
    from time import perf_counter

    def wrapper(*args):
        time_start = perf_counter()
        func(*args)
        cost_time = perf_counter() - time_start
        print(f'we had time: {cost_time}')

    return wrapper


# @decorator_time
# def pull_list(string_row):                # O(1)
#     list1 = string_row.split(' ')         # O(1) + (.split())
#     print(list1)                          # O(1)
#
#
# list1 = []                                # O(1
# pull_list(input())                        # O(1)

"['карл', 'у', 'клары', 'украл', 'кораллы']" \
"we had time: 0.0014890000000000736"

# @decorator_time
# def pull_dict(string_of_dict):
#     for i in string_of_dict.split(' '):     # O(n) + (.split())
#         dict1[i] = i                        # O(1)
#     print(dict1)                            # O(1)
#
#
# dict1 = {}                                  # O(1)
# pull_dict(input())                          # O(1)


"{'карл': 'карл', 'у': 'у', 'клары': 'клары', 'украл': 'украл', 'кораллы': 'кораллы'}" \
"we had time: 5.48000000000215e-05"

"Словарь заполняется медленнее, потому что использует только неизменяемые данные," \
" в список всеядный и имеет встроенную функцию"

"Б"

# @decorator_time
# def change_list1(change_string_of_list1, el_of_list1, change_el):
#     change_string_of_list1[change_string_of_list1.index(el_of_list1)] = change_el
#     print(change_string_of_dict)  # O(1)
#
#
# list1 = ['карл', 'у', 'клары', 'украл', 'кораллы']  # O(1)
# change_list1(list1, input(), input())  # O(1)

"['карлл', 'у', 'клары', 'украл', 'кораллы']" \
"we had time: 5.539999999992773e-05"

# @decorator_time
# def del_el_list1(del_el_of_list1, el_of_list1):
#     del_el_of_list1.remove(el_of_list1)
#     print(del_el_of_list1)  # O(1)
#
#
# list1 = ['карл', 'у', 'клары', 'украл', 'кораллы']  # O(1)
# del_el_list1(list1, input())  # O(1)

"['карл', 'клары', 'украл', 'кораллы']" \
"we had time: 0.0014327999999999008"


# @decorator_time
# def change_el_of_dict1(string_of_dict, k, v):
#     for i in string_of_dict:
#         if k != i:
#             string_of_dict.update(string_of_dict.items())
#         else:
#             string_of_dict.pop(k)
#             string_of_dict[v] = v
#     print(string_of_dict)
#
#
# dict1 = {'карл': 'карл', 'у': 'у', 'клары': 'клары', 'украл': 'украл', 'кораллы': 'кораллы'}
# change_el_of_dict1(dict1, input(), input())
#
# "{'карл': 'карл', 'клары': 'клары', 'украл': 'украл', 'кораллы': 'кораллы', 'уу': 'уу'}" \
# "we had time: 5.930000000020641e-05"



# @decorator_time
# def pull_dict(string_of_dict, del_el_of_dict):
#     string_of_dict.pop(del_el_of_dict)  # O(1)
#     print(dict1)  # O(1)
#
# dict1 = {'карл': 'карл', 'у': 'у', 'клары': 'клары', 'украл': 'украл', 'кораллы': 'кораллы'}
# pull_dict(dict1, input())  # O(1)
#
# "{'у': 'у', 'клары': 'клары', 'украл': 'украл', 'кораллы': 'кораллы'}" \
# "we had time: 4.7200000000025e-05"

"Здесь все наоборот, у словаря есть встроенные функции со сложностью O(1)" \
" функции для списка пробегают по всем значениям "

