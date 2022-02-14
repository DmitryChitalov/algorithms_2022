from collections import deque
from timeit import timeit


def lst():
    i = 0
    lst = []
    while i <= 100:
        lst.append(i)
        i += 1
    print(lst)


def deq():
    i = 0
    deq = deque()
    while i <= 100:
        deq.append(i)
        i += 1
    print(deq)


num = 10000


def lst_pop():
    lst = [i for i in range(num)]
    lst.pop(0)


def deq_pop():
    deq = deque([i for i in range(num)])
    deq.popleft()


def lst_ext():
    lst1 = [i for i in range(num)]
    lst1.extend([101, 102, 103, 104, 105, 106])
    return lst1


def deq_ext():
    deq = deque([i for i in range(num)])
    deq.extend([101, 102, 103, 104, 105, 106])
    return deq


def deq_appleft():
    deq = deque([i for i in range(num)])
    deq.appendleft(123)
    return deq


def lst_insert():
    lst1 = [i for i in range(num)]
    lst1.insert(0, 123)
    return lst1


def deq_popleft():
    deq = deque([i for i in range(num)])
    deq.popleft()
    return deq


def lst_popleft():
    lst1 = [i for i in range(num)]
    lst1.pop(0)
    return lst1


def lst_extendleft():
    lst1 = [i for i in range(num)]
    lst2 = [23, 45, 36, 657]
    lst2.extend(lst1)
    return lst2


def deq_extendleft():
    deq = deque([i for i in range(num)])
    deq.extend([23, 45, 36, 657])
    return deq


print(f'Добавление элементов в список')
print(timeit("lst", "from __main__ import lst", number=10000))

print(f'Добавление элементов в deque')
print(timeit("deq", "from __main__ import deq", number=10000))

print(f'Удаление элемента в списке')
print(timeit("lst_pop", "from __main__ import lst_pop", number=10000))

print(f'Удаление элемента в deque')
print(timeit("deq_pop", "from __main__ import deq_pop", number=10000))

print(f'Расширение списка')
print(timeit("lst_ext", "from __main__ import lst_ext", number=10000))

print(f'Расширение deque')
print(timeit("deq_ext", "from __main__ import deq_ext", number=10000))

print(f'Добавление элемента в начало списка')
print(timeit("lst_insert", "from __main__ import lst_insert", number=10000))

print(f'Добавление элемента в начало deque')
print(timeit("deq_appleft", "from __main__ import deq_appleft", number=10000))

print(f'Удаление первого элемента  списка')
print(timeit("lst_popleft", "from __main__ import lst_popleft", number=10000))

print(f'Удаление первого элемента в deque')
print(timeit("deq_popleft", "from __main__ import deq_popleft", number=10000))

print(f'Добавление нескольких элементов в начало списка')
print(timeit("lst_extendleft", "from __main__ import lst_extendleft", number=10000))

print(f'Добавление нескольких элементов в deque')
print(timeit("deq_extendleft", "from __main__ import deq_extendleft", number=10000))

# Аналитика показала, что операции popleft, appendleft, extendleft у deque будут исполняться быстрее, чем у списка,
# поскольку deque.popleft() – O(1) – операция с постоянным временем, а list.pop(0) – это O(n) – линейная операция времени:
# чем больше список, тем дольше это требуется.
