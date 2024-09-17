num = int(input('Введите число: '))
even = odd = 0


def calc():
    global even
    global odd
    global num

    if num == 0:
        return f'чётных - {even}, нечётных - {odd}'


    elif num % 2 == 0 or num == 0:
        even += 1
        num = num // 10
        return calc()
    else:
        odd += 1
        num = num // 10
        return calc()


print(calc())
