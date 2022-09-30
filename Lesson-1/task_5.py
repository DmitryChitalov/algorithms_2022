class PlatesStack:
    def __init__(self, num_el):
        self.elems = []
        self.num_el = num_el

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.elems) == 0:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)
        elif len(self.elems[len(self.elems) - 1]) < self.num_el:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    SC_OBJ = PlatesStack(5)

    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(7)
    SC_OBJ.push_in(11)
    SC_OBJ.push_in(4.8)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(10.8)
    SC_OBJ.push_in(11)

    print(SC_OBJ.get_val())
    print(SC_OBJ.stack_size())
    print(SC_OBJ.is_empty())
    SC_OBJ.push_in(4.4)
    print(SC_OBJ.stack_size())
    print(SC_OBJ.elems)
