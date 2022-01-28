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


def count_parity(nums, even=0, not_even=0):
    if nums == 0:  # с базового случая начнется разворот
        return even, not_even  # возвращаем счетчики
    else:
        num = nums % 10  # отделяем число
        nums = nums // 10  # от исходного окалываем последнее число

        if num % 2 == 0:  # если четное, то прибавляем к четному счетчику
            even += 1
        else:  # если не четное, то не к четному
            not_even += 1

        return count_parity(nums, even, not_even)  # вызываем функцию с другими даными


print(count_parity(int(input())))