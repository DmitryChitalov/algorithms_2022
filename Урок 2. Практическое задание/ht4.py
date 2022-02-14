
def func_sum(n):
    return 0 if n == 0 else 1 - func_sum(n-1) / 2
try:
    number = int(input('Введите количество элементов: '))
    print(func_sum(number))
except ValueError:
    print(f'Введен неверный формат числа!')