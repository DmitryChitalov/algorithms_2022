def calc(number, even=0, uneven=0):
    if number == 0:
        print(f'Нечетных цифр: {uneven}')
        print(f'Четных цифр: {even}')
        return
    else:
        n = number % 10
        number = number // 10
        if n % 2 == 1:
            uneven += 1
        elif n % 2 == 0:
            even += 1
        return calc(number, even, uneven)

try:
    number = int(input('Введите натуральное число: '))
    calc(number)
except ValueError:
    print(f'Введен неверный формат числа!')