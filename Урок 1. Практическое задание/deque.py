"""Дек - двустаронняя очередь,  гибрид стека и очереди"""


class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


if __name__ == '__main__':
    dc_obj = DequeClass()
    print(dc_obj.is_empty())

    dc_obj.add_to_rear(10)
    dc_obj.add_to_rear('mystr')
    dc_obj.add_to_front(None)
    dc_obj.add_to_front(True)

    print(dc_obj.size())
    print(dc_obj.is_empty())

    dc_obj.add_to_rear(3.3)

    print(dc_obj.remove_from_rear())
    print(dc_obj.remove_from_front())
