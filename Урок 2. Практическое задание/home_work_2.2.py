def even_odd(num, even=0, odd=0):

    if num == 0:
        return even, odd
    else:
        cur_num = num % 10
        num = num // 10
        if cur_num % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_odd(num, even, odd)


try:
    NUM = int(input("Введите число: "))
    print(f"Количество четных и нечетных цифр в числе: {even_odd(NUM)}")
except ValueError:
    print("Вместо чила ввели строку. Исправьте")
