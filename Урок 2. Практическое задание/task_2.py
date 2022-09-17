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

num = int(input("Введите  целое число"))
def rec(count=1, a=10, b=1, odd=0, even=0, res=0):
    if count <= len(str(num)):
        res = num % a // b
        if res % 2 == 1:
            return rec(count=count + 1, a=a * 10, b=b * 10, odd=odd+1, even=even, res=res)
        elif res % 2 == 0:
            return rec(count=count + 1, a=a * 10, b=b * 10, odd=odd, even=even+1, res=res)
    # print(f' Количество четных и нечетных цифр в числе равно: ({even}, {odd})')
    return f' Количество четных и нечетных цифр в числе равно: ({even}, {odd})'

rec()