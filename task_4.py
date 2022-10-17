def row(count, i, j, sum):
    if count == i:
        return f'Количество элементов: {i}, их сумма: {sum}'
    elif count > i:
        return row(count, i + 1, j / -2, sum + j)


con = int(input('Введите количество элементов: '))
print(row(con, 0, 1, 0))
