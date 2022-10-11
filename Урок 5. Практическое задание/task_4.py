"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

# https://www.awesomeandrew.ru/2021/07/10/ordereddict-vs-dict-%D0%B2-python-%D0%B2%D1%8B%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD/?ysclid=l94iqk7wbl992406050

import timeit
from collections import OrderedDict

numbers_1 = dict({"one": 1, "two": 2, "three": 3})
numbers_2 = OrderedDict({"one": 1, "two": 2, "three": 3})
"""
print(numbers_1)
print(numbers_2)

numbers_1 = dict([("one", 1), ("two", 2), ("three", 3)])
numbers_2 = OrderedDict([("one", 1), ("two", 2), ("three", 3)])
print(numbers_1)
print(numbers_2)

numbers_1 = dict(one=1, two=2, three=3)
numbers_2 = OrderedDict(one=1, two=2, three=3)
print(numbers_1)
print(numbers_2)

keys = ["one", "two", "three"]
numbers_2 = OrderedDict.fromkeys(keys, 0)
print(numbers_2)
"""

print("Добавление нового элемента в dict:", timeit.timeit('numbers_1["four"]=4', number=10000, globals=globals()))
print("Добавление нового элемента в OrderedDict:", timeit.timeit('numbers_2["four"]=4', number=10000, globals=globals()))
print('Добавление элемента: Время dict немного меньше OrderedDict')
print("Удаление элемента в dict:", timeit.timeit('del numbers_1["four"]', number=1, globals=globals()))
print("Удаление элемента в OrderedDict:", timeit.timeit('del numbers_2["four"]', number=1, globals=globals()))
print('Удаление элемента: Время dict кратно меньше OrderedDict')

"""
В большинстве случаев при использовании версии Python 3.6 и выше использование OrderedDict нецелесообразно.
Нашел только несколько причин использования OrderedDict:
1. Обозначение смысла кода:
    если вы используете OrderedDict, а не dict, то ваш код поясняет, что важен порядок следования элементов в словаре.
    Вы определенно сообщаете, что ваш код требует и полагается на порядок элементов в словаре.
2. Контроль над порядком элементов:
    если вам нужно переупорядочить или переупорядочить элементы в словаре, вы можете использовать .move_to_end()
    и расширенный вариант .popitem().
3. Поведение при проверке равенства equality элементов: 
    если ваш код сравнивает словари на предмет их равенства (эквивалентности), и при сравнении важен порядок элементов, 
    то словари класса OrderedDict это правильный выбор.
4. Необходима обратная совместимость.
"""
