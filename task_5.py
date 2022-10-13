
class StackClass:
    def __init__(self, size):
        self.elems = []
        self.size = size

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems) >= self.size:
            self.elems.append([])
        else:
            self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    SC_OBJ = StackClass(100)

    print(SC_OBJ.is_empty())

    SC_OBJ.push_in(15)
    SC_OBJ.push_in(57)
    SC_OBJ.push_in(135)
    SC_OBJ.push_in(8)

    print(SC_OBJ.get_val())
    print(SC_OBJ.stack_size())
    print(SC_OBJ.is_empty())

    SC_OBJ.push_in(5)

    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.stack_size())