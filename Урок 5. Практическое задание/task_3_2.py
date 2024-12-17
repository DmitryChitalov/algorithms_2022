"""
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""
from collections import deque
from timeit import timeit

test_lst = []  # Пустой список для тестов
test_deque = deque()  # Очередь для тестов
n = 250  # Количество операций

"""
1) Дабавление элементов в начало списка и очереди
"""


def add_to_left_array(is_deque: bool) -> None:
    """Добавление элементов в начало"""
    if is_deque:
        for i in range(n):
            test_deque.appendleft(i)
    else:
        for i in range(n):
            test_lst.insert(0, i)


"""
2) Удаление элементов из начала списка и очереди 
"""


def pop_left_array(is_deque: bool) -> None:
    """Удаление элементов из начала"""
    if is_deque:
        for _ in range(n):
            test_deque.popleft()
    else:
        for _ in range(n):
            test_lst.pop(0)


"""
3) Добавление массивов в в начало списка и очереди
"""


def extend_left_array(is_deque: bool) -> None:
    """Добавление массива элементов в начало"""
    if is_deque:
        for i in range(n):
            test_deque.extendleft([i])
    else:
        for i in range(n):
            test_lst.insert(0, [i] * 3)


def run_tests() -> None:
    print(f"2) Тест оперций для дека appendleft, popleft, extendleft "
          f"и сравнение со схожими операциями для списка:")
    print(f"{add_to_left_array.__doc__} списка выполнилось за "
          f"{timeit(lambda: add_to_left_array(False), number=n)} секунд.")
    print(f"{add_to_left_array.__doc__} дека выполнилось за "
          f"{timeit(lambda: add_to_left_array(True), number=n)} секунд.\n")

    print(f"{pop_left_array.__doc__} списка выполнилось за "
          f"{timeit(lambda: pop_left_array(False), number=n)} секунд.")
    print(f"{pop_left_array.__doc__} дека выполнилось за "
          f"{timeit(lambda: pop_left_array(True), number=n)} секунд.\n")

    print(f"{extend_left_array.__doc__} списка выполнилось за "
          f"{timeit(lambda: extend_left_array(False), number=n)} секунд.")
    print(f"{extend_left_array.__doc__} дека выполнилось за "
          f"{timeit(lambda: extend_left_array(True), number=n)} секунд.")
