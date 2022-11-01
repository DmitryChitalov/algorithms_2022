"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

"""
Упорядоченный словарь есть смысл использовать только если хотим подчеркнуть, что нам очень важен порядок элементов в словаре для кода,
также у него есть два очень удобных метода: 1) престановка пары в начало и конец move_to_end, 2) popitem для OrderedDict может забирать пару с начала.
Чтобы реализовать эти действия для dict нужно писать дополнительный код, добавлять операции, что приводит к увеличению времени выполнения кода.
В остальных случаях использование OrderedDict в версиях Python старше 3.6 не имеет смысла
"""

from collections import OrderedDict
from timeit import timeit
import string

dic_for_task = {num: num ** 3 for num in range(1, 100)}
ordered_dict = OrderedDict(dic_for_task)

dic_for_update = dict.fromkeys(string.ascii_lowercase, 0)




"""
В данной операции делать замер с большим числом вызовов функции не имеет смысла, т.к. после первого вызова,
словарь больше не будет изменяться, все ключи будут добавлены.
Но даже при одном вызове видно, что update для простого словаря быстрее более чем в два раза
"""


def task_update(data):
    data.update(dic_for_update)
    return data


print(timeit('task_update(dic_for_task)', 'from __main__ import task_update, dic_for_task', number=1))
print(timeit('task_update(ordered_dict)', 'from __main__ import task_update, ordered_dict', number=1))

"""
Метод popitem тоже нет смысла вызывать больше 1 раза, при последующих вызовах словарь будет пуст, можно конечно заполнять
его каждый раз, но это только внесет большую погрешность колебаниями времени заполнения.
Удаление с конца в цикле также работает медленнее для OrderedDict.
"""


def task_popitem(data):
    if type(data) == OrderedDict:
        while len(data) > 0:
            data.popitem(last=True)
            if len(data) == 0:
                return data
    if type(data) == dict:
        while len(data) > 0:
            data.popitem()
            if len(data) == 0:
                return data


print(timeit('task_popitem(dic_for_task)', 'from __main__ import task_popitem, dic_for_task', number=1))
print(timeit('task_popitem(ordered_dict)', 'from __main__ import task_popitem, ordered_dict', number=1))


"""А если использовать специальные методы, то тут OrderedDict, наоборот - быстрее, что и ожидаемо"""

dic_for_task = {num: num ** 3 for num in range(1, 100)}
ordered_dict = OrderedDict(dic_for_task)


def task_popitem_last(data):
    if type(data) == OrderedDict:
        num = 99
        while num > 0:
            data.move_to_end(num, last=False)
            num -= 1

    if type(data) == dict:
        n = 0
        while len(data) != n:
            _data = data.popitem()
            _ = {_data[0]: _data[1]}
            data, _ = _, data
            data.update(_)
            n += 1
        return data


print(timeit('task_popitem_last(dic_for_task)', 'from __main__ import task_popitem_last, dic_for_task', number=1))
print(timeit('task_popitem_last(ordered_dict)', 'from __main__ import task_popitem_last, ordered_dict', number=1))

