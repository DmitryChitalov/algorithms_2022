from collections import deque
from random import randint


lst = [randint(0,100) for i in range(0, 20)]
deq = deque(lst)
ext_lst = [i for i in range(0, 20)]

for i in range(len(lst)):
    lst.pop(0)
    print(lst)

# for i in deq:
#     deq.popleft()