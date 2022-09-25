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

first_list = [i for i in range(0, 10)]
print(first_list)
deque_list = deque()
ordinary_list = list()


# 1 часть
# append, pop, extend списка и дека и сделать выводы что и где быстрее

# Append - добавление элемента в конец списка
test_append_list = timeit('for i in first_list: ordinary_list.append(i)', globals=globals(), number=1000)
test_append_deque = timeit('for i in first_list: deque_list.append(i)', globals=globals(), number=1000)
print(f'Замеры deque append - {test_append_deque}\nЗамеры list append - {test_append_list}')
# Замеры deque append - 0.008271599654108286 +
# Замеры list append - 0.010595600120723248 -

# Pop - убрать последний элемент в списке
test_pop_list = timeit('for i in first_list: ordinary_list.pop()', globals=globals(), number=1000)
test_pop_deque = timeit('for i in first_list: deque_list.pop()', globals=globals(), number=1000)
print(f'Замеры deque pop - {test_pop_deque}\nЗамеры list pop - {test_pop_list}')
# Замеры deque pop - 0.11060390016064048 -
# Замеры list pop - 0.07875300012528896 +

# Extend - добавляем список в список
test_extend_list = timeit('for i in range(1000, 1100) : ordinary_list.extend(first_list)', globals=globals(),
                          number=1000)
test_extend_deque = timeit('for i in range(1000, 1100) : deque_list.extend(first_list)', globals=globals(),
                           number=1000)
print(f'Замеры deque extend - {test_extend_deque}\nЗамеры list extend - {test_extend_list}')
# Замеры deque extend - 1.2706903996877372 +
# Замеры list extend - 4.131936599966139 -

# Вывод по первой части: deque хорошо показывает себя в методах: append и extend,
# но немного отстает в скорости в методе pop.


# 2 часть
# appendleft, popleft, extendleft дека и соответствующих им операций списка
# # и сделать выводы что и где быстрее

# Appendleft - добавляет i в начало списка, аналогично insert(0, i) для списка
test_insert_list = timeit('for i in first_list: ordinary_list.insert(0, i)', globals=globals(), number=1000)
test_appendleft_deque = timeit('for i in first_list: deque_list.appendleft(i)', globals=globals(), number=1000)
print(f'Замеры deque appendleft - {test_appendleft_deque}\nЗамеры list appendleft - {test_insert_list}')
# Замеры deque appendleft - 0.0008898000232875347 +
# Замеры list appendleft - 12.756114599760622 -

# Popleft - удаление с начала списка или дека
test_popleft_list = timeit('for i in first_list: ordinary_list.pop(0)', globals=globals(), number=1000)
test_popleft_deque = timeit('for i in first_list: deque_list.popleft()', globals=globals(), number=1000)
print(f'Замеры deque popleft - {test_popleft_deque}\nЗамеры list popleft - {test_popleft_list}')
# Замеры deque popleft - 0.0008898000232875347 +
# Замеры list pop(0) - 12.756114599760622 -


# extendleft - добавляем список в начало списка список
# deque_list.clear()
# ordinary_list.clear()

test_extendleft_list = timeit('first_list + ordinary_list', globals=globals(), number=1000)
test_extendleft_deque = timeit('deque_list.extendleft(first_list)', globals=globals(), number=1000)
print(f'Замеры deque extendleft - {test_extendleft_deque}\nЗамеры list extendleft - {test_extendleft_list}')
# Замеры deque extendleft - 0.00024899980053305626 +
# Замеры list extendleft - 0.00010609999299049377 -
# Замеры deque extendleft - 0.0002770996652543545 +
# Замеры list extendleft - 9.63001511991024e-05 - !!!!!! < - ОЧЕНЬ СТРАННЫЙ ВЫЗОВ

# Вывод по второй части: как видно по замерам,
# deque работает в разы быстрее с началом списка выигрывает по всем пунктам,
# ОДИН МОМЕНТ МНЕ НЕ ПОНЯТЕН, ПОЧЕМУ ПРИ МНОГОКРТНОМ ВЫЗОВЕ, ИНОГДА СЛОЖЕНИЕ В ОБЫЧНОМ СПИСКЕ ВЫПОЛНЯЕТЬСЯ ОЧЕНЬ ДОЛГО?


# 3 Часть
# сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее

test_element_list = timeit('ordinary_list[0]', globals=globals(), number=99999)
test_element_deque = timeit('ordinary_list[0]', globals=globals(), number=99999)
print(ordinary_list[5], ordinary_list[5] )
print(f'Замеры deque element - {test_element_deque}\nЗамеры list element - {test_element_list}')
# Замеры deque element - 0.0005272999405860901 +
# Замеры list element - 0.0006356001831591129 -
# Увеличил число повторений до 99999
# Замеры deque element - 0.0046594999730587006
# Замеры list element - 0.005942199844866991
# Замеры deque element - 0.007010199595242739
# Замеры list element - 0.007477799896150827
# Замеры deque element - 0.005516999866813421
# Замеры list element - 0.005524999927729368
# Замеры deque element - 0.005275900010019541
# Замеры list element - 0.005122799891978502
# Замеры deque element - 0.007399599999189377
# Замеры list element - 0.007568900007754564
# Вывод : Получение элемента в списке, как показали замеры deque быстрее работает с индексами

# Общия оценка : deque = 6 очков, list = 1 очко, list лучше показал себя в удалении элемента pop,
# вывод всегда используй deque

# Готово