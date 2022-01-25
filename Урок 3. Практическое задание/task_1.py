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


def test_time(fn):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = fn(*args, **kwargs)
        dt = time.time() - st
        print(f"Время работы функции {fn.__name__}: {dt} сек")
        return res

    return wrapper


x = 100000


@test_time
def makelist():
    my_list = [a * 3 for a in range(x)]  # O(n), здесь можно написать O(100000)


@test_time
def makedic():
    my_dict = {a: a + 2 for a in range(x)}  # O(n)


makelist()
print('*' * 60)

makedic()
print('*' * 60)


@test_time
def empt_lst(pop_list):
    for i in range(50000):
        pop_list.pop(i)    # O(n)


@test_time
def empt_dict(pop_dict):
    for i in range(50000):
        pop_dict.pop(i)  # O(1)
        # print(pop_list)


mylist = [a for a in range(x)]
# print(mylist)
empt_lst(mylist)
print('*' * 60)

mydict = {a: a + 2 for a in range(x)}
# print(mylist)
empt_dict(mydict)
print('*' * 60)


@test_time
def ch_lst(del_list):
    for i in range(50000):
        del_list.remove(i)  # O(n)
        # print(pop_list)


@test_time
def ch_dict(del_dict):
    for i in range(50000):
        del_dict.popitem()  # O(1)
        # print(pop_list)


mylist = [a for a in range(x)]
# print(mylist)
ch_lst(mylist)
print('*' * 60)

mydict = {a: a + 2 for a in range(x)}
# print(mylist)
ch_dict(mydict)
print('*' * 60)

"""
создание списков идет быстрее чем словарей, но 
оперции со списком происходят дольше, т.к. словари 
являются хешируемыми объектами
"""