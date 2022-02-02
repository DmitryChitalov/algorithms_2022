class SixDigits:
    def __init__(self, lst):
        lst = [x for x in lst]
        self.digs = lst

    def __add__(self, other):
        n = int(''.join([x for x in self.digs]).split()[0], 16)
        n += int(''.join([x for x in other.digs]).split()[0], 16)
        return hex(n)[2:].upper()

    def __mul__(self, other):
        n = int(''.join([x for x in self.digs]).split()[0], 16)
        n *= int(''.join([x for x in other.digs]).split()[0], 16)
        return hex(n)[2:].upper()

ch1 = SixDigits("A2")
ch2 = SixDigits("C4F")

print(ch1 + ch2)
print(ch1 * ch2)
