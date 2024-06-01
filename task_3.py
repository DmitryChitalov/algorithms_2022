def num_reverse(num):
    reversed = ''
    if num == 0:
        return reversed
    else:
        num = int(num)
        last_num = num % 10
        return str(last_num) + str(num_reverse(num // 10))


try:
    test_1 = num_reverse(input('Введите число: '))
    print(test_1)
except ValueError:
    print('Нужно вводить числа')
