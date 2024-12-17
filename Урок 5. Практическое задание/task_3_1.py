"""
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
"""

from collections import deque
from timeit import timeit

test_lst = []  # Пустой список для тестов
test_deque = deque()  # Очередь для тестов
n = 250  # Количество операций


# 1) Дабавление элементов в начало списка и очереди
def append_in_array(is_deque: bool) -> None:
    """Добавление элементов в конец"""
    lst = test_lst if is_deque else test_deque
    for i in range(n):
        lst.append(i)


# 2) Дабавление элементов в начало очереди
def pop_for_array(is_deque: bool) -> None:
    """Удаление последнего элемента"""
    lst = test_lst if is_deque else test_deque
    for i in range(n):
        lst.pop()


# 3) Дабавление массива из другого списка в конец очереди
def extend_in_array(is_deque: bool) -> None:
    """Добавление элементов из другого списка в конец"""
    lst = test_lst if is_deque else test_deque
    for i in range(n):
        lst.extend([i] * 3)


def run_tests() -> None:
    print("1) Тест использование append, pop, extend для списка и очереди")
    print(f"{append_in_array.__doc__} для списка "
          f"выполнился за {timeit(lambda: append_in_array(False), number=n)} секунд")
    print(f"{append_in_array.__doc__} для очереди "
          f"выполнился за {timeit(lambda: append_in_array(True), number=n)} секунд\n")
    print(f"{pop_for_array.__doc__} для списка "
          f"выполнился за {timeit(lambda: pop_for_array(False), number=n)} секунд")
    print(f"{pop_for_array.__doc__} для очереди "
          f"выполнился за {timeit(lambda: pop_for_array(True), number=n)} секунд\n")
    print(f"{extend_in_array.__doc__} для списка "
          f"выполнился за {timeit(lambda: extend_in_array(False), number=n)} секунд")
    print(f"{extend_in_array.__doc__} для очереди "
          f"выполнился за {timeit(lambda: extend_in_array(True), number=n)} секунд\n")
