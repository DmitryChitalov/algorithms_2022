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

def num_dig(n, oddnum=0, evennum=0):
    if len(str(n)) == 1:
        if (n % 2) == 1:
            oddnum += 1
        else:
            evennum += 1
        return (oddnum, evennum)
    else:
        if (n % 10 % 2) == 1:
            oddnum += 1
        else:
            evennum += 1
        n //= 10
        return num_dig(n, oddnum, evennum)


m = int(input('Введите число: '))
print(num_dig(m))

