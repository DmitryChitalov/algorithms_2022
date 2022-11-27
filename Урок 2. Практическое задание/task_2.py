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


def even_uneven_numbers(user_input, even_numbers=0, uneven_numbers=0):
    if user_input // 10 == 0:
        if user_input % 2 == 0:
            even_numbers += 1
        else:
            uneven_numbers += 1
        print(f'Количество четных и нечетных цифр в числе равно:({even_numbers}, {uneven_numbers})')
    else:
        last_number = user_input % 10
        if last_number % 2 == 0:
            even_numbers += 1
        else:
            uneven_numbers += 1
        user_input = user_input // 10
        return even_uneven_numbers(user_input, even_numbers, uneven_numbers)


try:
    number = int(input('Введите число: '))
    even_uneven_numbers(number)
except ValueError:
    print('Вы ввели строку, попробуйте снова!')
    number = int(input('Введите число: '))
    even_uneven_numbers(number)
