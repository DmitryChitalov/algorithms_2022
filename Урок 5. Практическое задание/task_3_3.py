"""
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
"""
from collections import deque
from timeit import timeit

n = 10000  # Увеличьте количество операций для точности
test_deque = deque(i for i in range(n))
test_lst = [i for i in range(n)]


def replace_in_array(lst):
    """Получение и изменение элемента"""
    for i in range(n):
        lst[i] = f"{i}"
    return lst


def run_tests():
    print("3) Тест получения и изменения элемента в массиве:")

    print(f"{replace_in_array.__doc__} дека "
          f"выполнилось за {timeit(lambda: replace_in_array(test_deque.copy()), number=n)} секунд")
    print(f"{replace_in_array.__doc__} списка "
          f"выполнилось за {timeit(lambda: replace_in_array(test_lst.copy()), number=n)} секунд")


run_tests()
