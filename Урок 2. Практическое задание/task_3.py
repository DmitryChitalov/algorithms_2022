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

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230->3210
"""

def get_number(mess):
    try:
        num = int(input(mess))
        return num
    except ValueError:
        print('You enter wrong number')
        return get_number(mess)


def reverse(number: int) -> str:
    def recursion_reverse(number):
        if number < 10:
            return [number]

        number, remain = divmod(number, 10)
        return [remain] + recursion_reverse(number)
    
    result_list = recursion_reverse(number)
    result_list_str = [str(num) for num in result_list]
    return ''.join(result_list_str)
    
number = get_number('Enter number for reverse: ')

print(reverse(number))