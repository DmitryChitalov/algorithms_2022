class StackClass:
    def __init__(self):
        self.elems = [[]]

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def push_in(self, el, n):
        if len(self.elems[len(self.elems) - 1]) < n:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elems)




def divide_by_two(dec_number):
    sc_obj = StackClass()

    while dec_number > 0:
        res = dec_number % 2
        sc_obj.push_in(res, 2)
        dec_number = dec_number // 2
    return sc_obj

print(divide_by_two(233))