def invert(n):
    if n < 10:
        return str(n)
    else:
        return str(n % 10) + invert(n // 10)


print(f'Перевернутое число: ', invert(int(input("Введите число: "))))
