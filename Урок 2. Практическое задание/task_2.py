"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

# Вариант 1
my_number = int(input("Введите натуральное число: "))
def number_parsing(number, even_numbers=0, odd_numbers=0):
    if number == 0:
        return even_numbers, odd_numbers
    else:
        if number // 10 >= 0 and number % 2 != 0:
            odd_numbers += 1
            number = number // 10
        else:
            even_numbers += 1
            number = number // 10
        return number_parsing(number, even_numbers, odd_numbers)

print(f'Количество четных и нечетных чифр в числе равно: {number_parsing(my_number)}')

# Вариант 2

even_numbers = []
odd_numbers = []
my_number = int(input("Введите натуральное число: "))
def number_parsing(number):
    if number == 0:
        return len(even_numbers), len(odd_numbers)
    else:
        if number // 10 >= 0 and number % 2 != 0:
            odd_numbers.append(1)
            number = number // 10
        else:
            even_numbers.append(1)
            number = number // 10
        return number_parsing(number)

print(f'Количество четных и нечетных чифр в числе равно: {number_parsing(my_number)}')
