"""
Что нужно в классе:
1. инициализация: закидываем число в 16-ной системе, превращаем в список
2. вывод str
2. перегрузка add: посимвольно склеиваем число, переводим в int, считаем сумму, переводим в hex,
создаём из получившегося числа объект класса
3. перегрузка mul: аналогично предыдущему с точность до замены операции
"""


class CalcHex():
    def __init__(self, num_str):
        self.hex_num = list(num_str)

    def __str__(self):
        return str(self.hex_num[2::])

    def __add__(self, other):
        return CalcHex(hex(int(''.join(self.hex_num), 16) + int(''.join(other.hex_num), 16)))

    def __mul__(self, other):
        return CalcHex(hex(int(''.join(self.hex_num), 16) * int(''.join(other.hex_num), 16)))


num1 = CalcHex(input('Введите первое число: '))
num2 = CalcHex(input('Введите второе число: '))

print(num1 + num2)
print(num1 * num2)
