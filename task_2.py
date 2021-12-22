def even_odd_amount(num, even_nums, odd_nums):
    if num == 0:
        return even_nums, odd_nums
    else:
        num = int(num)
        last_num = num % 10
        if last_num % 2 == 0:
            even_nums += 1
        else:
            odd_nums += 1
        return even_odd_amount(num // 10, even_nums, odd_nums)


try:
    test_1 = even_odd_amount(input('Введите число: '), 0, 0)
    print(test_1)
except ValueError:
    print('Нужно вводить числа')
