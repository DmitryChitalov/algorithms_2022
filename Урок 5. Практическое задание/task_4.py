"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

number = 100000
simple_dict = {}
simple_ord_dict = OrderedDict()



"""
Заполнение словарей:
0.8902039
1.1189535
Обычный словарь заполняется быстрее.
"""
print('-----------------------------------------------------------------------------------')


def dict_append(dict):
    for i in range(number):
        dict[i] = i
    return dict


def ord_dict_append(ord_dict):
    for i in range(number):
        ord_dict[i] = i
    return ord_dict


dict_append(simple_dict)
ord_dict_append(simple_ord_dict)
print(timeit("dict_append(simple_dict)", globals=globals(), number=100))
print(timeit('ord_dict_append(simple_ord_dict)', globals=globals(), number=100))


"""
Изменение словарей:
0.0005900000000003125
0.0007867999999997544
Обычный словарь изменяется быстрее.
"""
print('-----------------------------------------------------------------------------------')


def dict_change(dict):
    for i in range(100):
        dict[i] = i+10
    return dict


def ord_dict_change(ord_dict):
    for i in range(100):
        ord_dict[i] = i+10
    return ord_dict


dict_change(simple_dict)
ord_dict_change(simple_ord_dict)

print(timeit("dict_change(simple_dict)", globals=globals(), number=100))
print(timeit("ord_dict_change(simple_ord_dict)", globals=globals(), number=100))


"""
Удаление элемента словарей:
замерить изменение словарей не получилось, т.к. все время на исполнении timeit ошибка:
Traceback (most recent call last):
  File "C:\Projects\algorithms_2022\Урок 5. Практическое задание\task_4.py", line 70, in <module>
    print(timeit("dict_pop(simple_dict)", globals=globals(), number=100))
  File "C:\Users\admin\AppData\Local\Programs\Python\Python39\lib\timeit.py", line 233, in timeit
    return Timer(stmt, setup, timer, globals).timeit(number)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python39\lib\timeit.py", line 177, in timeit
    timing = self.inner(it, self.timer)
  File "<timeit-src>", line 6, in inner
  File "C:\Projects\algorithms_2022\Урок 5. Практическое задание\task_4.py", line 57, in dict_pop
    dict.pop(i)
KeyError: 0
Process finished with exit code 1

Пробовала в разных вариациях. Что-то не так делаю?
"""
print('-----------------------------------------------------------------------------------')


def dict_pop(dict):
    for i in range(100):
        dict.pop(i)
    return dict


def ord_dict_pop(ord_dict):
    for i in range(100):
        ord_dict.pop(i)
    return ord_dict


dict_pop(simple_dict)
ord_dict_pop(simple_ord_dict)

print(timeit("dict_pop(simple_dict)", globals=globals(), number=100))
print(timeit("ord_dict_pop(simple_ord_dict)", globals=globals(), number=100))
