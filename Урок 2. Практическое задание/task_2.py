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

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


class Counter:
    """
    Класс для ведения одновременно двух счетчиков.
    Сумма двух счетчиков равна счетчику, компоненты которого равна сумме компонентов 
    Пример: (1,0) + (0,1) = (1,1)
    """

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __add__(self, other):
        return Counter(self.a + other.a, self.b + other.b)

    def __str__(self) -> str:
        return f'{self.a}, {self.b}'


def even_count(num):
    if num < 10:
        if (num % 10) % 2 == 0:
            return Counter(1, 0)
        else:
            return Counter(0, 1)
    else:
        if (num % 10) % 2 == 0:
            return even_count(num // 10) + Counter(1, 0)
        else:
            return even_count(num // 10) + Counter(0, 1)


print(even_count(87881))
print(even_count(1200))
