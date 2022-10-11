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
def even_odd(num, count_even=0, count_odd=0):
    if len(num) == 1:
        if int(num) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        print(f'Кол-во нечетных и четных цифр в числе: ({count_even}, {count_odd})')
    else:
        x = int(num) % 10
        if x % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        num = int(num) // 10
        even_odd(str(num), count_even, count_odd)


if __name__ == '__main__':
    number = input('Введите число:')
    even_odd(number)