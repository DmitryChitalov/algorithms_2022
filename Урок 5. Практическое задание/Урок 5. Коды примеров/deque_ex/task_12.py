"""Класс collections.deque()"""
# простые операции с очередью
from collections import deque

simple_lst = list("bcd")
deq_obj = deque(simple_lst)
print(deq_obj)  # -> deque(['b', 'c', 'd'])

# добавим элемент в конец и начало очереди
deq_obj.append('e')
print(deq_obj)  # -> deque(['b', 'c', 'd', 'e'])
deq_obj.appendleft('a')
print(deq_obj)  # -> deque(['a', 'b', 'c', 'd', 'e'])

# pop также работает с обоих концов
deq_obj.pop()  # -> deque(['a', 'b', 'c', 'd'])
print(deq_obj)
deq_obj.popleft()  # -> deque(['b', 'c', 'd'])
print(deq_obj)

# extend также работает с обоих концов
deq_obj.extend(['x', 'y', 'z'])
print(deq_obj)  # -> deque(['b', 'c', 'd', 'x', 'y', 'z'])
deq_obj.extendleft(['k', 'l', 'm'])
print(deq_obj)  # -> deque(['m', 'l', 'k', 'b', 'c', 'd', 'x', 'y', 'z'])
