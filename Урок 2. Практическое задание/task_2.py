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


def check_num(num, ce, co):
    if (num % 10) % 2 == 0:
        ce += 1
    else:
        co += 1
    if num // 10 == 0:
        return f'Четных: {ce} Нечетных: {co}'
    return check_num((num // 10), ce, co)


if __name__ == '__main__':
    print(check_num(int(input('Введите число: ')), 0, 0))
