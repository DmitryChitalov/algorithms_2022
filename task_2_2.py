class HexClass:
    def __init__(self, num_1):
        self.num_1 = num_1

    def __add__(self, other):
        sum_nums = int(''.join(self.num_1), 16) + int(''.join(other.num_1), 16)
        return list(f'{sum_nums:X}')

    def __mul__(self, other):
        mult_nums = int(''.join(self.num_1), 16) * int(''.join(other.num_1), 16)
        return list(f'{mult_nums:X}')


h1 = HexClass('A2')
h2 = HexClass('C4F')

print(h1 + h2)
print(h1 * h2)
