def split_the_num(number: int, even=0, odd=0):
    if number // 10 == 0:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        return even, odd
    if number % 10 % 2 == 0:
        even += 1
    else:
        odd += 1
    return split_the_num(number // 10, even, odd)


num = int(input('Введите натуральное число'))
even_index, odd_index = split_the_num(num)
print(f' Число {num}: четных: {even_index}, нечетных {odd_index}')
