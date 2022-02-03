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


def count_numb2(n, even=0, odd=0):
    if n == 0:
        print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    else:
        cur_n = n % 10
        n = n // 10
        if cur_n % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_numb2(n, even, odd)


n = int(input("Введите число: "))
count_numb2(n)
