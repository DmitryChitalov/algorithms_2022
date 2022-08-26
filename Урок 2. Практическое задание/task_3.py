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


def change_numbers(number: int, ost: str = '') -> str:
    """Функция принимает в себя число, а также пустую по умолчанию строку.
    Отделяет последнюю цифру числа в отдельную строку и рекурсивно вызывает сама себя"""
    if len(str(number)) > 1:
        last = str(number % 10)
        ost += last
        change_numbers(number // 10, ost)
    else:
        ost += str(number)
        return f'Перевернутое число: {ost}'


#change_numbers(1234567890)
print(change_numbers(int(input('Введите число: '))))