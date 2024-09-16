"""Конвертация"""


def convert_to_str(n, base_val):
    convert_str = "0123456789ABCDEF"
    if n < base_val:
        return convert_str[n]
    # Здесь выполняются 2-й и 3-й законы рекурсии
    # выполняется рекурсивный вызов и происходит
    # уменьшение размера задания с помощью деления
    else:
        return convert_to_str(n // base_val, base_val) + convert_str[n % base_val]


print(convert_to_str(5, 2))


# convert_to_str(5, 2)
# convert_to_str(2, 2) + 1
# convert_to_str(1, 2) + 0
# convert_to_str(1, 2) -> 1
# начинаем возвраты ->
# 1 + 0
# 1 + 0 + 1
# 1 + 0 + 1
