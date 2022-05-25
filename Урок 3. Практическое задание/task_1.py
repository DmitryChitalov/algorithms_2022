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


def decorator(function):
    startTime = time()
    function()
    endTime = time()
    differTime = endTime - startTime
    print('start: ' + str(startTime))
    print('end: ' + str(endTime))
    print('differ: ' + str(differTime))
    print()


# a) Заполнение списка:
@decorator
def list_completion():

    newList = []            # O(len(0))

    newList.append(45)      # O(1)
    newList.append(56)      # O(1)
    newList.append(67)      # O(1)


# a) Заполнение словаря:
@decorator
def dictionary_complection():

    newDictionary = {}                   # O(len(0))

    newDictionary['имя'] = 'Шери'        # O(1)
    newDictionary['порода'] = 'сфинкс'   # O(1)
    newDictionary['возраст'] = 5         # O(1)


# b) Получение элемента списка:
@decorator
def get_element_list():

    getListElement = [5, 6, 7, 8, 9, 4]    # O(len(6))

    element1 = getListElement[0]           # O(1)
    element2 = getListElement[1]           # O(1)
    element3 = getListElement[-1]          # O(1)


# b) Получение элемента словаря
@decorator
def get_element_dictionary():

    getDictionaryElement = {'имя': 'Иван', 'отчество': 'Иванович', 'фамилия': 'Иванов', 'возраст': '32', 'рост': '175'}     #O(len(5))

    element1 = getDictionaryElement['имя']                                                                                  # O(1)
    element2 = getDictionaryElement['возраст']                                                                              # O(1)
    element3 = getDictionaryElement['рост']                                                                                 # O(1)


# c) Удаление элемента списка
@decorator
def deletingList():

    deleteList = [1, 2, 5, 78, 6, 8]      # O(len(6)

    del deleteList[3]                     # O(1)
    del deleteList[2]                     # O(1)
    del deleteList[0]                     # O(1)


# c) Удаление элемента словаря
@decorator
def deletingDict():

    deleteDict = {'логин': 'Max333', 'пароль': '123446', 'почта': 'Max@gmail.com', 'активация': 'True'}   # O(len(4))

    deleteDict.pop('почта')                                                                               # O(1)
    deleteDict.pop('логин')                                                                               # O(1)

