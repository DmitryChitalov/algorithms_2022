"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_rec(number, current_val=1):
    if number == 1:
        return current_val
    return current_val + sum_rec(number - 1, current_val / -2.0)


def main():
    try:
        number = int(input('Введите количество элементов: '))
    except ValueError:
        print("Нужео ввести число а не строку")
        return
    summ = sum_rec(number)
    print(f"Количество элементов: {number}\nИх сумма : {summ}")

if __name__ == '__main__':
    main()