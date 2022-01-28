def revers_number(num):

    rest_num, numeral_1 = divmod(num, 10)
    if rest_num == 0:
       return str(numeral_1)
    else:
        return str(numeral_1) + str(revers_number(rest_num))


number = int(input("Введите число, которое требуется перевернуть: "))
print(f"перевернутое число: {revers_number(number)}")
