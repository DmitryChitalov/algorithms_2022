import sys

from collections import namedtuple
from recordclass import recordclass


def rc_demo():
    var_1 = recordclass('var_1', ('x', 'y', 'z'))  # использование recordclass - позволяет уменьшить объем памяти
    var_2 = namedtuple('var_2', ('x', 'y', 'z'))
    c = {'x': 1, 'y': 2, 'z': 3}
    a = var_1(x=1, y=2, z=3)
    b = var_2(x=1, y=2, z=3)
    a.x = 4

    print(f'Объём занимаемой объектом recordclass памяти: '
          f'{sys.getsizeof(a)} байт(а)')
    print(f'Объём занимаемой объектом namedtuple памяти: '
          f'{sys.getsizeof(b)} байт(а)')
    print(f'Объём занимаемой объектом dict памяти:'
          f' {sys.getsizeof(c)} байт(а)')


rc_demo()

'''
Объём занимаемой объектом recordclass памяти: 40 байт(а)
Объём занимаемой объектом namedtuple памяти: 64 байт(а)
Объём занимаемой объектом dict памяти: 232 байт(а)
'''
