"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""

def upheaval (number_enter,number_print,zero):
   if not number_enter:
       return ('{}{}'.format(zero, number_print))
   else:
        number_print = number_print * 10 + number_enter % 10
        return(upheaval(number_enter//10,number_print,zero))

number_enter=int(input('Ведите число: '))
number_print=0
countZero = 0
zero = ''
while (number_enter % 10 == 0):
    zero = '0'
    number_enter //= 10
    countZero += 1
    zero = zero * countZero
print(upheaval(number_enter,number_print,zero))
