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
def user_enter():
    users = input('Введите количество элементов: ')
    if not (users.isdecimal()):
        print('Вместо числа введена строка! Исправьтесь')
        return user_enter()
    return int(users)

def quantity_elem(count, elem, users, my_sum):
    if count == users:
        print(f"Количество элементов - {users}, их сумма - {my_sum}")
    elif count < users:
        return quantity_elem(count + 1, elem/2 * -1, users, my_sum + elem)

if __name__ == "__main__":
    quantity_elem(0, 1, user_enter(), 0)
