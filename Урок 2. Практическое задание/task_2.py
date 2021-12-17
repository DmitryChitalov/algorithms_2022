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


def count_dig(number, counter=[0, 0]):
    dig = number - (number // 10) * 10  # - получаем младший разряд
    if dig % 2 == 0:
        counter[0] += 1
    else:
        counter[1] += 1
    if number < 10:
        return counter
    else:
        return count_dig(number // 10, counter)


num = int(input('Введите число \n'))
total = count_dig(num)
print('В числе %s колчество четных цифр : %s, нечетных : %s' % (num, total[0], total[1]))
