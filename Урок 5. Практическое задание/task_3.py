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
from random import randint
from timeit import timeit


def deque_append(deq_obj=deque([])):
    for i in (range(10)):
        deq_obj.append(i)
    return deq_obj


def list_append(lst_obj=[]):
    for i in (range(10)):
        lst_obj.append(i)
    return lst_obj


def deque_pop(deq_obj=deque([])):
    while deq_obj:
        deq_obj.pop()
    return deq_obj


def list_pop(lst_obj=[]):
    while lst_obj:
        lst_obj.pop()
    return lst_obj


def deque_extend(deq_obj=deque([])):
    for i in (range(10)):
        deq_obj.extend([i, i])
    return deq_obj


def list_extend(lst_obj=[]):
    for i in (range(10)):
        lst_obj.extend([i, i])
    return lst_obj


def deque_append_left(deq_obj=deque([])):
    for i in (range(3)):
        deq_obj.appendleft(i)
    return deq_obj


def list_append_left_insert(lst_obj=[]):
    for i in (range(3)):
        lst_obj.insert(0, i)
    return lst_obj


def list_append_left_con(lst_obj=[]):
    for i in (range(3)):
        lst_obj = [i] + lst_obj
    return lst_obj


def deque_pop_left(deq_obj=deque([])):
    while deq_obj:
        deq_obj.popleft()
    return deq_obj


def list_pop_left(lst_obj=[]):
    while lst_obj:
        lst_obj.pop(0)
    return lst_obj


def deque_extend_left(deq_obj=deque([])):
    for i in (range(3)):
        deq_obj.extendleft([i, i])
    return deq_obj


def list_extend_left_con(lst_obj=[]):  # аналога extendleft([i, i]) для list нет, попробуем другие алгоритмы.
    for i in (range(3)):
        lst_obj = [i, i] + lst_obj
    return lst_obj


def list_extend_left_insert(lst_obj=[]):
    for i in (range(3)):
        lst_obj.insert(0, i)
        lst_obj.insert(0, i)
    return lst_obj


def deque_get_middle_el(deq_obj=deque([])):
    middle_el = deq_obj[len(deq_obj) // 2]
    return middle_el


def list_get_middle_el(lst_obj=[]):
    middle_el = lst_obj[len(lst_obj) // 2]
    return middle_el


def deque_get_randint_el(deq_obj=deque([])):
    middle_el = deq_obj[randint(0, len(deq_obj) - 1)]
    return middle_el


def list_get_randint_el(lst_obj=[]):
    middle_el = lst_obj[randint(0, len(lst_obj) - 1)]
    return middle_el


if __name__ == '__main__':
    #  Класс deque это обобщение стеков и очередей и представляет собой двустороннюю очередь.
    #  Двусторонняя очередь поддерживает эффективные по памяти операции добавления и извлечения
    #  элементов последовательности с любой стороны с примерно одинаковой производительностью O(1)
    #  в любом направлении.
    #  Списки поддерживают аналогичные операции, но они оптимизированы только для быстрых операций
    #  с последовательностями фиксированной длины.
    #  Сложность О(1) для записи и удаления с конца списка.
    #  Они требуют затрат O(n) на перемещение памяти для операций pop(0) и insert(0, v),
    #  которые изменяют как размер, так и положение базового представления данных.
    #  1
    print(f'deque_append(): {timeit("deque_append(deq_obj=deque([]))", globals=globals())}')
    print(f'list_append(): {timeit("list_append(lst_obj=[])", globals=globals())}')
    #  Сеорость добавления элемента с помощью append в конец списка и дека сравнимая (практически одинакова)
    #  У списка немного быстрее.
    #  При нескольких запусках теста иногда бывает, что быстрее элемент добавляется в дек.
    #  Это соответствует документации.
    print(f'deque_pop(): {timeit("deque_pop(deque([2, 1, 0]))", globals=globals())}')
    print(f'list_pop(): {timeit("list_pop([2, 1, 0])", globals=globals())}')
    #  Сеорость удаления элемента с помощью pop из конеца списка и дека сравнимая (практически одинакова)
    #  У списка чуть-чуть быстрее.
    #  При нескольких запусках теста иногда бывает, что быстрее элемент удаляется из дека.
    #  Это соответствует документации.
    print(f'deque_extend(): {timeit("deque_extend()", globals=globals())}')
    print(f'list_extend(): {timeit("list_extend()", globals=globals())}')
    #  Сеорость добавления элементов с помощью extend в конец списка и дека сравнимая (практически одинакова)
    #  У спмска несущественно быстрее.
    #  При нескольких запусках теста иногда бывает, что быстрее у дкеа.
    #  Это соответствует документации.
    #  2
    print(f'deque_append_left(): {timeit("deque_append_left()", number=10000, globals=globals())}')
    print(f'list_append_left_insert(): {timeit("list_append_left_insert()", number=10000, globals=globals())}')
    print(f'list_append_left_con(): {timeit("list_append_left_con()", number=10000, globals=globals())}')
    #  Скорость добавления в список слева зависит от способа добавления.
    #  insert в списке практически в 50 раз медленее, чем appendleft дека.
    #  Это соответствует документации.
    #  Однако, конкатенация списков сравнима по скорости с appendleft дека,
    #  Сложение списков чуть-чуть медленее.
    print(f'deque_pop_left(): {timeit("deque_pop_left(deque([3, 2, 1, 0]))", globals=globals())}')
    print(f'list_pop_left(): {timeit("list_pop_left([3, 2, 1, 0])", globals=globals())}')
    #  Скорость удаление из списка и дека слева сравнимая (практичкски одинакова)
    #  У дека чуть быстрее.
    #  Это соответствует документации.
    print(f'deque_extend_left(): {timeit("deque_extend_left()", number=10000, globals=globals())}')
    print(f'list_extend_left_con(): {timeit("list_extend_left_con()", number=10000, globals=globals())}')
    print(f'list_extend_left_insert(): {timeit("list_extend_left_insert()", number=10000, globals=globals())}')
    #  У списка аналогичной команды нет.
    #  Скорость добавления в список нескольких элементов слева зависит от способа вставки.
    #  Скорость добавления в деке с помощью extend_left и в списке с помощью конкатенации сравнимая
    #  (практически одинакова). У списка скорость сложения несвущественно выше.
    #  Если мы добавляли с помощью insert, то как и по предыдущему примеру с insert видно,
    #  что время возртает. Здесь оно больше примерно в 100 раз.
    #  3
    print(f'deque_get_middle_el(): {timeit("deque_get_middle_el(deque([4, 3, 2, 1, 0]))", globals=globals())}')
    print(f'list_get_middle_el(): {timeit("list_get_middle_el([4, 3, 2, 1, 0])", globals=globals())}')
    print(f'deque_get_randint_el(): {timeit("deque_get_randint_el(deque([4, 3, 2, 1, 0]))", globals=globals())}')
    print(f'list_get_randint_el(): {timeit("list_get_randint_el([4, 3, 2, 1, 0])", globals=globals())}')
    #  Скорость извлечения среднего элемента у дека в практически в два раза медленее, чем у списка.
    #  Это соответствует документации.
    #  При извлечении случайного элемента, с учетом увеличения времени на генерацию случайного числа,
    #  извлечение элемента из списка все равно остается быстрее.
    #  Это соответствует документации.
