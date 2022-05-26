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

# Создадим тестовый список на 1000 элементов, и на его основе создадим тестовый deque:
test_list = [n for n in range(1000)]
test_deque = deque(test_list)

'''
сравнить операции append, pop, extend списка и дека:
'''


def list_append(user_list, n=100):
    for i in range(n):
        user_list.append(i)


def list_pop(user_list, n=100):
    for i in range(n):
        user_list.pop()


def list_extend(user_list, n=100):
    t_extend = [i for i in range(n)]
    user_list.extend(t_extend)


"""
 сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка``
"""


def list_append_left(user_list, n=1):
    for i in range(n):
        user_list.insert(0, i)


def deque_append_left(user_deque, n=1):
    for i in range(n):
        user_deque.appendleft(i)


def list_pop_left(user_list, n=1):
    for i in range(n):
        user_list.pop(0)


def deque_pop_left(user_deque, n=1):
    for i in range(n):
        user_deque.popleft()


def list_extend_left(user_list, n=1):
    t_extend = [i for i in range(n)]
    user_list.insert(0, t_extend)


def deque_extend_left(user_deque, n=1):
    t_extend = [i for i in range(n)]
    user_deque.extendleft(t_extend)


"""
сравнить операции получения элемента списка и дека
"""


def get_list(user_list, n=100):
    for i in range(n):
        user_list[i]




print('Часть 1:')
print('append списка', timeit("list_append(test_list)", globals=globals(), number=10000))
print('append дэка', timeit("list_append(test_deque)", globals=globals(), number=10000))
print('pop списка', timeit("list_pop(test_list)", globals=globals(), number=10000))
print('pop дэка', timeit("list_pop(test_deque)", globals=globals(), number=10000))
print('extend списка', timeit("list_extend(test_list)", globals=globals(), number=10000))
print('extend дэка', timeit("list_extend(test_deque)", globals=globals(), number=10000))
print('Часть 2:')
print('appendleft списка', timeit("list_append_left(test_list)", globals=globals(), number=10000))
print('appendleft дэка', timeit("deque_append_left(test_deque)", globals=globals(), number=10000))
print('popleft списка', timeit("list_pop_left(test_list)", globals=globals(), number=10000))
print('popleft дэка', timeit("deque_pop_left(test_deque)", globals=globals(), number=10000))
print('extendleft списка', timeit("list_extend_left(test_list)", globals=globals(), number=10000))
print('extendleft дэка', timeit("deque_extend_left(test_deque)", globals=globals(), number=10000))
print('Часть 2:')
print('извлечение элемента списка', timeit("get_list(test_list)", globals=globals(), number=100000))
print('извлечение элемента дэка', timeit("get_list(test_deque)", globals=globals(), number=100000))

"""
Результаты получивщиеся на моей машине:
Часть 1:
append списка 0.06245719999424182
append дэка 0.03651020000688732
pop списка 0.039973599996301346
pop дэка 0.03298630000790581
extend списка 0.03939580000587739
extend дэка 0.028139699992607348
Часть 2:
appendleft списка 6.188089100003708
appendleft дэка 0.0021902000007685274
popleft списка 5.1951016999955755
popleft дэка 0.0021620000043185428
extendleft списка 6.187748699987424
extendleft дэка 0.0038016000034986064
Часть 2:
извлечение элемента списка 0.20235459999821614
извлечение элемента дэка 0.2695411000022432

1)
В "классическом" добавлении, дэк немного опережает по скорости список. Т.К. синтаксис одинаковый, для замеров 
использовал одинаковые функции, в каждой можно регулировать количество удаляемых/добавляемых элементов с помощью 
параметра n (по умолчанию n=100)
2)
В "добавлении/удалении слева", дэк фантастически опережает список! (запустив функции с параметром n=100 судя по 
тревожно загудевшему куллеру, ждать надо было очень долго... 68 секунд для списка! по этому, замер проводил с n=1)
3)
А в операции извлечения элемента лидирует класический список. Тут из за одинакового синтаксиса используем одну и ту же 
функцию для списка и дэка.
Видим по замерам, что утверждение из начала задания верно!
"""