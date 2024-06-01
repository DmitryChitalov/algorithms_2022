def check_equality(num):
    return num if num == 1 else num + check_equality(num-1)


test_1 = int(input('Введите число: '))
if check_equality(test_1) == test_1 * (test_1 + 1) / 2:
    print('Равенство выполняется')
else:
    print('Равенство не выполняется')
