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
    print(dc_obj.is_empty())  # -> True

    # добавить элементы в хвост
    dc_obj.add_to_rear(10)
    dc_obj.add_to_rear('my_str')

    # добавить элементы в голову
    dc_obj.add_to_front(None)
    dc_obj.add_to_front(True)

    # размер дека
    print(dc_obj.size())  # -> 4
    print(dc_obj.is_empty())  # -> False

    # добавить элемент в хвост
    dc_obj.add_to_rear(3.3)

    print(dc_obj.remove_from_rear())  # -> 3.3
    print(dc_obj.remove_from_front())  # -> True


def pal_checker(string):
    dc_obj = DequeClass()

    for el in string.replace(" ", ""):
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))

print(f"а роза упала на лапу азора --> " + str(pal_checker("а роза упала на лапу азора")))
print(f"баба заругала балагура за баб --> " + str(pal_checker("баба заругала балагура за баб")))
print(f"дорого небо да надобен огород --> " + str(pal_checker("дорого небо да надобен огород")))
