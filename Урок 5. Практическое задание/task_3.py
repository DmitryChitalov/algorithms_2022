"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
from timeit import timeit

list_1 = [i for i in range(1, 100)]
list_2 = [i for i in range(1, 1000)]
deque_ = deque(i for i in range(1, 1000))

print('*** deque.append vs list.append ***')
print(timeit('for i in range(100): deque_.append(i)', globals=globals(), number=5000))
print(timeit('for i in range(100): list_1.append(i)', globals=globals(), number=5000))
print('*** deque.pop vs list.pop ***')
print(timeit('for i in range(100): deque_.pop()', globals=globals(), number=5000))
print(timeit('for i in range(100): list_1.pop()', globals=globals(), number=5000))
print('*** deque.extend vs list.extend ***')
print(timeit('for i in range(100): deque_.extend(list_2)', globals=globals(), number=5000))
print(timeit('for i in range(100): list_1.extend(list_2)', globals=globals(), number=5000))

"""
В операциях "append", "pop", "extend" по всем позициям лидирует deque.
Возможно, это связано тем, что deque эффективные использует память при операции добавления
и извлечения элементов последовательности с любой стороны с производительностью O(1) в любом направлении.
Списки, поддерживающие аналогичные операции, оптимизированы только для быстрых операций с 
последовательностями фиксированной длины и требуют затрат O(n) на перемещение памяти для операций,
которые изменяют размер и положение базового представления данных.
"""

print('*** deque.appendleft vs list.insert(0...) ***')
print(timeit('for i in range(5): deque_.appendleft(i)', globals=globals(), number=10))
print(timeit('for i in range(5): list_1.insert(0, i)', globals=globals(), number=10))
print('*** deque.extendleft vs list."конкатенация" ***')
print(timeit('deque_.extendleft(list_2)', globals=globals(), number=10))
print(timeit('list_2 + list_1', globals=globals(), number=10))
print('*** deque.popleft vs list.pop(0) ***')
print(timeit('for i in range(10): deque_.popleft()', globals=globals(), number=10))
print(timeit('for i in range(10): list_2.pop()', globals=globals(), number=10))

"""
В операциях "appendleft", "extendleft" быстрее deque.
Обычный список, работает медленнее за счёт пересчёта индексов элементов.
В операции "popleft" список быстрее.
"""


print(
    '*** Получение элементов по индексу (deque[..] vs list[..]) ***')
print(
    timeit('for i in range(100): deque_[i]', globals=globals(), number=10000))
print(
    timeit('for i in range(100): list_1[i]', globals=globals(), number=10000))

"""
На большой выборке и deque имеет пеимущества.
Замеры на небольших параметрах показывают преимущесво "штатных" методов.
Вывод: Выбирать подходящие способы в зависимости от задачи. 
"""
