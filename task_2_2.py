# Дмитрий, у меня медиана находится, а с замера возникает проблема при создании копии списка...
# Из-за этого не могу сделать корректный вывод, но встроенная функция поиска медианы эффективнее Шелла.
# Думаю, что она обгонит и второй вариант.

from random import randint
from timeit import timeit

m = 5
test_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(test_list)


def find_median(some_list):
    num = 0
    while num < m:
        max_num = max(some_list)
        test_list.remove(max_num)
        num += 1
    median = max(some_list)
    return f'Медиана: {median}'


print(find_median(test_list))

print(timeit('find_median(test_list[:])', globals=globals(), number=100))

# 2
m = 50
test_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(test_list[:])', globals=globals(), number=100))

# 3
m = 500
test_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(test_list[:])', globals=globals(), number=100))
