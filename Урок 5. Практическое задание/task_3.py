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

def append_list(lst: list) -> None:
    # Добавить занчение в конец списка.
    base_list = lst.copy()
    for item in range(len(base_list)):
        base_list.append(item)
    return None

def append_deque(dq: deque) -> None:
    # Добавить занчение в конец дека.
    for item in range(len(dq)):
        dq.append(item)
    return None

def pop_list(lst: list) -> None:
    # Удалить занчение с конеца списка.
    for _ in range(len(lst)):
        lst.pop()
    return None

def pop_deque(dq: deque) -> None:
    # Удалить занчение с конеца списка дека.
    for _ in range(len(dq)):
        dq.pop()
    return None

def extend_list(lst: list) -> None:
    # Присоединить список в конец списка.
    for _ in range(len(lst)):
        lst.extend([1, 2, 3, 4, 5])
    return None

def extend_deque(dq: deque) -> None:
    # Присоединить список в конец дека.
    for _ in range(len(dq)):
        dq.extend([1, 2, 3, 4, 5])
    return None

def appendleft_list(lst: list) -> None:
    # Добавить элемент в начало списка.
    for item in range(len(lst)):
        lst.insert(0, item)
    return None

def appendleft_deque(dq: deque) -> None:
    # Добавить элемент в начало дека.
    for item in range(len(dq)):
        dq.appendleft(item)
    return None

def popleft_list(lst: list) -> None:
    # Удалить элемент с начала списка.
    for _ in range(len(lst)):
        lst.pop(0)
    return None

def popleft_deque(dq: deque) -> None:
    # Удалить элемент с начала дека.
    for _ in range(len(dq)):
        dq.popleft()
    return None

def extendleft_list(lst: list) -> None:
    # Присоединить список в начале списка.
    for _ in range(len(lst)):
        lst.extend([1, 2, 3, 4, 5])
        for item in range(5):
            lst[item] = lst[-(item+1) ]
    return None

def extendleft_deque(dq: deque) -> None:
    # Присоединить список в начале дека.
    for item in range(len(dq)):
        dq.extendleft([1, 2, 3, 4, 5])
    return None

def get_element_list(lst: list) -> None:
    # Получить элемент списка.
    for item in range(len(lst)):
        x = lst[item]

def get_element_deque(dq: deque) -> None:
    # Получить эдемент дека.
    for item in range(len(dq)):
        x = dq[item]

if __name__ == "__main__":
    gen_lst: list = [item for item in range(1000)]
    gen_dq: deque = deque([item for item in range(1000)])
    number: int = 10000 # Количество повторений timeit.

    print("Задание 1:")
    print("Выполнение функции append:")
    print(f"\tдля списка {timeit('append_list(gen_lst.copy())', globals=globals(), number=number)} секунды.")
    print(f"\tдля дека: {timeit('append_deque(gen_dq.copy())', globals=globals(), number=number)} секунды.")

    print("Выполнение функции pop:")
    print(f"\tдля списка {timeit('pop_list(gen_lst.copy())', globals=globals(), number=number)} секунды.")
    print(f"\tдля дека: {timeit('pop_deque(gen_dq.copy())', globals=globals(), number=number)} секунды.")
    
    print("Выполнение функции extend:")
    print(f"\tдля списка {timeit('extend_list(gen_lst.copy())', globals=globals(), number=number)} секунды.")
    print(f"\tдля дека: {timeit('extend_list(gen_dq.copy())', globals=globals(), number=number)} секунды.")

    print("Задание 2:")
    print("Выполнение функции appendleft:")
    print(f"\tдля списка {timeit('appendleft_list(gen_lst.copy())', globals=globals(), number=number)} секунды.")
    print(f"\tдля дека: {timeit('appendleft_list(gen_dq.copy())', globals=globals(), number=number)} секунды.")

    print("Выполнение функции popleft:")
    print(f"\tдля списка {timeit('popleft_list(gen_lst.copy())', globals=globals(), number=number)} секунды.")
    print(f"\tдля дека: {timeit('popleft_deque(gen_dq.copy())', globals=globals(), number=number)} секунды.")

    print("Выполнение функции extendleft:")
    print(f"\tдля списка {timeit('extendleft_list(gen_lst.copy())', globals=globals(), number=number)} секунды.")
    print(f"\tдля дека: {timeit('extendleft_deque(gen_dq.copy())', globals=globals(), number=number)} секунды.")

    print("Задание 3:")
    print("Получение элемента:")
    print(f"\tдля списка {timeit('get_element_list(gen_lst.copy())', globals=globals(), number=number)} секунды.")
    print(f"\tдля дека: {timeit('get_element_deque(gen_dq.copy())', globals=globals(), number=number)} секунды.")

"""
Вывод:
    Задание 1:
    Выполнение функции append:
            для списка 2.922173416009173 секунды.
            для дека: 3.0654621639754623 секунды.
    Выполнение функции pop:
            для списка 2.4927129150019027 секунды.
            для дека: 3.255258364020847 секунды.
    Выполнение функции extend:
            для списка 3.775302833004389 секунды.
            для дека: 4.355614390049595 секунды.
    
    Задание 2:
    Выполнение функции appendleft:
            для списка 9.325660981994588 секунды.
            для дека: 2.7460312920156866 секунды.
    Выполнение функции popleft:
            для списка 2.6058385550277308 секунды.
            для дека: 1.932272884005215 секунды.
    Выполнение функции extendleft:
            для списка 17.898852633021306 секунды.
            для дека: 3.23186247801641 секунды.
    
    Задание 3:
    Получение элемента:
            для списка 1.4440771919908002 секунды.
            для дека: 1.4713600489776582 секунды.        
"""

"""

    1) Функции append, рор, extend в list выполняется быстрее, чем в deque.
    2) Функции, взаимодействующие с началом массива  выполняются быстрее в deque.
    3) Получение элемента по индексу в list проходит быстрее, чем в deque.
    
"""