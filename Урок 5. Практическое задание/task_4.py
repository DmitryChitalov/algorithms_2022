"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict


dict = {
    1: 'понедельник',
    4: 'четверг',
    2: 'вторник',
    5: 'пятница',
    3: 'среда'
}

dict_ord = OrderedDict([
    (1, 'понедельник'),
    (2, 'вторник'),
    (3, 'среда'),
    (4, 'четверг'),
    (5, 'пятница')
])


print(dict == dict_ord)     # -> словари равны

# добавление элемента в словарь
dict[6] = 'суббота'
dict[7] = 'воскресение'
print(dict)                 # -> вставка в конец

dict_ord[6] = 'суббота'
dict_ord[7] = 'воскресение'
print(dict_ord)             # -> вставка в конец

print(dict == dict_ord)     # -> словари равны

# удаление элемента словаря
del dict[7]
print(dict)

del dict_ord[7]
print(dict_ord)

print(dict == dict_ord)     # -> словари равны

# изменение значения
dict[6] = 'saturday'
dict.update({5 :'friday'})
print(dict)

dict_ord[5] = 'friday'
dict_ord[6] = 'saturday'
print(dict_ord)

print(dict == dict_ord)     # -> словари равны

# вывод значений
for key, val in dict.items():
    print (key, val)

for key, val in dict_ord.items():
    print (key, val)

for key, val in reversed(dict.items()):
    print (key, val)

for key, val in reversed(dict_ord.items()):
    print (key, val)

# перемещение элемента
dict_ord.move_to_end(1, last=True)
print(dict_ord)

day_1 = dict.pop(1)
dict[1] = day_1
print(dict)


# удаление элемента и возврат значения
print(dict.pop(2))
print(dict)

print(dict_ord.popitem())
print(dict_ord)

print(dict_ord.popitem(last=False))
print(dict_ord)

# ВЫВОД:
# в более поздних версиях Python - есть смысл использовать OrderedDict в случаях когда важен порядок и для операвтивного переупорядочивания элементов