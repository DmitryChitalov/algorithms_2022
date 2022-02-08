class HexNumber:
    def __init__(self, value):
        self.value = int(value, 16)

    def __str__(self):
        result = str(hex(self.value)).split('x')[1].upper()
        return f'{result}'

    def __add__(self, other):
        res = self.value + other.value
        return str(hex(res)).split('x')[1].upper()

    def __mul__(self, other):
        res = self.value * other.value
        return str(hex(res)).split('x')[1].upper()


x = HexNumber('A2')
y = HexNumber('B2')
print(x + y)
print(x * y)
