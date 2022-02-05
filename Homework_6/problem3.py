from memory_profiler import profile

# Класс из задания #2 урока №5

class SixDigits:
    def __init__(self, lst):
        lst = [x for x in lst]
        self.digs = lst

    @profile
    def __add__(self, other):
        n = int(''.join([x for x in self.digs]).split()[0], 16)
        n += int(''.join([x for x in other.digs]).split()[0], 16)
        return hex(n)[2:].upper()

    @profile
    def __mul__(self, other):
        n = int(''.join([x for x in self.digs]).split()[0], 16)
        n *= int(''.join([x for x in other.digs]).split()[0], 16)
        return hex(n)[2:].upper()

ch1 = SixDigits("A2")
ch2 = SixDigits("C4F")

print(ch1 + ch2)
print(ch1 * ch2)

# Заменили решением без перегрузки

@profile
def am(a, b, st):
    if st == '+':
        return print(int(a, 16) + int(b, 16))
    elif st == '*':
        return print(int(a, 16) * int(b, 16))

am("2A", "3B", '*')