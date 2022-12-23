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
def metering(func):
    def wrap(*args):
        first = time()
        i = func(*args)
        last = time()
        print(last - first)
        return i if i else None

    return wrap
@metering
def populate_list(): # O(1)
    result = []  # O(1)
    for i in range(99999):  # O(1)
        result.append(["Новое значение" , i])  # O(1)
    return result  # O(1)

@metering # A
def populate_hashtable():# O(1)
    result = {}  # O(1)
    for i in range(99999):  # O(1)
        result[i] = ["Новое значение", i]  # O(1)
    return result  # O(1)


print ("Заполнение элементами")
print_list = populate_list()
print_hashtable = populate_hashtable()

print ("Словарь  считает  кэш это тратит ресурсы, выходит дольше")

@metering    #Б
def assign_list(element: list):
    """Сложность O(n)"""
    for i in range(len(element)):  # O(n)
        value = element[i]  # O(1)

@metering
def assign_hashtable(element: dict):
    """Сложность O(n)"""
    for i in range(len(element)):  # O(n)
        value = element[i]  # O(1)

print("Вывод элементов")

assign_list(print_list)
assign_hashtable(print_hashtable)

print("Словарь вышел опять дольше. видимо по причине чтения кеша, хотя мне казалось чтение должно быть быстрее.  ")

@metering # C
def removal_from_list(element: list):#O(n^2)
    for i in range(len(element) - 1, 0, -1):  # O(n)
        del element[i]  # O(n)


@metering
def removal_from_hashtable(element: dict): # O(n)
    for i in range(len(element)):  # O(n)
        del element[i]  # O(1)

print('Удаление элемента')
removal_from_list(print_list)
removal_from_hashtable(print_hashtable)

print("Словарь вышел быстрее, очевидно по тому что не перебераем элемент а сразу удаляем")