"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""
from pympler import asizeof                                                                                  
                                                                                                             
                                                                                                             
class HexOperation:                                                                                          
    def __init__(self, numb_1, numb_2):                                                                      
        self.numb_1 = numb_1                                                                                 
        self.numb_2 = numb_2                                                                                 
                                                                                                             
    def __add__(self, other):                                                                                
        return list(hex(int(''.join(self.numb_1), 16) + int(''.join(other.numb_2), 16)))[2:]                 
                                                                                                             
    def __mul__(self, other):                                                                                
        return list(hex(int(''.join(self.numb_1), 16) * int(''.join(other.numb_2), 16)))[2:]                 
                                                                                                             
                                                                                                             
hex_num_1 = list(input("Введите первое шестнадцатеричное число: "))                                          
hex_num_2 = list(input("Введите второе шестнадцатеричное число: "))                                          
                                                                                                             
sum_hex_num = HexOperation(hex_num_1, hex_num_2) + HexOperation(hex_num_1, hex_num_2)                        
                                                                                                             
mult_hex_num = HexOperation(hex_num_1, hex_num_2) * HexOperation(hex_num_1, hex_num_2)                       
                                                                                                             
print(asizeof.asizeof(sum_hex_num))                                                                          
                                                                                                             
# 248                                                                                                        
                                                                                                             
                                                                                                             
                                                                                                                                                                                    
#print(f'Сумма числел равно: {sum_hex_num}')                                                                 
#print(f'Произведение числел равно: {mult_hex_num}')                                                         
                                                                                                             
                                                                                                             
                                                                                                             
class HexOperation:                                                                                          
    __slots__ = ['numb_1', 'numb_2']                                                                         
                                                                                                             
    def __init__(self, numb_1, numb_2):                                                                      
        self.numb_1 = numb_1                                                                                 
        self.numb_2 = numb_2                                                                                 
                                                                                                             
    def __add__(self, other):                                                                                
        return list(hex(int(''.join(self.numb_1), 16) + int(''.join(other.numb_2), 16)))[2:]                 
                                                                                                             
    def __mul__(self, other):                                                                                
        return list(hex(int(''.join(self.numb_1), 16) * int(''.join(other.numb_2), 16)))[2:]                 
                                                                                                             
                                                                                                             
hex_num_1 = list(input("Введите первое шестнадцатеричное число: "))                                          
hex_num_2 = list(input("Введите второе шестнадцатеричное число: "))                                          
                                                                                                             
sum_hex_num = HexOperation(hex_num_1, hex_num_2) + HexOperation(hex_num_1, hex_num_2)                        
                                                                                                             
mult_hex_num = HexOperation(hex_num_1, hex_num_2) * HexOperation(hex_num_1, hex_num_2)                       
                                                                                                             
print(asizeof.asizeof(sum_hex_num))                                                                          
                                                                                                             
# 248                                                                                                        
                                                                                                             
                                                                       
#print(f'Сумма числел равно: {sum_hex_num}')                                                                 
#print(f'Произведение числел равно: {mult_hex_num}')                                                         