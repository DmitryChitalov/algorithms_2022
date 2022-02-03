"""Класс collections.deque()"""
"""В соответствии с документацией Python, 
deque – это обобщение стеков и очередей. 
Вот основное правило: если вам нужно что-то быстро! дописать или вытащить,
используйте deque. 
Если вам нужен быстрый случайный доступ, используйте list?"""

import string
from collections import deque

# формируем очередь из элементов-заглавных букв
NEW_DEQUE = deque(string.ascii_uppercase)
print(NEW_DEQUE)

# итерируем очередь
for el in NEW_DEQUE:
    print(el, end=' ')
print()

# добавляем элемент в конец очереди
NEW_DEQUE.append('end')
print(NEW_DEQUE)

# добавляем элемент в начало очереди
NEW_DEQUE.appendleft('start')
print(NEW_DEQUE)

# перемещаем два элемента с конца очереди в начало
NEW_DEQUE.rotate(2)
print(NEW_DEQUE)

# перемещаем два элемента с начала очереди в конец
NEW_DEQUE.rotate(-2)
print(NEW_DEQUE)

print(NEW_DEQUE[1])
