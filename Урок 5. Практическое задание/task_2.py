"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""

class AddMult:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def save(self):
        for_num1 = []
        for_num2 = []
        
        for elem in self.number1:
            for_num1.append(elem)

        print 'Первое число сохраенно как: {}'.format(for_num1)

        for ele in self.number2:
            for_num2.append(ele)

        print 'Второе число сохранено как: {}'.format(for_num2)

    def summ(self):
    
        self.save()
        
        summ = int(self.number1, 16) + int(self.number2, 16)
        summ = hex(summ)
        summ = summ[2:]
        
        for_summ = []
        
        for elem in summ:
            for_summ.append(elem)
            
        print 'Сумма чисел: {}'.format(for_summ)
        
        self.mult()

    def mult(self):
    
        mult = int(self.number1, 16) * int(self.number2, 16)
        mult = hex(mult)
        mult = mult[2:]
        
        for_mult = []
        
        for elem in mult:
            for_mult.append(elem)
            
        print 'Произведение чисел: {}'.format(for_mult)


if __name__ == '__main__':

    number1 = raw_input('Введите первое число - каждую цифру через пробел: ')
    number2 = raw_input('Введите второе число - каждую цифру через пробел: ')
    
    a = AddMult(number1=number1, number2=number2)
    a.summ()
