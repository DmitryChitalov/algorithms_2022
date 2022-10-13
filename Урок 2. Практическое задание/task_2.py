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


def even_odd(number, even_counter=0, odd_counter=0):
    """ функция для подсчёта четных и нечётных цифр в числе """

    last_digit = number % 10
    if last_digit == 0:
        pass
    elif last_digit % 2 == 0:
        even_counter += 1
    elif last_digit % 2 == 1:
        odd_counter += 1

    number = number // 10
    if number == 0:
        return even_counter, odd_counter

    return even_odd(number, even_counter, odd_counter)


if __name__ == '__main__':
    numb = input('Введите число: ')
    try:
        numb = int(numb)
        if numb < 0:
            raise ValueError
    except ValueError:
        print('Нужно было ввести натуральное число')
    else:
        print(f'Количество четных и нечетных цифр в числе равно: {even_odd(numb)}')
