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


def find_sum_cycle(num):
    res = 1
    cur_num = 1
    for i in range(num - 1):
        cur_num = cur_num / 2 if cur_num > 0 else cur_num / 2 * -1

        if i % 2 == 0:
            cur_num = cur_num * -1
        res += cur_num

    return res


def find_sum(num):
    num -= 1
    current_num = 1 / 2 ** num
    if num == 0:
        return 1

    if num % 2 != 0:
        current_num = current_num * -1

    return current_num + find_sum(num)


if __name__ == "__main__":
    quantity = int(input("Enter the number: "))
    print(find_sum_cycle(quantity))
    print(find_sum(quantity))
