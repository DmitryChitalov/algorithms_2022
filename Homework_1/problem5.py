class Stack:
    def __init__(self, n):
        self.plates = []
        self.max_num = n
        self.full_stacks = []

    def last_size(self):
        return self.plates[len(self.plates) - 1]

    def height(self):
        return len(self.plates)

    def is_empty(self):
        return self.plates == []

    def pick_one_up(self):
        return self.plates.pop()

    def put_on_top(self, plate_size):
        if self.height() == self.max_num:
            self.full_stacks.append(self.plates)
            self.plates = []
        self.plates.append(plate_size)

    def show_stacks(self):
        self.full_stacks.append(self.plates)
        print(self.full_stacks)
        self.full_stacks = self.full_stacks[:-1]

stack_1 = Stack(6)
print(stack_1.is_empty())
stack_1.put_on_top(1)
stack_1.put_on_top(2)
stack_1.put_on_top(3)
stack_1.put_on_top(4)
stack_1.put_on_top(5)
stack_1.put_on_top(6)
stack_1.put_on_top(7)
print(stack_1.last_size())
stack_1.put_on_top(8)
stack_1.put_on_top(9)
stack_1.pick_one_up()
stack_1.put_on_top(10)
print(stack_1.height())
print(stack_1.is_empty())
stack_1.show_stacks()