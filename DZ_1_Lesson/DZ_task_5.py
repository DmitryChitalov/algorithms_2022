class tarelki:
    def __init__(self, max_stack):
        self.base_list = [[]]
        self.max_stack = max_stack

    def put_in(self, value):
        if len(self.base_list[-1]) < self.max_stack:
            self.base_list[-1].append(value)
        else:
            self.base_list.append([])
            self.base_list[-1].append(value)
        return self.base_list

    def delte_plate(self):
        self.base_list[-1].pop()
        if len(self.base_list[-1]) == 0:
            self.base_list.pop()
        return self.base_list

    def all_plates(self):
        count = 0
        for i in self.base_list:
            count += len(i)
        return count


plates = tarelki(3)
print(plates.put_in("plate_1"))
print(plates.put_in("plate_2"))
print(plates.put_in("plate_3"))
print(plates.put_in("plate_4"))
print(plates.delte_plate())
print(plates.all_plates())