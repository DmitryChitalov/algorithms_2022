from sys import getsizeof
from pympler.asizeof import asizeof


# Хранение информации в словаре занимает больше памяти
d = {1: '1', 2: '2', 3: '3'}
print(getsizeof(d))  # -> 232
print(asizeof(d))  # -> 496

# Код можно оптимизировать, используя вместо словаря, кортеж
#Хранение информации в кортеже занимает меньше памяти
t = (1, 2, 3)
print(getsizeof(t))  # -> 64
print(asizeof(t))  # -> 160