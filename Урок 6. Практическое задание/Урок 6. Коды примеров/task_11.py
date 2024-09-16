from sys import getsizeof
from pympler.asizeof import asizeof


d = {1: '1', 2: '2', 3: '3'}
print(getsizeof(d))  # -> 240
print(asizeof(d))  # -> 504

t = (1, 2, 3)
print(getsizeof(t))  # -> 72
print(asizeof(t))  # -> 168
