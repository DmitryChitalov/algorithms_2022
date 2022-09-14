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
from random import randint

test_dq = deque()
test_lst = list()
my_lst = [i for i in range(200, 300)]

# test_one
print('Операции append')
print(timeit('for i in range(100): test_dq.append(i)', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst.append(i)', globals=globals(), number=10000))
print('Операции extend')
print(timeit('for i in range(100): test_dq.extend(my_lst)', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst.append(my_lst)', globals=globals(), number=10000))
print('Операции pop')
print(timeit('for i in range(100): test_dq.pop()', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst.pop()', globals=globals(), number=10000))


test_dq.clear()
test_lst.clear()

# test two
print('Операции appendleft')
print(timeit('for i in range(100): test_dq.appendleft(i)', globals=globals(), number=1000))
print(timeit('for i in range(100): test_lst.insert(0, i)', globals=globals(), number=1000))
print('Операции extendleft')
print(timeit('test_dq.extendleft(my_lst)', globals=globals(), number=10000))
print(timeit('my_lst + test_lst', globals=globals(), number=10000))
print('Операции popleft')
print(timeit('for i in range(10): test_dq.pop()', globals=globals(), number=10000))
print(timeit('for i in range(10): test_lst.pop(0)', globals=globals(), number=10000))

test_dq.clear()
test_lst.clear()


# test_three
for i in range(101):
    test_lst.append(i)

for i in range(101):
    test_dq.append(i)

print('Операции получения элемента')
print(timeit('for i in range(100): test_dq[randint(0, 100)]', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst[randint(0, 100)]', globals=globals(), number=10000))

"""
В операциях добавления в конец списка, чуть лучше себя показал deque за исключением метода extend,
по добавлению в начало выигрывает deque
в получении элемента примерно равны, чуть лучше список
Вывод: deque эффективнее при работе с извлечением и вставкой в начало списка, так как его методы
по умолчанию созданы для этого, ну а если элементы будут извлекаться произвольно то лучше использовать список

Операции append
deque 0.054608300037216395
list 0.08525400003418326

Операции extend
deque 1.219630400009919
list 0.08219049999024719

Операции pop
deque 0.051354699942748994
list 0.05484799999976531

Операции appendleft
deque 0.005324600031599402
list 2.219512600044254

Операции extendleft
deque 0.009033099981024861
list 1.7500893999822438

Операции popleft
deque 0.006472499982919544
list 1.035616500012111

Операции получения элемента
deque 0.6795986999641173
list 0.664863999991212
"""
