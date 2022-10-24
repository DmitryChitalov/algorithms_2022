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
from timeit import timeit
from collections import deque

my_list = list(range(500))
my_deque = deque(my_list)

# 1
print('append list', timeit("""for i in range(500): my_list.append(i)""", globals=globals(), number=1000))
print('append deque', timeit("""for i in range(500): my_deque.append(i)""", globals=globals(), number=1000))

print('pop list', timeit("""for i in range(500): my_list.pop()""", globals=globals(), number=1000))
print('pop deque', timeit("""for i in range(500): my_deque.pop()""", globals=globals(), number=1000))

print('extend list', timeit("""for i in range(500): my_list.extend([i])""", globals=globals(), number=1000))
print('extend deque', timeit("""for i in range(500): my_deque.extend([i])""", globals=globals(), number=1000))
# различия в пределах погрешности, можно сделать вывод, что работают с одной скоростью

# 2
print('insert(0) list', timeit("""for i in range(100): my_list.insert(0, i)""", globals=globals(), number=100))
print('appendleft deque', timeit("""for i in range(100): my_deque.appendleft(i)""", globals=globals(), number=100))

print('pop(0) list', timeit("""for i in range(100): my_list.pop(0)""", globals=globals(), number=100))
print('popleft deque', timeit("""for i in range(100): my_deque.popleft()""", globals=globals(), number=100))

print('[:0] list', timeit("""for i in range(100): my_list[:0] = [i]""", globals=globals(), number=100))
print('extendleft deque', timeit("""for i in range(100): my_deque.extendleft([i])""", globals=globals(), number=100))
# deque быстрее на несколько порядков, что неудивительно, ведь его для этого и придумали.

# 3
print('[] list', timeit("""for i in range(500): x = my_list[i]""", globals=globals(), number=100000))
print('[] deque', timeit("""for i in range(500): x = my_deque[i]""", globals=globals(), number=100000))
# получение элемента из списка происходит значительно быстрее, хотя я думал, что будет примерно одинаково
