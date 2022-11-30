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


def odd_even(number,odd_numbered,even_numbered):
    if not number:
        return (odd_numbered,even_numbered)
    if number % 2 == 1:
        odd_numbered += 1
    else:
        even_numbered += 1
    return odd_even(number//10, odd_numbered,even_numbered )

number = int(input('введите число: '))
even_numbered = 0
odd_numbered = 0
print(odd_even(number,odd_numbered,even_numbered))

