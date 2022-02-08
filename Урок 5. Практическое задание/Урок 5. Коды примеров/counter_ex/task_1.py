"""Класс collections.Counter()"""

from collections import Counter

# создаем объект коллекции
OBJ = Counter(['js', 'java', 'java', 'python', 'python', 'python'])
print(type(OBJ))
print(OBJ)  # -> Counter({'python': 3, 'java': 2, 'js': 1})

# объект на базе словаря
print(OBJ['python'])
print(OBJ['perl'])

OBJ = Counter('abrakadabra')
print(OBJ)  # -> Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})

OBJ = Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})
print(OBJ)  # -> Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})

OBJ = Counter(python=2, java=4, ci=3)
print(list(OBJ.elements()))  # -> ['python', 'python', 'java', 'java',
                                        # 'java', 'java', 'ci', 'ci', 'ci']

print(Counter('abracadabra').most_common(2))  # -> [('a', 5), ('b', 2)]
print(Counter('abracadabra').most_common())  # -> [('a', 5), ('b', 2),
                                            # ('r', 2), ('c', 1), ('d', 1)]
