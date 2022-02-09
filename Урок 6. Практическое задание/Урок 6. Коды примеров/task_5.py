"""Профилировка памяти"""

from memory_profiler import profile


class Point:
    def __init__(self, x=0, y=0, lst=[]):
        self.x = x
        self.y = y
        self.lst = list(range(100000))

    def __del__(self):
        class_name = self.__class__.__name__
        print(f'{class_name} уничтожен')


@profile
def func():
    pt1 = Point()
    pt2 = pt1
    pt3 = pt1
    print(id(pt1), id(pt2), id(pt3))
    del pt1
    del pt2
    del pt3


func()
