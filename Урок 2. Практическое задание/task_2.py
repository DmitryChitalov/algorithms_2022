def recur_method(numb, even=0, odd=0):
    """Рекурсия"""
    # все цифры числа извлечены
    if numb == 0:
        return even, odd
    else:
        # достаем очередную цифру числа
        cur_n = numb % 10
        # число естественно становится короче
        numb = numb // 10
        # проверяем цифра четная или нечетная
        if cur_n % 2 == 0:
            even += 1
        else:
            odd +=1
        return recur_method(numb, even, odd)

try:
    NUMB = int(input("Введите натуральное число: "))
    print(f"Количество четных и нечетных чисел в числе: {recur_method(NUMB)}")
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")