def count(num, num_1 = 0, num_2 = 0):
    if num == 0:
        return f'Количество четных и нечетных цифр в числе равно: ({num_1}, {num_2})'
    else:
        res = num % 10
        if res % 2 == 0:
            num_1 += 1
            return count(num // 10, num_1, num_2)
        elif res % 2 == 1:
            num_2 += 1
            return count(num // 10, num_1, num_2)

try:
    print(count(int(input('Введите число: '))))
except ValueError:
    print("Ошибка: Вместо строки введите число!")
    print(count(int(input('Введите число: '))))
