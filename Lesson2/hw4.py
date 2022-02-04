def my_func(i, number, my_num, my_sum):
    if i == my_num:
        print(f'Количество элементов - {my_num}, их сумма - {my_sum}')

    elif i < my_num:
        return my_func(i + 1, number / 2 * -1, my_num, my_sum + number)


try:
    my_num = int(input('Введите количество элементов: '))
    my_func(0, 1, my_num, 0)
except ValueError:
    print("Вы ввели строку вместо числа")
