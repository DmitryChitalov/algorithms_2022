"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""
def recur_method(i, numb, n_count, common_sum):
    """Рекурсия"""
    if i == n_count:
        print(f"Количество элементов - {n_count}, их сумма - {common_sum}")
    elif i < n_count:
        return recur_method(i + 1, numb / 2 * -1, n_count, common_sum+numb)


try:
    N_COUNT = int(input("Введите количество элементов: "))
    recur_method(0, 1, N_COUNT, 0)
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")


"""
def recur_method(elem):
    '''Через тернарный оператор'''
    return 0 if elem == 0 else 1 + recur_method(elem - 1) / - 2


N_COUNT = int(input('Введите количество элементов: '))
print(f'Количество элементов: {N_COUNT}, их сумма: {recur_method(N_COUNT)}')
"""