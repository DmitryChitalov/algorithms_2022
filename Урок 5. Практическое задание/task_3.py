"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

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
(append, pop и т.д.) проводить в циклах
"""

from collections import deque
from timeit import repeat, default_timer


# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее

# append
setup = """
from collections import deque

test_deque = deque()
test_list = []

def test_deque_append(n):
    test_deque = deque()
    for i in range(n):
        test_deque.append(i)

def test_list_append(n):
    test_list = []
    for i in range(n):
        test_deque.append(i)
"""
# 0.052957899984903634
print(f"{min(repeat(stmt='test_deque_append(10**5)', repeat=3, setup=setup, number=10))=}") # 0.052957899984903634
# 0.05117939994670451
print(f"{min(repeat(stmt='test_deque_append(10**5)', repeat=3, setup=setup, number=10))=}")
# ===> При append разницы во времени выполения нет --- O(1)
print('=================================================================')

# pop
setup = """
from collections import deque
test_deque = deque()
test_list = []
[test_deque.append(i) for i in range(10**6+1)]
[test_list.append(i) for i in range(10**6+1)]
def test_deque_pop(n):
    for i in range(n):
        return test_deque.pop()

def test_list_pop(n):
    for i in range(n):
        return test_list.pop()
"""
# 0.022783199907280505
print(f"{min(repeat(stmt='test_deque_pop(10)', repeat=3, setup=setup, number=10**5))=}")
# 0.022772800060920417
print(f"{min(repeat(stmt='test_list_pop(10)', repeat=3, setup=setup, number=10**5))=}")
# ===> При pop разницы во времени выполения нет --- O(1)
print('=================================================================')

# extend
# 0.01776040007825941
print(f"{min(repeat(stmt='test_deque.extend(range(10**5))', repeat=3, setup=setup, number=10))=}")
# 0.02590430004056543
print(f"{min(repeat(stmt='test_list.extend(range(10**5))', repeat=3, setup=setup, number=10))=}")
# ===> deque и list примерно работают с одной скоростью, 
# при одних значниях одно немного быстрее, при других значениях другое 
# Скорость работы пропорционально количеству входных значений 
# --- O(k) где к - это размер входной последовательности
print('=================================================================')

# appendleft
setup = """
from collections import deque
test_deque = deque()
test_list = []
def test_deque_appendleft(n):
    for i in range(n):
        test_deque.appendleft(i)

def test_list_insert_zero(n):
    for i in range(n):
        test_list.insert(0, i)
"""
# 0.00041280000004917383
print(f"{min(repeat(stmt='test_deque_appendleft(10**4)', repeat=3, setup=setup, number=1))=}")
# 0.01703549991361797
print(f"{min(repeat(stmt='test_list_insert_zero(10**4)', repeat=3, setup=setup, number=1))=}")
# ===> deque работает значительно быстрее,
# deque дает сложность  - O(1) list - O(n)
print('=================================================================')
# popleft
setup = """
from collections import deque
test_deque = deque()
test_list = []
[test_deque.append(i) for i in range(10**6)]
[test_list.append(i) for i in range(10**6)]

def test_deque_popleft(n):
    for i in range(n):
        return test_deque.popleft()

def test_list_pop_zero(n):
    for i in range(n):
        return test_list.pop(0)
"""
# 4.599918611347675e-06
print(f"{min(repeat(stmt='test_deque_popleft(10**2)', repeat=3, setup=setup, number=1))=}")
# 0.0006923999171704054
print(f"{min(repeat(stmt='test_list_pop_zero(10**2)', repeat=3, setup=setup, number=1))=}")
# ===> deque работает значительно быстрее,
# deque дает сложность  - O(1) list - O(n)
print('=================================================================')


# extendleft
setup = """
from collections import deque
test_deque = deque()
test_list = []
[test_deque.append(i) for i in range(10**6)]
[test_list.append(i) for i in range(10**6)]
"""
# 0.17714689997956157
print(f"{min(repeat(stmt='test_deque.extendleft(range(10**6))', repeat=3, setup=setup, number=10))=}")
# 0.36082429997622967
print(f"{min(repeat(stmt='test_list[0:0]=list(range(10**6))', repeat=3, setup=setup, number=10))=}")
# ===> deque и list вставляют за сопоставимое время
# O(k) где к - это размер входной последовательности
print('=================================================================')

# получение элемента
setup = """
from collections import deque
test_deque = deque()
test_list = []
[test_deque.append(i) for i in range(10**6)]
[test_list.append(i) for i in range(10**6)]

def test_deque_get_zero(n):
    for i in range(n):
        result = test_deque.popleft()
        test_deque.appendleft(result)
        return result

def test_deque_get_last(n):
    for i in range(n):
        result = test_deque.pop()
        test_deque.append(result)
        return result

def test_deque_get_middle(n):
    middle=10**6//2
    for i in range(n):
        tmp_ = test_deque.copy()
        for num in range(middle):
            tmp_.pop()
        return tmp_.pop()

def test_list_get_zero(n):
    for i in range(n):
        return test_list[0]

def test_list_get_last(n):
    for i in range(n):
        return test_list[-1]

def test_list_get_middle(n):
    middle=10**6//2
    for i in range(n):
        return test_list[middle]
"""
# 9.899958968162537e-06
print(f"{min(repeat(stmt='test_deque_get_zero(10**5)', repeat=3, setup=setup, number=10))=}")
# 8.09994526207447e-06
print(f"{min(repeat(stmt='test_list_get_zero(10**5)', repeat=3, setup=setup, number=10))=}")

# 8.899951353669167e-06
print(f"{min(repeat(stmt='test_deque_get_last(10**5)', repeat=3, setup=setup, number=10))=}")
# 8.100061677396297e-06
print(f"{min(repeat(stmt='test_list_get_last(10**5)', repeat=3, setup=setup, number=10))=}")

# 0.33735649997834116
print(f"{min(repeat(stmt='test_deque_get_middle(10**5)', repeat=3, setup=setup, number=10))=}")
# 8.500064723193645e-06
print(f"{min(repeat(stmt='test_list_get_middle(10**5)', repeat=3, setup=setup, number=10))=}")
# ===> deque и list вначале и в конце значения получают за одинаковое время
# list из середины берет значение за такое-же время - сложность O(1), 
# однако из середины deque получить значения очень долго - сложность O(n)
print('=================================================================')