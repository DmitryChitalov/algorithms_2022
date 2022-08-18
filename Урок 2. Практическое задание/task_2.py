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


def check_numbers(number: int, odd_digits: int = 0, even_digits: int = 0):
    """Функция принимает в себя число, а также количество четных и нечетных цифр в числе,
    которые по умолчанию равны нулю, до тех пор пока длинна числа больше 1, функция отделяет последнюю цифру
    и проверяет ее на четность и рекурсивно вызывает сама себя передавая в себя остаток числа и результаты проверки"""
    if len(str(number)) > 1:
        num = number % 10
        if num % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
        check_numbers(number // 10, odd_digits, even_digits)
    else:
        if number % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
        print(f'Количество четных цифр: {even_digits}, Количество нечетных цифр: {odd_digits}')


check_numbers(int(input('Введите число: ')))
