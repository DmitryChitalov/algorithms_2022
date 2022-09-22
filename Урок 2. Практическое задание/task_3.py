def revers_number(numb):
    """Рекурсия"""
    rest_numb, numeral = divmod(numb, 10)
    if rest_numb == 0:
        return str(numeral)
    else:
        return str(numeral) + str(revers_number(rest_numb))


"""
def revers_number(num):
    '''Через тернарный оператор'''
    return str(num) if num < 10 else str(num % 10) + revers_number(num // 10)
"""

number = int(input("Введите число, которое требуется перевернуть: "))
print(f'Перевернутое число: {revers_number(number)}')
