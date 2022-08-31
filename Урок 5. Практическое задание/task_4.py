"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


ordered = OrderedDict([(i, i) for i in range(50)])
simple = dict([(i, i) for i in range(50)])

print('Получение элемента по ключу, OrderedDict:', timeit("ordered[1]", globals=globals()))
print('Получение элемента по ключу, dict:', timeit("simple[1]", globals=globals()))
print('Метод get(), OrderedDict:', timeit("ordered.get(1)", globals=globals()))
print('Метод get(), dict:', timeit("simple.get(1)", globals=globals()))
print('Метод setdefault(), OrderedDict:', timeit("ordered.setdefault(50, 5)", globals=globals()))
print('Метод setdefault(), dict:', timeit("simple.setdefault(50, 5)", globals=globals()))
print('Метод update(), OrderedDict:', timeit("ordered.update({51: 5, 52: 6})", globals=globals()))
print('Метод update(), dict:', timeit("simple.update({51: 5, 52: 6})", globals=globals()))
print('Метод pop(), OrderedDict:', timeit("""for key in range(40, 50):
                                                 ordered.pop(key)
                                          """, globals=globals(), number=1))
print('Метод pop(), dict:', timeit("""for key in range(40, 50):
                                                 simple.pop(key)
                                          """, globals=globals(), number=1))

print('Метод popitem(last=True), OrderedDict:', timeit("ordered.popitem()", globals=globals(), number=10))
print('Метод popitem(), dict:', timeit("simple.popitem()", globals=globals(), number=10))

"""
Обычный словарь работает быстрее.

Использование OrderedDict имеет смысл, если:
    - требуется обозначить необходимость четкого порядка элементов;
    - необходимо реализовать принцип FIFO (метод popitem(last=False));
    - необходим метод move_to_end().
"""