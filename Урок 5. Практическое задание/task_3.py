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

# 1) Cравниваем операции append, pop, extend.

test_list = [i for i in range(10 ** 4)]
test_deque = deque([i for i in range(10 ** 4)])

# Можно произвести замеры таким способом.

print('Сравниваем операцию append в списке и деке')
print(timeit("test_list.append(1)", number=10 ** 7, globals=globals()))  # 1.170076299997163
print(timeit("test_deque.append(1)", number=10 ** 7, globals=globals()))  # 0.9259825999979512
# Операция append отрабатывает на 15-30 процентов быстрее в объекте deque.

# Операция pop

print('Сравниваем операцию pop в списке и деке')
print(timeit("test_list.pop()", number=10 ** 7, globals=globals()))  # 0.8642072000002372
print(timeit("test_deque.pop()", number=10 ** 7, globals=globals()))  # 0.873252199999115
# Операция pop отрабатывает приблизительно одинаково,что в случае с листом, что в случае с дека.

# Операция extend

print('Сравниваем операцию extend в списке и деке')
print(timeit("test_list.extend([1, 2, 3])", number=10 ** 7, globals=globals()))  # 2.7559307999981684
print(timeit("test_deque.extend([1, 2, 3])", number=10 ** 7, globals=globals()))  # 2.5140488000033656
# Операция extend отрабатывает на 10 процентов быстрее в объекте deque.

# 2) Cравниваем операции appendleft, popleft, extendleft дека и соответствующие им операций списка.

# insert и appendleft.

print('Сравниваем операции insert и appendleft')
print(timeit("test_list.insert(0, 1)", number=1000, globals=globals()))  # 36.5175883999982
print(timeit("test_deque.appendleft(1)", number=1000, globals=globals()))  # 0.00011380000069038942
# Операция appendleft отрабатывает значительно быстрее своего аналога insert в листе.

# pop и popleft

print('Сравниваем операции pop и popleft')
print(timeit("test_list.pop(0)", number=1200, globals=globals()))  # 67.25891319999937
print(timeit("test_deque.popleft()", number=1200, globals=globals()))  # 0.00011780000204453245
# Операция popleft отрабатывает значительно быстрее своего аналога pop в листе.

# insert и extendleft.

print('Сравниваем операции insert и extendleft')
print(timeit("test_list.insert(0, [1,2,3] )", number=1000, globals=globals()))  # 0.6710261000043829
print(timeit("test_deque.extendleft([1,2,3])", number=1000, globals=globals()))  # 0.8462872999953106
# Операция extendleft отрабатывает значительно быстрее своего аналога insert в листе.

# 3) Cравниваем операции получения элемента списка и дека.


print('Cравниваем операции получения элемента списка и дека')
print(timeit("test_list[100]", number=10 ** 7, globals=globals()))  # 0.6653814000019338
print(timeit("test_deque[100]", number=10 ** 7, globals=globals()))  # 0.7017668999978923
# Получение элемента на 10 процентов быстрее в объекте List.

# Вывод. Если программа предусматривает обращение к элементу списка, то есть смысл использовать List. Если планируется
# изменение, удаление, замена элементов то по времени исполнения однозначно лидирует deque.
