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


def counting_even_and_odd_digits(natural_number, count_an_even_number, count_odd_number):
    member = count_an_even_number + count_odd_number
    if len(natural_number) > member:
        if int(natural_number[member]) % 2 == 0:
            count_an_even_number += 1
        else:
            count_odd_number += 1
    else:
        print(f"Количество четных и нечетных цифр в числе: {count_an_even_number, count_odd_number}")
        return "Выход"
    counting_even_and_odd_digits(natural_number, count_an_even_number, count_odd_number)


instance_of_natural_number = input()


counting_even_and_odd_digits(instance_of_natural_number, 0, 0)

