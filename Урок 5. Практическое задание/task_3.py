"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

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
(append, pop и т.д.) проводить в циклах
"""
from collections import deque
from timeit import timeit

test_lst = [i for i in range(1, 50)]
my_lst = [i for i in range(1, 1000)]
test_dq = deque(i for i in range(1, 1000))


print('-----------------------------deque.append vs list.append')
print(timeit('for i in range(100): test_dq.append(i)', globals=globals(), number=5000))
print(timeit('for i in range(100): test_lst.append(i)', globals=globals(), number=5000))
print('-----------------------------deque.pop vs list.pop')
print(timeit('for i in range(100): test_dq.pop()', globals=globals(), number=5000))
print(timeit('for i in range(100): test_lst.pop()', globals=globals(), number=5000))
print('-----------------------------deque.extend vs list.extend')
print(timeit('for i in range(100): test_dq.extend(my_lst)', globals=globals(), number=5000))
print(timeit('for i in range(100): test_lst.extend(my_lst)', globals=globals(), number=5000))
"""
    В операциях "добавление элемента справа", "удаление и возврат элемента справа", "расширение
правой стороны с добавлением элементов заданного списка" по всем позициям лидирует "deque".
    Думаю, это обусловлено тем, что 'deque' поддерживает поточно-ориентированные, эффективные 
по памяти операции добавления и извлечения элементов последовательности с любой стороны с  
производительностью O(1) в любом направлении.
    Списки, поддерживающие аналогичные операции, оптимизированы только для быстрых операций с 
последовательностями фиксированной длины и требуют затрат O(n) на перемещение памяти для операций,
которые изменяют размер и положение базового представления данных.
(Подсказчик: docs-python.ru. Нам же главное разобраться, да?)
"""


print('-----------------------------deque.appendleft vs list.insert(0...)')
print(timeit('for i in range(5): test_dq.appendleft(i)', globals=globals(), number=10))
print(timeit('for i in range(5): test_lst.insert(0, i)', globals=globals(), number=10))
print('-----------------------------deque.extendleft vs list."конкатенация"')
print(timeit('test_dq.extendleft(my_lst)', globals=globals(), number=10))
print(timeit('my_lst + test_lst', globals=globals(), number=10))
print('-----------------------------deque.popleft vs list.pop(0)')
print(timeit('for i in range(10): test_dq.popleft()', globals=globals(), number=10))
print(timeit('for i in range(10): my_lst.pop()', globals=globals(), number=10))
"""
    В операциях "добавление элемента слева", "расширение левой стороны с добавлением элементов 
заданного списка" скорость снова на стороне "deque".
    Обычный список, "притормаживает" за счёт постоянного пересчёта индексов составляющих его
членов.
    "Удаление и возврат элемента слева" - на стороне списка.
"""


print('-----------------------------Получение элементов по индексу (deque[..] vs list[..])')
print(timeit('for i in range(100): test_dq[i]', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst[i]', globals=globals(), number=10000))
"""
   На большой выборке и заявленных операциях "deque" имеет пеимущества.
Замеры на небольших параметрах показывают преиущесво "штатных" методов.
    Вывод: Всегда надо действовать по обстановке). 
"""
